from Snake import snake
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
                    'health': 100, 
                    'body': [
                        {'x': 1, 'y': 14}, 
                        {'x': 2, 'y': 14}, 
                        {'x': 3, 'y': 14}, 
                        {'x': 3, 'y': 13}, 
                        {'x': 2, 'y': 13}, 
                        {'x': 1, 'y': 13}, 
                        {'x': 1, 'y': 12}, 
                        {'x': 0, 'y': 12}, 
                        {'x': 0, 'y': 11}, 
                        {'x': 0, 'y': 10}, 
                        {'x': 1, 'y': 10}, 
                        {'x': 1, 'y': 10}
                    ]
                },

                {
                    'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ee', 
                    'name': 'snake', 
                    'health': 100, 
                    'body': [
                        {'x': 14, 'y': 1}, 
                        {'x': 14, 'y': 2}, 
                        {'x': 14, 'y': 3}, 
                        {'x': 13, 'y': 3}, 
                        {'x': 13, 'y': 2}, 
                        {'x': 13, 'y': 1}, 
                        {'x': 12, 'y': 1}
                    ]
                }
            ]
        }, 
        'you': {
            'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ef', 
            'name': 'snake', 
            'health': 100, 
            'body': [
                {'x': 1, 'y': 14}, 
                {'x': 2, 'y': 14}, 
                {'x': 3, 'y': 14}, 
                {'x': 3, 'y': 13}, 
                {'x': 2, 'y': 13}, 
                {'x': 1, 'y': 13}, 
                {'x': 1, 'y': 12}, 
                {'x': 0, 'y': 12}, 
                {'x': 0, 'y': 11}, 
                {'x': 0, 'y': 10}, 
                {'x': 1, 'y': 10}, 
                {'x': 1, 'y': 10}
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
    print(ts.calc_conn((14,0)))
    print(ts.calc_conn((0,0)))

    print()
    test_arr = [3,2,6,1,7,8,6]
    print(ts.sort(test_arr, lambda e_1, e_2: e_1 > e_2))

    print()
    test_arr_2 = [(0,0),(13,0),(0,1)]
    print(ts.sort(test_arr_2, lambda e_1, e_2: ts.calc_conn(e_1)>ts.calc_conn(e_2)))

    print()
    path = []
    ts.DLS((0,0),path,np.zeros(ts.board.shape))
    print(path)
    print(ts.get_dir(path[0], path[1]))

    print(ts.beside_head((0,14)))
    print(ts.beside_head((0,13)))

    print()

    print(ts.can_move((0,14)))
    print(ts.can_move((0,14),panic=True))
    path = []
    ts.DLS((0,14),path,np.zeros(ts.board.shape),panic=True)
    print(path)

    print()

    print("testing get adj panic mode")
    print(ts.get_adj((0,13)))
    print(ts.get_adj((0,13),panic=True))

