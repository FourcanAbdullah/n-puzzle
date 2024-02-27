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
        #012    125
        #345    340
        #678    678
        goal_state_matrix = [0,1,2,3,4,5,6,7,8] 
        for i in range(1,len(goal_state_matrix)):
            index = self.find(self.state, goal_state_matrix[i])
            distance = abs(i-index)
            temp = temp + distance
        #print(temp)
        return temp
    def print_state(self):
        print("current state", self.state, self.depth, State.maxDepth)




def BFS(start_state, goal_state):
    all_nodes = 0
    start = State(start_state)
    if start.test_goal(goal_state):
        return start
    queue = Queue()
    visited = set()
    temp = []
    queue.put(start)
    while(queue.empty() == False):
        current_state = queue.get()
        visited.add(tuple(current_state.state))
        #print(all_nodes)
        #current_state.print_state()
        if current_state.test_goal(goal_state):
            print(all_nodes)
            print(current_state.mDepth())
            print(current_state.depth)
            return current_state.solution()
            #temp.append([all_nodes,current_state.mDepth(),current_state.cost,current_state.depth, current_state.solution()])
        current_state.get_children()
        all_nodes+=1
        for child in current_state.children:
            if(tuple(child.state) not in visited):
                queue.put(child)
                visited.add(tuple(child.state))
    
    return temp

#3,1,2
#0,4,5
#6,7,8

from queue import LifoQueue

def DFS(start_state, goal_state):
    allnodes = 0
    temp = []
    start = State(start_state)
    if start_state == goal_state:
        return start
    stack = LifoQueue()
    visited = set()
    stack.put(start)
    while(stack.empty() == False):
        current_state = stack.get()
        visited.add(tuple(current_state.state))
        if current_state.test_goal(goal_state) :
            print(allnodes)
            print(current_state.mDepth())
            print(current_state.depth)
            print(current_state.cost)
            #print(start.tree_height())
            #print(current_state.solution())
            return current_state.solution()
            #temp.append([allnodes,current_state.mDepth(),current_state.cost,current_state.depth, current_state.solution()])

        current_state.get_children()
        allnodes+=1
        for child in list(reversed(current_state.children)):
            if(tuple(child.state) not in visited):
                stack.put(child)
                visited.add(tuple(child.state))
    
            
    
    return temp


from queue import PriorityQueue
def manhatten1(start):
    temp = 0
    #012    125
    #345    340
    #678    678
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
    Pqueue.put((start.h, start))
    while(Pqueue.empty() == False):
        current = Pqueue.get()
        current_h =current[0]
        current_state = current[1]
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
            if(tuple(child.state) not in visited ):# and child not in Pqueue.queue
                val = child.h
                Pqueue.put((child.h,child))
                #visited.add(tuple(child.state))
            # elif(child in Pqueue.queue):
                
            #     Pqueue.put((child.h,child))
                
    return "not found"