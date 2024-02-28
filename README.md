# n-puzzle

To run this program have all the files in one folder and run "python driver.py <choice of algorithm> <9 digits for the start state>

choice of algorithm can be:
ast: a\* algorithm, using manhatten distance
bfs: breath first search
dfs depth first search

9 digits should be in the form:
6,1,8,4,0,2,7,3,5

example format: python driver.py ast 6,1,8,4,0,2,7,3,5

This outputs a output.txt with information on the path, cost, nodes expanded, depth, total depth, ram usage, and time
I was able to complete, BFS, DFS, and A\*
