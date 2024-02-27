from queue import Queue
from state import *
#breath first search algorithm
def BFS(start_state, goal_state):
    #keeps track of all nodes
    all_nodes = 0
    #make start a node
    start = State(start_state)
    #if the start is the goal just return that
    if start.test_goal(goal_state):
        return start.create_ans(start.solution(),start.cost,all_nodes, start.depth, start.mDepth())
    #create a queue and a set
    queue = Queue()
    visited = set()
    #first node goes in queue
    queue.put(start)
    #while queue is not empty
    while(queue.empty() == False):
        #get the node 
        current_state = queue.get()
        #add the puzzle list in its original form into the visited list
        visited.add(tuple(current_state.state))
        #check if this is the goal
        if current_state.test_goal(goal_state):
            #return the answer
            return current_state.create_ans(current_state.solution(),current_state.cost,all_nodes, current_state.depth, current_state.mDepth())
        #get all the children for each node
        current_state.get_children()
        #increment the all nodes expanded
        all_nodes+=1
        #for each child
        for child in current_state.children:
            #check if its in visited array
            if(tuple(child.state) not in visited):
                #put the child and the child state into visited and queue
                queue.put(child)
                visited.add(tuple(child.state))
    #if no answer is found, return something
    return start.create_ans(0,0,all_nodes, 0, start.mDepth())