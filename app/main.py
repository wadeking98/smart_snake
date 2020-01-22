import json
import os
import random
import bottle
import numpy as np
import time
from Snake import snake
from Node import node

from api import ping_response, start_response, move_response, end_response

PATH = []

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """

    color = "#DC7633"

    return {
            "color": "#58D68D",
            "headType": "fang",
            "tailType": "hook"
            }


def get_direction(d):
    directions = ['up', 'down', 'left', 'right']
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    for i in range(len(dirs)):
        if d == dirs[i]:
            return directions[i]

def validate(snake, path, thresh=0.7):
    valid = snake.get_head() == path[0]
    for point in path[1:]:
        if not snake.can_move(point):
            valid = False

    valid = valid and snake.calc_conn_ratio(path[-1]) >= thresh
    return valid



@bottle.post('/move')
def move():
    data = bottle.request.json

    start_time = time.time()

    print(data['turn'])

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    s = snake(data)
    thresh = 0.7
    search_type = 0 if (data["turn"] < 50) and len(data["board"]["snakes"]) > 1 else -1
    response = None

    if data["turn"] == 1:
        print(s.get_head())
        print(s.board)
        

    
    PATH = []

    #find a good dls path
    goal_n = s.LS(search_type, [node(s.get_head())], np.zeros(s.board.shape), np.zeros(s.board.shape),lim=s.data['you']['health']-1, thresh=thresh)
    
    if goal_n is not None:
        PATH = goal_n.traceback()
        d = s.get_dir(PATH[0], PATH[1])
        #PATH = PATH[1:]
        print("LS:",PATH,get_direction(d))
        response = get_direction(d)

    #move to a well connected tile
    elif len(s.get_adj(s.get_head()))>0:
        #choices_sorted = s.sort(s.get_adj(s.get_head()), lambda e_1, e_2: s.calc_conn_ratio(e_1) > s.calc_conn_ratio(e_2))
        choices_sorted = s.sort(s.get_adj(s.get_head()), s.compare_conn)
        choice = choices_sorted[0]
        choice_d = s.get_dir(s.get_head(), choice)
        print("ADJ: ",choices_sorted, get_direction(choice_d))
        response = get_direction(choice_d)

    #find a potentially poor dls path
    else:
        goal_n_poor = s.LS(search_type, [node(s.get_head())], np.zeros(s.board.shape), np.zeros(s.board.shape),lim=s.data['you']['health']-1, thresh=thresh,panic=True)
        if goal_n_poor is not None:
            PATH = goal_n_poor.traceback()
            d = s.get_dir(PATH[0], PATH[1])
            print("LS PANIC:",get_direction(d))
            #PATH = PATH[1:]
            response = get_direction(d)

        #move to a potentially poorly connected tile
        elif len(s.get_adj(s.get_head(),panic=True))>0:
            #choices_sorted = s.sort(s.get_adj(s.get_head(),panic=True), lambda e_1, e_2: s.calc_conn_ratio(e_1) > s.calc_conn_ratio(e_2))
            choices_sorted = s.sort(s.get_adj(s.get_head(),panic=True), s.compare_conn)
            choice = choices_sorted[0]
            choice_d = s.get_dir(s.get_head(), choice)
            print("ADJ PANIC: ",choices_sorted, get_direction(choice_d))
            response = get_direction(choice_d)
        
        #move randomly
        else:
            directions = ['up', 'down', 'left', 'right']
            response = random.choice(directions)

    

    end_time = time.time()
    print(str((end_time-start_time)*1000)+"ms")
    return move_response(response)

    
    
        

    
        
    
    

    
    
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '7998'),
        debug=os.getenv('DEBUG', True)
    )
