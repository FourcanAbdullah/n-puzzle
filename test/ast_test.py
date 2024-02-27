#from state import *
from queue import Queue

class State:
    #global maxDepth
    maxDepth = 0
    def __init__(self, state, parent=None, children=[], position=-1, movement="", depth = 0, cost = 0, h = 0):
        self.state = state
        self.movement = movement
        self.parent = parent
        self.children = children
        self.depth = depth
        self.cost = cost
        self.h = cost + self.manhatten()
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

    #123
    #456
    #780
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
                
                self.children.append(State(newState,self,[],newPos,i, self.depth+1, self.cost+1, (self.cost+1)+(self.manhatten())))
                #print(newState, self.depth+1)
                State.maxDepth = max(State.maxDepth, self.depth+1)
    def tree_height(self):
        if self is None:
            return 0
        
        # Using a queue to perform level-order traversal
        queue = Queue()
        queue.put((self, 1))  # (node, level)
        max_level = 0

        while queue:
            node, level = queue.get()
            
            max_level = max(max_level, level)
            print(max_level)
            for child in node.children:
                queue.put((child, level + 1))

        return max_level
                
    def __lt__(self, other):
        return self.h < other.h
    # def __gt__(self, other):
    #     return self.h > other.h

    # def __eq__(self, other):
    #     return self.h == other.h
    
    def mDepth(self):
        return State.maxDepth   
    def manhatten(self):
        temp = 0
        # 012    125
        # 345    340
        # 678    678
        goal_state_matrix = [0,1,2,3,4,5,6,7,8] 
        for i in range(1,len(goal_state_matrix)):
            index = self.find(self.state, goal_state_matrix[i])
            distance = abs(i-index)
            temp = temp + distance/3 +distance%3

        #print(temp)
        return temp
    def print_state(self):
        print("current state", self.state, self.depth, State.maxDepth)






from queue import PriorityQueue
def manhatten1(start):
    temp = 0
    goal_state_matrix = [0,1,2,3,4,5,6,7,8] 
    for i in range(1,len(goal_state_matrix)):
        index = start.find(start.state, goal_state_matrix[i])
        distance = abs(i-index)
        temp = temp + distance
    return temp

def set_h_val(child):
        #f = g + h
    child.h = child.cost + manhatten1(child)
    

def AST(start_state, goal_state):
    start = State(start_state)
    allnodes = 0
    if start.test_goal(goal_state):
        return "solution"
    Pqueue = PriorityQueue()
    visited = set()
    Pqueue.put((start.h,start.state, start))
    while(Pqueue.empty() == False):
        current = Pqueue.get()
        current_ =current[1]
        current_state = current[2]
        #print(current_state.state)
        visited.add(tuple(current_state.state))
        if current_state.test_goal(goal_state):
            print(allnodes)
            print(current_state.mDepth())
            print(current_state.depth)
            print(current_state.cost)
            print(current_state.h)
            print(current_state.manhatten())
            return current_state.solution()

        current_state.get_children()
        allnodes+=1
        for child in current_state.children:
            #print(Pqueue.queue)
            # temparr = []
            # temparr3 = []
            # for i in Pqueue.queue:
            #     temparr.append(i[1])  # and child not in temparr
            if(tuple(child.state) not in visited):# and child not in Pqueue.queue
                Pqueue.put((child.h,child.state,child))

            # elif(child.state in temparr):
            #     decrease(temparr, Pqueue, child)
            #     #print(Pqueue.queue[1])
                
                
                
    return "not found"


def decrease(arr,queue, child):
    for i in range(len(arr)):
        if(child.state ==queue.queue[i][1]):
            h,puzzle,state = queue.queue[i][0],queue.queue[i][1],queue.queue[i][2]
           # print("found if ", h,puzzle )
    if(child.state == puzzle):
        state.h = child.h
        h = child.h
    #print("new h: ", h, state.h)
    tempQ = PriorityQueue()
    #print("before While")
    while(queue):
        val = queue.get()
        
        if(val[1] == child.state):
            tempQ.put((h,puzzle,state))
            #print("first loop1",tempQ.queue)
        else:
            tempQ.put(val)
        #     print("first loop",tempQ.queue)
        # print(1)
        if(queue.empty() == True):
            break
            
    #print("our 1st while")
    
    while(tempQ):
        val = tempQ.get()
        queue.put(val)
        #print(queue.queue)
        if(tempQ.empty() == True):
            break
    #print("out second while")

    