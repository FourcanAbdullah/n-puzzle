from test.state_old import *
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
            print(Pqueue.queue)
            if(child not in visited and child not in Pqueue.queue):
                val = child.h
                Pqueue.put((child.h,child))
            elif(child in Pqueue.queue):
                
                Pqueue.put((child.h,child))
                
    return "not found"