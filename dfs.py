from queue import LifoQueue
from state import *
#DFS algorithm
def DFS(start_state, goal_state):
    #keeps track of all nodes
    allnodes = 0
    #make start a node
    start = State(start_state)
    #if the start is the goal just return that
    if start_state == goal_state:
        return start.create_ans(start.solution(),start.cost,allnodes, start.depth, start.mDepth())
    #create a stack and a set
    stack = LifoQueue()
    visited = set()
    #first node goes in stack
    stack.put(start)
    #while stack is not empty
    while(stack.empty() == False):
        #get the node 
        current_state = stack.get()
        #add the puzzle list in its original form into the visited list
        visited.add(tuple(current_state.state))
        #check if this is the goal
        if current_state.test_goal(goal_state) :
            #return the answer
            return current_state.create_ans(current_state.solution(),current_state.cost,allnodes, current_state.depth, current_state.mDepth())
        #get all the children for each node
        current_state.get_children()
        #increment the all nodes expanded
        allnodes+=1
        #for each child
        for child in list(reversed(current_state.children)):
            #check if its in visited array
            if(tuple(child.state) not in visited):
                #put the child and the child state into visited and stack
                stack.put(child)
                visited.add(tuple(child.state))
     #if no answer is found, return something
    return start.create_ans(0,0,allnodes, 0, start.mDepth())