import json
import os
import random
import bottle
import numpy as np
from Snake import snake

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

    color = "#505565"

    return start_response(color)


def get_direction(d):
    directions = ['up', 'down', 'left', 'right']
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    for i in range(len(dirs)):
        if d == dirs[i]:
            return directions[i]

def validate(snake, path, thresh=0.7):
    valid = True
    for point in path:
        if not snake.can_move(point):
            valid = False
    valid = valid and snake.calc_conn(path[-1]) >= thresh
    return valid



@bottle.post('/move')
def move():
    data = bottle.request.json
    print(data['turn'])

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    s = snake(data)
    global PATH
    success = True

    if (len(PATH) <=1) or not validate(s,PATH[1:]):
        PATH = []
        success = s.DLS(s.get_head(), PATH, np.zeros(s.board.shape),lim=s.data['you']['health']-1,thresh=0)
        print(PATH)
    else:
        print(PATH)
        print("PATH REUSE")
    
    
        

    if success:
        d = s.get_dir(PATH[0], PATH[1])
        print(get_direction(d))
        PATH = PATH[1:]
        return move_response(get_direction(d))
        
    
    # choices = s.get_adj(s.get_head())
    # if len(choices)>0:
    #     choices_sorted = s.sort(choices, lambda e_1, e_2: s.calc_conn(e_1) > s.calc_conn(e_2))
    #     choice = choices_sorted[0]
    #     choice_d = s.get_dir(s.get_head(), choice)
    #     print(choices_sorted)
    #     return move_response(get_direction(choice_d))

    choices = s.get_adj(s.get_head())
    if len(choices)>0:
        choice = random.choice(choices)
        choice_d = s.get_dir(s.get_head(), choice)
        return move_response(get_direction(choice_d))
    
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
