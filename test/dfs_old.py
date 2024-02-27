from test.state_old import *
from queue import LifoQueue

def DFS(start_state, goal_state):
    start = State(start_state)
    if start_state == goal_state:
        return "solution"
    stack = LifoQueue()
    visited = set()
    stack.put(start)
    while(stack.empty() == False):
        current_state = stack.get()
        visited.add(tuple(current_state.state))
        current_state.print_state()
        if current_state.test_goal(goal_state):
            return current_state.solution()

        current_state.get_children()
        for child in list(reversed(current_state.children)):
            if(tuple(child.state) not in visited):
                stack.put(child)
                
    return "not found"
    