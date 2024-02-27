from queue import PriorityQueue
from state import *
#a* algorithm
def AST(start_state, goal_state):
    #make start a node
    start = State(start_state)
    #keeps track of all nodes
    allnodes = 0
    #if the start is the goal just return that
    if start.test_goal(goal_state):
        return start.create_ans(start.solution(),start.cost,allnodes, start.depth, start.mDepth())
    #create a priority queue and a set
    Pqueue = PriorityQueue()
    visited = set()
    #first node goes in queue
    Pqueue.put((start.h,start.state, start))
    #while queue is not empty
    while(Pqueue.empty() == False):
        #get the node
        current = Pqueue.get()
        current_state = current[2]
        #add the puzzle list in its original form into the visited list
        visited.add(tuple(current_state.state))
        #check if this is the goal
        if current_state.test_goal(goal_state):
            return current_state.create_ans(current_state.solution(),current_state.cost,allnodes, current_state.depth, current_state.mDepth())
        #get all the children for each node
        current_state.get_children()
        #increment the all nodes expanded
        allnodes+=1
        #for each child
        for child in current_state.children:
            #check if its in visited array
            if(tuple(child.state) not in visited):
                #put the child and the child state into visited and stack
                Pqueue.put((child.h,child.state,child))
    #if no answer is found, return something            
    return start.create_ans(0,0,allnodes, 0, start.mDepth())