import json
from collections import deque

# Initial state options for the puzzle
init_state_1 = [1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 7, 12, 13, 14, 11, 15]
init_state_2 = [1, 0, 3, 4, 5, 2, 7, 8, 9, 6, 10, 11, 13, 14, 15, 12]
init_state_3 = [0, 2, 3, 4, 1, 5, 7, 8, 9, 6, 11, 12, 13, 10, 14, 15]
init_state_4 = [5, 1, 2, 3, 0, 6, 7, 4, 9, 10, 11, 8, 13, 14, 15, 12]
init_state_5 = [1, 6, 2, 3, 9, 5, 7, 4, 0, 10, 11, 8, 13, 14, 15, 12]
# Final state of the puzzle
final_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

# Finds the possible moves for the blank tile.
def moves(puzzle):
    pos = puzzle.index(0)  # Find where 0 is in the current state of the puzzle

    if pos == 0:  # If the blank tile is in the 0th position of the state array, the tile can make the following moves
        possible_moves = [1, 4]  # If at the 0 position, the blank tile can move either right (+1) or down (+4)
    elif pos == 1:
        possible_moves = [1, 4, -1]  # -1 will move the blank tile to the left in the puzzle
    elif pos == 2:
        possible_moves = [1, 4, -1]
    elif pos == 3:
        possible_moves = [-1, 4]
    elif pos == 4:
        possible_moves = [-4, 1, 4]  # -4 will move the blank tile upward in the puzzle
    elif pos == 5:
        possible_moves = [-4, 4, 1, -1]
    elif pos == 6:
        possible_moves = [-4, 4, 1, -1]
    elif pos == 7:
        possible_moves = [-4, 4, -1]
    elif pos == 8:
        possible_moves = [-4, 1, 4]
    elif pos == 9:
        possible_moves = [-4, 4, 1, -1]
    elif pos == 10:
        possible_moves = [-4, 4, 1, -1]
    elif pos == 11:
        possible_moves = [-4, 4, -1]
    elif pos == 12:
        possible_moves = [-4, 1]
    elif pos == 13:
        possible_moves = [-4, -1, 1]
    elif pos == 14:
        possible_moves = [-4, -1, 1]
    else:
        possible_moves = [-4, -1]

    return possible_moves  # Return the possible moves for the tile


# Moves the blank tile in the puzzle.
def move(puzzle, direction):
    # Creates a copy of the new_puzzle to change it.
    new_puzzle = puzzle.copy()
    pos = puzzle.index(0)
    # Position blank tile will move to.
    new_pos = pos + direction
    # Swap tiles.
    new_puzzle[pos], new_puzzle[new_pos] = new_puzzle[new_pos], new_puzzle[pos]

    return new_puzzle  # Return the new state of the puzzle, so the next available move can be found


# Creates the database.
def solve_puzzle():
    # Initializes a starting state, queue and visited list.
    start = init_state_5
    queue = deque([[start, 0]])
    node_states = []  # Create an array to hold the steps taken from beginning to final state
    repeats = []  # Create an array to hold all the previously visited puzzle states

    # BFS taking into account a state and the cost (number of moves) to reach it from the starting state.
    while queue:
        # Creates a queue with two entries: first is the state and second is # of moves from starting state
        state_cost = queue.popleft()
        state = state_cost[0]
        cost = state_cost[1]  # Cost represents the number of moves from the starting state of the puzzle

        for m in moves(state):
            next_move = move(state, m)

            # Increases cost if blank tile swapped with number tile.
            pos = state.index(0)
            if next_move[pos] > 0:
                next_state_cost = [next_move, cost+1]
            else:
                next_state_cost = [next_move, cost]

            if not "".join(str(t) for t in next_move) in repeats:
                queue.append(next_state_cost)
            # Create an array with a comma between entries so that values such as 0 and 1 can be differentiated from 10
            node_states.append((",".join(str(t) for t in state), cost))
            repeats.append("".join(str(t) for t in state))

        if state == final_state:  # If the final state of the puzzle has been reached, break out of the loop
            break
    print("Entries collected: " + str(len(node_states)))  # Print how many total moves it has taken to reach final state
    print("Writing entries to file...")
    # Writes entries to the text file, sorted by cost
    with open("nodePath.txt", "w") as f:
        for entry in sorted(node_states, key=lambda c: c[1]):
            json.dump(entry, f)
            f.write("\n")


print(solve_puzzle())



