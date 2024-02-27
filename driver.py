import sys
from dfs import *
from bfs import *
from state import *
from astar import *
import time
import sys


def main():
    
    
    if len(sys.argv) < 3:
        print("Usage: python main.py <algorithm> <start state>")
        return
    
    #takes in all the arguments
    algorithm = sys.argv[1]
    start_state = sys.argv[2]
    #starts the time
    start_time = time.time()
    #gets all the values from the arguements
    new_string_state = start_state.split(",")
    new_state =  [int(i) for i in new_string_state]
    #pre given goal state
    goal_state_matrix = [0,1,2,3,4,5,6,7,8] 
    #if bfs was chosen run BFS algorithm
    if( algorithm == 'bfs'):
        ans = BFS(start_state=new_state,goal_state=goal_state_matrix)
    #if dfs was chosen run DFS algorithm
    elif( algorithm == 'dfs'):
        ans = DFS(start_state=new_state,goal_state=goal_state_matrix)
   #if a* was chosen run a* algorithm
    elif( algorithm == 'ast'):
        ans = AST(start_state=new_state,goal_state=goal_state_matrix)
    #ends the time
    end_time = time.time()
    #finds the time difference
    total_time = end_time - start_time
    #adds it to anser
    ans.append("running_time: "+ str(round(total_time,6)))
    #for ram
    if sys.platform == "win32":
        import psutil
        ramu = psutil.Process().memory_info().rss
        ans.append("max_ram_usage: " + str(round(ramu,6)))
    else:
        import resource
        ramu = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        ans.append("max_ram_usage: " + str(rount(ramu,6)))
    #for putting into file
    file_name = "output.txt"
    with open(file_name, 'w') as output:
        for line in ans:
            output.write(line)
            output.write('\n')
        
    

if __name__ == "__main__":
    main()