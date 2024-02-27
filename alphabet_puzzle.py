from itertools import permutations

def solver(puzzle):
    #putting all the letters into a array
    arr = []
    for i in puzzle:
        for j in i:
            if j.isalpha() and j not in arr:
                arr.append(j)
    #this array holds the answers      
    tempg = []
    #a map to store letters and thier possible number values
    letter_map = {}
    #all the possible permutations
    allcombinations = permutations(range(10), len(arr))
    #for each combination
    for combination in allcombinations:
        #create a copy of the puzzle
        copy = []
        copy = puzzle.copy()
        #add the map values, set the values to the possible permutation answer
        for i in range(len(arr)):
            letter_map[arr[i]] = str(combination[i])
        #if any of the first letter values are zero, just continue
        if(letter_map[copy[0][0]] == '0' or letter_map[copy[1][0]] == '0' or letter_map[copy[1][0]] == '0'):
            continue
        #for each word replace thier string values and make them into numbers
        for i in range(len(copy)):
            for test in letter_map.keys():
                copy[i] = copy[i].replace(test, letter_map[test])
            #make them to int
            copy[i] = int(copy[i])
        #check if combination is correct then add it to the answer array
        if(copy[0] + copy[1] == copy[2]):
            mapi = letter_map.copy()
            tempg.append([copy[0], copy[1],copy[2],mapi])
    #return the answer array
    return tempg

if __name__ == "__main__":
    
    val1 =  input("Enter value 1: ")
    val2 =  input("Enter value 2: ")
    val3 =  input("Enter Total: ")
    puzzle = [val1, val2, val3]
    solution = solver(puzzle)
    if solution:
        print("Solution found:")
        for i in solution:
            print("Solution: " + str(i[0]) + " + "+ str(i[1]) + " = " + str(i[2]) + " | "+ str(i[3]))
        #print(solution)
    else:
        print("No solution found")






# import itertools

# def solve_cryptarithmetic(puzzle):
#     # Extracting unique letters from the puzzle
#     letters = set([char for char in puzzle if char.isalpha()])

#     # Generate all possible permutations of digits from 0 to 9 for the unique letters
#     for permutation in itertools.permutations(range(10), len(letters)):
#         digit_map = {letter: digit for letter, digit in zip(letters, permutation)}
#         # Replacing letters with corresponding digits in the puzzle
#         try:
#             equation = puzzle.translate(str.maketrans(digit_map))
#             # Checking if the equation holds true
#             if eval(equation):
#                 return digit_map
#         except Exception as e:
#             print("Error:", e)

#     return None

# # Example usage:
# if __name__ == "__main__":
#     puzzle = "SEND + MORE == MONEY"
#     solution = solve_cryptarithmetic(puzzle)
#     if solution:
#         print("Solution found:")
#         for letter, digit in solution.items():
#             print(f"{letter} = {digit}")
#     else:
#         print("No solution found")
