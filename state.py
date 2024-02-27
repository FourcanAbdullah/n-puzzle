from queue import Queue
#holds the state class
class State:
    #this is the maximum depth of the graph
    maxDepth = 0
    def __init__(self, state, parent=None, children=[], position=-1, movement="", depth = 0, cost = 0, h = 0):
        #holds the puzzle state
        self.state = state
        #holds which movement it took
        self.movement = movement
        #connects to parent
        self.parent = parent
        #connects to children
        self.children = children
        #holds this nodes depth
        self.depth = depth
        #holds the cost
        self.cost = cost
        #hold the heuristic value
        self.h = cost + self.manhatten()
        #if there is no position
        if(position ==-1):
            #find the zero val
            self.position = self.find(state,0)
        else:
            #otherwise set the position
            self.position = position
    #finds the given value in the state    
    def find(self, state, zero_val):
        return state.index(zero_val)
    #switchs the tiles based on position values
    def switchVals(self, state, positionOriginal, positionNew):
        #stores original val
        temp = state[positionOriginal]
        #moves new val to it
        state[positionOriginal] = state[positionNew]
        #replaces the new val
        state[positionNew] = temp
        #return the state
        return state
    #organizes the movements
    def get_movements(self, state):
        #order of priority for movements
        movements = ["Up", "Down", "Left", "Right"]
        #finds the location of zero
        pos = self.find(state, 0)
        #if the 0 is in the top row remove the up option
        if(pos < 3):
            movements.remove("Up")
        #if the 0 is in the bottom row remove the down option
        if(pos >5):
            movements.remove("Down")
        #if the 0 is in the leftmost row remove the left option
        if(pos == 0 or pos == 3 or pos == 6):
            movements.remove("Left")
        #if the 0 is in the rightmost row remove the right option
        if(pos == 2 or pos == 5 or pos == 8):
            movements.remove("Right")
        #return movements
        return movements
    #checks if the current node is the goal node
    def test_goal(self, goal_state):
        #if its the goal return true
        if(self.state == goal_state):
            return True
        else:
            return False
    #returns the solution path
    def solution(self):
            #stores movements
            movements = []
            #stores first movement
            movements.append(self.movement)
            #sets the mode to self
            node = self
            while node.parent:
                #sets the current node to parrent
                node = node.parent
                #append the node movment
                movements.append(node.movement)
            #reverse the list
            movements.reverse()
            #return the list with the removed empty val
            return movements[1:]

    #creates and make sthe children
    def get_children(self):
        #get the movements
        movements = self.get_movements(self.state)
        #find the 0 position of the current node
        pos = self.position
        #if there is no children
        if(len(self.children) == 0):
            #for each possible movment
            for i in movements:
                #create a copy of the state
                copy = self.state.copy()
                #if i is equal to the movment then swith the values in raltion to it and get the new positon
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
                #append the child with all the values into the current node
                self.children.append(State(newState,self,[],newPos,i, self.depth+1, self.cost+1, (self.cost+1)+(self.manhatten())))
                #kepp track of the maximum depth
                State.maxDepth = max(State.maxDepth, self.depth+1)
    #compares the h values <            
    def __lt__(self, other):
        return self.h < other.h
    #returns the max depth
    def mDepth(self):
        return State.maxDepth   
    #manhatten distance for heurestic val
    def manhatten(self):
        #holds the ans
        temp = 0
        #given goal state
        goal_state_matrix = [0,1,2,3,4,5,6,7,8] 
        #for values from 1 to 9
        for i in range(1,len(goal_state_matrix)):
            #finds the index of the i value
            index = self.find(self.state, goal_state_matrix[i])
            #finds the distance and the vals to add to the heuristic
            distance = abs(i-index)
            temp = temp + distance/3 +distance%3
        return temp
    #prints the state
    def print_state(self):
        print("current state", self.state, self.depth, State.maxDepth)
    #creates the answer format
    def create_ans(self, path, cost, nodes_expanded, search_depth, max_depth):
        ans_array = []
        ans_array.append("path_to_goal: "+str(path))
        ans_array.append("cost_of_path: " +str(cost))
        ans_array.append("nodes_expanded: " + str(nodes_expanded))
        ans_array.append("search_depth: "+str(search_depth))
        ans_array.append("max_search_depth: "+ str(max_depth))
        return ans_array
        