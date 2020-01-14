import json
import os
import random
import bottle
import numpy as np
from Snake import snake


from api import ping_response, start_response, move_response, end_response



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



@bottle.post('/move')
def move():
    data = bottle.request.json
    print(data['turn'])

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    s = snake(data)

    path = []
    success = s.DLS(s.get_head(), path, np.zeros(s.board.shape),lim=s.data['you']['health'])
    if not success:
        conn_arr = [s.calc_conn(x) for x in s.get_adj(s.get_head())]
        try:
            success = s.DLS(s.get_head(), path, np.zeros(s.board.shape),lim=s.data['you']['health'],thresh=np.max(conn_arr))
        except ValueError:
            pass
        if not success:
            success = s.DLS(s.get_head(), path, np.zeros(s.board.shape),lim=s.data['you']['health'],thresh=0)
        
    
        
    print(path)

    if success:
        d = s.get_dir(path[0], path[1])
        print(get_direction(d))
        return move_response(get_direction(d))
        
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    while not s.can_move(s.add_points(s.get_head(), s.DIRS_KEY[direction]),):
        direction = random.choice(directions)
    
    print(data)
    

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
