#!/usr/bin/python3
"""
This module contains a function called `canUnlockAll` that 
determines whether all the boxes in a given list can be unlocked.
The `canUnlockAll` function takes a list of lists called `boxes` as input. 
Each inner list represents a box, and the indices of the inner lists represent 
the keys contained in each box. 
The function returns True if all the boxes can be unlocked, and False otherwise.
Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True
In the above example, there are 4 boxes. 
The first box has a key to the second box, 
the second box has a key to the third box, and 
the third box has a key to the fourth box. 
Since all the boxes can be unlocked, the function returns True.
"""
def canUnlockAll(boxes):
    # Create a set to keep track of the boxes that have been visited
    visited = set()
    visited.add(0)  # Mark the first box as visited

    # Create a stack to store the boxes that need to be visited
    stack = [0]

    # Iterate through the stack until it is empty
    while stack:
        box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[box]:
            # If the key opens a new box and it hasn't been visited yet, add it to the stack
            if key < len(boxes) and key not in visited:
                stack.append(key)
                visited.add(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)