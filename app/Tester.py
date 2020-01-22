from Snake import snake
from Node import node
import numpy as np

#used primarily as a tester
if __name__ == "__main__":
    print("hello")

    data_test = {
        'game': {
            'id': 'f46577ff-1189-4ed3-ad26-234e47ae380d'
        }, 
        'turn': 242, 
        'board': {
            'height': 15, 
            'width': 15, 
            'food': [
                {'x': 1, 'y': 7}, 
                {'x': 4, 'y': 14}, 
                {'x': 14, 'y': 12}, 
                {'x': 0, 'y': 5}, 
                {'x': 4, 'y': 8}, 
                {'x': 2, 'y': 11}, 
                {'x': 10, 'y': 10}, 
                {'x': 14, 'y': 11}, 
                {'x': 6, 'y': 1}, 
                {'x': 9, 'y': 2}
            ], 
            'snakes': [
                {
                    'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ef', 
                    'name': 'snake', 
                    'health': 50, 
                    'body': [
                        {'x': 7, 'y': 12},
                        {'x': 7, 'y': 11},
                        {'x': 6, 'y': 11},
                        {'x': 5, 'y': 11},
                        {'x': 5, 'y': 12},
                        {'x': 4, 'y': 12}
                        
                    ]
                },

                {
                    'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ee', 
                    'name': 'snake', 
                    'health': 99, 
                    'body': [
                        {'x': 14, 'y': 1}, 
                        {'x': 14, 'y': 2}, 
                        {'x': 14, 'y': 3}, 
                        {'x': 13, 'y': 3}, 
                        {'x': 13, 'y': 2}, 
                        {'x': 13, 'y': 1}, 
                        {'x': 12, 'y': 1}
                    ]
                },


                {
                    'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ea', 
                    'name': 'snake', 
                    'health': 58, 
                    'body': [
                        {'x': 6, 'y': 13},
                        {'x': 7, 'y': 13},
                        {'x': 8, 'y': 13}
                    ]
                }
            ]
        }, 
        'you': {
            'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ef', 
            'name': 'snake', 
            'health': 50, 
            'body': [
                {'x': 7, 'y': 12},
                {'x': 7, 'y': 11},
                {'x': 6, 'y': 11},
                {'x': 5, 'y': 11},
                {'x': 5, 'y': 12},
                {'x': 4, 'y': 12}
            ]
        }
    }

    ts = snake(data_test)
    print(ts.board)

    #test get adj
    print(ts.get_adj((14,0)))
    print(ts.get_adj((0,0)))
    print()


    #testing set union
    pt = (1,1)
    pt_1 = (2,2)
    pt_set = [(1,1), (1,2), (3,3)]
    ts.pt_union(pt_set,pt,1)
    print(pt_set)
    ts.pt_union(pt_set,pt_1,1)
    print(pt_set)

    print()
    print(ts.calc_conn_ratio((14,0)))
    print(ts.calc_conn_ratio((0,0)))

    print()
    test_arr = [3,2,6,1,7,8,6]
    print(ts.sort(test_arr, lambda e_1, e_2: e_1 > e_2))

    print()
    test_arr_2 = [(0,0),(13,0),(0,1)]
    print(ts.sort(test_arr_2, lambda e_1, e_2: ts.calc_conn_ratio(e_1)>ts.calc_conn_ratio(e_2)))

    print()
    print("testing dls")
    path = []
    dls_root = node((0,0))
    goal_n = ts.LS(-1,[dls_root],np.zeros(ts.board.shape),np.zeros(ts.board.shape))
    path = goal_n.traceback()
    print(path)
    print(goal_n.depth)
    print(ts.get_dir(path[0], path[1]))

    print(ts.beside_head((0,14)))
    print(ts.beside_head((0,13)))

    print()

    print(ts.can_move((0,14)))
    print(ts.can_move((0,14),panic=True))
    path = ts.LS(-1,[node((0,0))],np.zeros(ts.board.shape),np.zeros(ts.board.shape),panic=True).traceback()
    print(path)

    print()

    print("testing get adj panic mode")
    print(ts.get_adj((0,13)))
    print(ts.get_adj((0,13),panic=True))

    print()

    print("testing tree building")
    root = node((0,0))
    n1 = node((1,0))
    n2 = node((2,0))
    root.attach(n1)
    print(n1.parent)
    print(n1.children)
    n1.attach(n2)
    print(root)
    print(n2.traceback())


    print()

    print("testing BLS")
    test_root = node((0,0))
    goal_n = ts.LS(0,[test_root],np.zeros(ts.board.shape),np.zeros(ts.board.shape))
    print(goal_n.traceback())
    print(goal_n.depth)

    print()
    print("testing get snake")
    print(ts.get_snake((1,14),0))

    print()
    print("testing can eat")
    print(ts.can_eat((1,14)))

    print()
    print("testing can_move_tail")
    print(ts.can_move_tail((1,12)))


    print()
    print("testing modified canmove")
    print(ts.can_move((14,0)))

    print()
    print("testing new bug")
    print(ts.can_move((12,6)))
    print(ts.can_move((13,6)))
    print(ts.compare_conn((12,6),(12,5)))

