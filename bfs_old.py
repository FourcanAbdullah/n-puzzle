from test.state_old import *
from queue import Queue

def BFS(start_state, goal_state):

    start = State(start_state)
    if start.test_goal(goal_state):
        return "solution"
    queue = Queue()
    visited = set()
    queue.put(start)
    while(queue.empty() == False):
        current_state = queue.get()
        print(len(visited))
        visited.add(tuple(current_state.state))
        current_state.print_state()
        if current_state.test_goal(goal_state):
            return current_state.solution()

        current_state.get_children()
        for child in current_state.children:
            if(tuple(child.state) not in visited):
                #visited.add(tuple(child.state))
                queue.put(child)
        

    
    
    
    return "not found"

#3,1,2
#0,4,5
#6,7,8