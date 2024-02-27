

class State:
    def __init__(self, state, parent=None, children=[], position=-1, movement="", cost=0, depth=0, all_nodes =0, total_depth = 0):
        self.state = state
        self.movement = movement
        self.depth = depth
        self.cost = cost
        self.all_nodes = all_nodes
        self.total_depth = total_depth
        self.parent = parent
        self.children = children
        if(position ==-1):
            self.position = self.find(state,0)
        else:
            self.position = position
        
    def find(self, state, zero_val):
        return state.index(zero_val)
    
    
    def switchVals(self, state, positionOriginal, positionNew):
        temp = state[positionOriginal]
        state[positionOriginal] = state[positionNew]
        state[positionNew] = temp
        return state
        
    # [123
    #  456 
    #  789]
    def get_movements(self, state):
        movements = ["Up", "Down", "Left", "Right"]
        pos = self.find(state, 0)
        if(pos < 3):
            movements.remove("Up")
        if(pos >5):
            movements.remove("Down")
        if(pos == 0 or pos == 3 or pos == 6):
            movements.remove("Left")
        if(pos == 2 or pos == 5 or pos == 8):
            movements.remove("Right")
        
        return movements

    def test_goal(self, goal_state):
        if(self.state == goal_state):
            return True
        else:
            return False
    def solution(self):
            solution = []
            solution.append(self.movement)
            path = self
            while path.parent != None:
                path = path.parent
                solution.append(path.movement)
            solution = solution[:-1]
            solution.reverse()
            return solution
            
    def get_children(self):
        movements = self.get_movements(self.state)
        pos = self.position
        arr = []
        if(len(self.children) == 0):
            for i in movements:
                copy = self.state.copy()
                if( i == "Up"):
                    newState = self.switchVals(copy, pos,pos-3)
                    newPos = pos-3
                    
                elif( i == "Down"):
                    newState = self.switchVals(copy, pos,pos+3)
                    newPos = pos+3

                elif( i == "Left"):
                    newState = self.switchVals(copy, pos,pos-1)
                    newPos = pos-1

                elif( i == "Right"):
                    newState = self.switchVals(copy, pos,pos+1)
                    newPos = pos+1
                arr.append([newState, newPos,i])
            
            self.total_depth = max(self.depth+1, self.total_depth)
            for i in arr:
                self.children.append(State(i[0],self,[],i[1],i[2],self.cost+1,self.depth+1,self.all_nodes + len(arr), self.total_depth))
            
    
    def print_state(self):
        # print("current state", self.depth, total_depth1)
        #print("current state", self.depth, self.total_depth, self.all_nodes)
        print("current state", self.state, self.depth, self.all_nodes, self.total_depth)
        
    def calc_total_depth(self):
        self.total_depth = max((self.depth, self.total_depth ))               
        
        
                
            

# class State:
    
#     def __init__(self, state, parent=None, children=[], position=-1, movement=""):
#         self.state = state
#         self.movement = movement
#         self.parent = parent
#         self.children = children
#         if(position ==-1):
#             self.position = self.find(state,0)
#         else:
#             self.position = position
        
#     def find(self, state, zero_val):
#         return state.index(zero_val)
    
#     def switchVals(self, state, positionOriginal, positionNew):
#         temp = state[positionOriginal]
#         state[positionOriginal] = state[positionNew]
#         state[positionNew] = temp
#         return state

#     #123
#     #456
#     #780
#     def get_movements(self, state):
#         movements = ["Up", "Down", "Left", "Right"]
#         pos = self.find(state, 0)
#         if(pos < 3):
#             movements.remove("Up")
#         if(pos >5):
#             movements.remove("Down")
#         if(pos == 0 or pos == 3 or pos == 6):
#             movements.remove("Left")
#         if(pos == 2 or pos == 5 or pos == 8):
#             movements.remove("Right")
        
#         return movements

#     def test_goal(self, goal_state):
#         if(self.state == goal_state):
#             return True
#         else:
#             return False
#     def solution(self):
#             solution = []
#             solution.append(self.movement)
#             path = self
#             while path.parent != None:
#                 path = path.parent
#                 solution.append(path.movement)
#             solution = solution[:-1]
#             solution.reverse()
#             return solution
            
#     def get_children(self):
#         movements = self.get_movements(self.state)
#         pos = self.position
        
#         if(len(self.children) == 0):
#             for i in movements:
#                 copy = self.state.copy()
#                 if( i == "Up"):
#                     newState = self.switchVals(copy, pos,pos-3)
#                     newPos = pos-3
            
                    
#                 if( i == "Down"):
#                     newState = self.switchVals(copy, pos,pos+3)
#                     newPos = pos+3
                    
#                 if( i == "Left"):
#                     newState = self.switchVals(copy, pos,pos-1)
#                     newPos = pos-1
                    
#                 if( i == "Right"):
#                     newState = self.switchVals(copy, pos,pos+1)
#                     newPos = pos+1

                
#                 self.children.append(State(newState,self,[],newPos,i))
#                 #print("current state", self.state)
        
    # def print_state(self):
    #     print("current state", self.state)