import numpy as np
import random
from Node import node


class snake:
    

    def __init__(self, data):
        self.DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
        self.DIRS_KEY = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
        self.data = data
        self.board = self.gen_board()


    def get_snake(self, point, pt_type):
        """
        @param (tuple) point, a point belonging to some snake
        @param (int) pt_type, the type of point specified for the search,
        -1 if tail, 0 if head
        @return (dict) the snake to which the point belongs
        """
        for snake in self.data["board"]["snakes"]:
            if self.pt_eq((snake["body"][pt_type]["y"],snake["body"][pt_type]["x"]),point):
                return snake
        return None

    def can_move_tail(self, point):
        """
        @param (tuple) point, the point in question
        @return (bool) true if the point is a tail and the snake it
        belongs to did not just eat a food
        """
        snake = self.get_snake(point,-1)
        if snake is None:#if not a tail or does not belong to any snake
            return False
        else:
            return snake["health"] < 100

    def can_eat(self, head):
        """
        @param (tuple) head, the head of the snake in question
        @return (bool) true if the enemy snake has less health than our snake
        """
        assert self.board[head[0]][head[1]] == 2
        enemy_len = len(self.get_snake(head, 0)["body"])
        self_len = len(self.data["you"]["body"])
        return self_len > enemy_len

    def beside_head(self,point, offensive=True):
        """
        @param (tuple) point, the point in question
        @param (numpy[][]) board, the game board
        @param (bool) offensive, determines if this snake will try to eat smaller snakes
        @return (bool) true if the point in question is next to an enemy head
        """
        for drc in self.DIRS:
            check = self.add_points(point,drc)
            if self.in_bounds(check) and self.board[check[0]][check[1]] == 2 and (not self.can_eat(check) or not offensive):
                return True
        return False

    def get_head(self):
        """
        @param (string) data, the json data of the state of the game
        @return (tuple) the coordinates of the head
        """
        return (self.data["you"]["body"][0]["y"],self.data["you"]["body"][0]["x"])

    def add_points(self, pt_a, pt_b):
        """
        @param (tuple) pt_a, pt_b
        @return (tuple) element wise sum of pt_a, pt_b
        """
        ret = []
        if len(pt_a) != len(pt_b):
            print(pt_a,pt_b)
            return None
        else:
            for i in range(len(pt_a)):
                ret.append(pt_a[i]+pt_b[i])
        return tuple(ret)

    def in_bounds(self, point):
        """
        @param (tuple) point the point in question
        @param (bool) True if point is on the board
        """
        return point[0] in range(len(self.board)) and point[1] in range(len(self.board[0]))

    def can_move(self, point, panic=False):
        """
        @param (tuple) point, the point in question
        @param (numpy[][]) board, the game board
        @param (bool) panic, allows snake to make more dangerous moves
        @return (bool) true if point is within the bounds of the game board,
        not occupied by a snake, and not beside the head of an enemy snake
        """
        if not self.in_bounds(point) or (not panic and self.beside_head(point)):
            return False
        else:
            return (self.board[point[0]][point[1]] != 1) or self.can_move_tail(point)
    

    def pt_eq(self, pt_a, pt_b):
        """
        @param (tuple) pt_a, pt_b
        @return (bool) true if pt_a == pt_b
        """
        if len(pt_a) != len(pt_b):
            return None

        for i in range(len(pt_a)):
            if pt_a[i] != pt_b[i]:
                return False

        return True


    def contains(self, pt_set, pt):
        """
        @param (list) pt_set, list of points
        @param (tuple) pt
        """
        for elem in pt_set:
            if self.pt_eq(elem,pt):
                return True

    
    def pt_union(self, pt_set, elem, idx):
        """
        adds an point to a set if is not already in the set
        @param (list) set, the set being added to
        @param (tuple) elem, the point being added to the set
        @return (bool) true, if element is not in set
        """
        if not self.contains(pt_set,elem):
            pt_set.insert(idx, elem)


    def get_adj(self,point, panic=False):
        """
        @param (tuple) point, the point in question
        @return (list) the list of available moves
        """
        ret = []
        for dir in self.DIRS:
            adj_pt = self.add_points(dir,point)
            if self.can_move(adj_pt, panic=panic):
                ret.append(adj_pt)
        return ret


    def calc_conn(self, point, lim=15):
        """
        @param (tuple) point, the point in question
        @param (int) lim, max iterations
        @return (int)  number of free tiles is this point connected to
        """
        
        # calculate the total number of free tiles
        explored = np.zeros(self.board.shape)

        

        #initialize queue
        queue = [point]
        explored[point[0]][point[1]] = 1

        total_conn = 0 if self.board[point[0]][point[1]] == 1 else 1
        while len(queue) > 0 and lim > 0:
            curr = queue.pop()
            adjs = self.get_adj(curr)

            #all adjacent tiles that we have not already visited
            adjs_cleaned = [x for x in adjs if not explored[x[0]][x[1]] and not self.beside_head(x,offensive=False)]
            for adj in adjs_cleaned:
                explored[adj[0]][adj[1]] = 1
                total_conn += 1
                self.pt_union(queue,adj,0)
            lim -= 1
        return total_conn
    

    def deg(self, point):
        """
        @param (tuple) point, the point in question
        @return the degree of the tile
        """
        return len(self.get_adj(point))



    def LS(self, search_type, fronteir, explored, lim=100, thresh=20, panic=False):
        """
        finds a path that favours more connected spaces
        @param (int) type, the type of search -1 for DLS, 0 for BLS
        @param (list) fronteir, the list of unexplored nodes to be searched
        @param (numpy[][]) explored, the buffer to hold the explored set
        @param (int) lim, the recursion depth limit 
        @return (node), the goal node
        """
        if lim <= 0 or len(fronteir) == 0:
            return None
        
        curr_node = fronteir.pop()
        curr = curr_node.item
        explored[curr[0]][curr[1]] = 1

        if (self.board[curr[0]][curr[1]] == -1) and self.calc_conn(curr) >= thresh:
            return curr_node
        else:
            #get adj spaces we can move to
            adjs = self.get_adj(curr,panic=panic)
            adjs_cleaned = [x for x in adjs if not explored[x[0]][x[1]]]
            random.shuffle(adjs_cleaned)

            adjs_sorted = self.sort(adjs_cleaned, lambda e_1, e_2: self.calc_conn(e_1) > self.calc_conn(e_2))

            for adj in adjs_cleaned:
                adj_n = node(adj)
                curr_node.attach(adj_n)
                fronteir.insert(search_type,adj_n)
            
            return self.LS(search_type,fronteir, explored, lim=lim-1, thresh=thresh, panic=panic)

    
    def get_dir(self, vec_init, vec_final):
        """
        @param (tuple) vec_init, the initial vector
        @param (tuple) vec_final, the final vector
        @return (tuple) vec_final - vec_init
        """
        subt = []
        if len(vec_init) != len(vec_final):
            return None
        
        for i in range(len(vec_init)):
            e_new = vec_final[i]-vec_init[i]
            subt.append(e_new)
        
        return tuple(subt)


    def sort(self, arr, cmp):
        """
        merge sorts an array using a given comparator
        @param (list) arr, the array to be sorted
        @param (function) cmp, the comparision function for two elements
        @return (list), a list sorted according to the comparitor
        """
        if len(arr) <= 1: #done splitting, can merge now
            return arr.copy()
        
        #split step of the arrays
        split_1 = self.sort(arr[:len(arr)//2], cmp)
        split_2 = self.sort(arr[len(arr)//2:], cmp)

        new_arr = []

        #add all part of split 2 smaller than the largest element in split 1
        i = 0
        j = 0
        while (i < len(split_1)) and (j<len(split_2)):
            if cmp(split_1[i],split_2[j]):
                new_arr.append(split_1[i])
                i += 1
            else:
                new_arr.append(split_2[j])
                j += 1
        
        #add any reamining elements
        while i < len(split_1):
            new_arr.append(split_1[i])
            i += 1

        while j < len(split_2):
            new_arr.append(split_2[j])
            j += 1
                
                
        return new_arr




    def gen_board(self):
        """
        generates the game board based on the json data
        @param (string) data, json data of the state of the game
        @return (numpy[][]) game board
        """
        dims = (self.data["board"]["height"], self.data["board"]["width"])
        new_board = np.zeros(dims)

        #mark the snakes
        snakes = self.data["board"]["snakes"]
        for snake in snakes:
            
            for point in snake["body"]:
                new_board[point["y"]][point["x"]] = 1

            #mark enemy heads
            if self.data["you"]["id"] != snake["id"]:
                head = snake["body"][0]
                new_board[head["y"]][head["x"]] = 2
            
        #mark the food
        foods = self.data["board"]["food"]
        for food in foods:
            new_board[food["y"]][food["x"]] = -1

        return new_board

    


