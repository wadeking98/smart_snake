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
                        {'x': 8, 'y': 1},
                        {'x': 7, 'y': 1}
                        
                    ]
                },

                {
                    'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ee', 
                    'name': 'snake', 
                    'health': 99, 
                    'body': [
                        {'x': 10, 'y': 1},
                        {'x': 11, 'y': 1}, 
                        {'x': 12, 'y': 1}
                    ]
                },


                {
                    'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ea', 
                    'name': 'snake', 
                    'health': 58, 
                    'body': [
                        {'x': 5, 'y': 13},
                        {'x': 6, 'y': 13},
                        {'x': 7, 'y': 13}
                    ]
                }
            ]
        }, 
        'you': {
            'id': 'f8c6a952-b287-4671-9b19-1f9cbb5c74ef', 
            'name': 'snake', 
            'health': 50, 
            'body': [
                {'x': 8, 'y': 1},
                {'x': 7, 'y': 1}
            ]
        }
    }

    # data_test = {
    #     'game': {
    #         'id': 'dff4f2ed-db77-4ac4-8eb0-d0073c43bc7a'
    #     }, 
    #     'turn': 1, 
    #     'board': {
    #         'height': 11, 
    #         'width': 11, 
    #         'food': [
    #             {'x': 8, 'y': 6}, 
    #             {'x': 0, 'y': 3}, 
    #             {'x': 5, 'y': 3}, 
    #             {'x': 5, 'y': 6}, 
    #             {'x': 10, 'y': 7}, 
    #             {'x': 6, 'y': 9}, 
    #             {'x': 1, 'y': 6}, 
    #             {'x': 8, 'y': 3}], 
    #             'snakes': [
    #                 {
    #                     'id': 'gs_PdM8dDyCM9HyDWjBPwH3mXHR', 
    #                     'name': 'sean-clarke / go-snake-go-gce', 
    #                     'health': 99, 
    #                     'body': [
    #                         {'x': 1, 'y': 0}, 
    #                         {'x': 1, 'y': 1}, 
    #                         {'x': 1, 'y': 1}
    #                     ]
    #                 }, 
    #                 {
    #                     'id': 'gs_mJjJHBQYwM7KRQqGTyvrCQWW', 
    #                     'name': 'spechtator / Mr. Noodle2', 
    #                     'health': 99, 
    #                     'body': [{'x': 9, 'y': 0}, {'x': 9, 'y': 1}, {'x': 9, 'y': 1}]
    #                 }, 
    #                 {
    #                     'id': 'gs_7vC3h94CrxW8Whj9BtpRfr9Q', 
    #                     'name': 'petah / Project Z', 
    #                     'health': 99, 
    #                     'body': [{'x': 1, 'y': 8}, {'x': 1, 'y': 9}, {'x': 1, 'y': 9}]
    #                 }, 
    #                 {
    #                     'id': 'gs_pxmqHHVDvMSGjwdWYxcDmYWY', 
    #                     'name': 'rtullybarr / Mamba #5', 
    #                     'health': 99, 
    #                     'body': [{'x': 9, 'y': 8}, {'x': 9, 'y': 9}, {'x': 9, 'y': 9}]
    #                 }, {'id': 'gs_qV4MqbWvM8f93MRkjfrpBCj7', 'name': 'andrewsmith / Decent Snake', 'health': 99, 'body': [{'x': 5, 'y': 8}, {'x': 5, 'y': 9}, {'x': 5, 'y': 9}]}, {'id': 'gs_QpqJFRpxPcyQ8KKRyCrYKCcY', 'name': 'chloeiii / Fine.', 'health': 99, 'body': [{'x': 8, 'y': 5}, {'x': 9, 'y': 5}, {'x': 9, 'y': 5}]}, {'id': 'gs_GtGRHhVXJjP8MfbhSq8hGvQ3', 'name': 'spechtator / Mr. Noodle2', 'health': 99, 'body': [{'x': 1, 'y': 4}, {'x': 1, 'y': 5}, {'x': 1, 'y': 5}]}, {'id': 'gs_W33GKvKRQGcWMxqv6WKxHpBf', 'name': 'wadeking98 / training', 'health': 99, 'body': [{'x': 5, 'y': 2}, {'x': 5, 'y': 1}, {'x': 5, 'y': 1}]}]}, 
    #                 'you': {'id': 'gs_W33GKvKRQGcWMxqv6WKxHpBf', 'name': 'wadeking98 / training', 'health': 99, 'body': [{'x': 5, 'y': 2}, {'x': 5, 'y': 1}, {'x': 5, 'y': 1}]}}

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
    print(ts.calc_conn_ratio((10,0)))
    print(ts.calc_conn_ratio((0,0)))

    print()
    test_arr = [3,2,6,1,7,8,6]
    print(ts.sort(test_arr, lambda e_1, e_2: e_1 > e_2))

    print()
    test_arr_2 = [(0,0),(9,0),(0,1)]
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

    print(ts.beside_head((0,0)))
    print(ts.beside_head((0,0)))

    print()

    print(ts.can_move((0,0)))
    print(ts.can_move((0,0),panic=True))
    path = ts.LS(-1,[node((0,0))],np.zeros(ts.board.shape),np.zeros(ts.board.shape),panic=True).traceback()
    print(path)

    print()

    print("testing get adj panic mode")
    print(ts.get_adj((0,0)))
    print(ts.get_adj((0,0),panic=True))

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
    print(ts.get_snake((1,0),0))

    print()
    print("testing can eat")
    #print(ts.can_eat((1,14)))

    print()
    print("testing can_move_tail")
    print(ts.can_move_tail((1,0)))


    print()
    print("testing modified canmove")
    print(ts.can_move((0,0)))

    print()
    print("testing new bug")
    print(ts.can_move((1,5)))
    print(ts.can_move((0,6)))
    print(ts.compare_conn((0,6),(0,5)))

    print()
    print(ts.board)
    print(ts.board[1][7])
    print(ts.deg((2,7)))

    print()
    print("distance")
    print(ts.get_dist((1,5),(11,11)))

    print()
    print("distance compare")
    print(ts.compare((1,1),(2,8)))
 



