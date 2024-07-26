#!/usr/bin/python3
"""
a module that contains a function called validUTF8 that
Determines if a given data set represents a valid UTF-8 encoding
for a list of integers
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    for a list of integers
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check if the current integer is a continuation byte
        if num >> 6 == 0b10:
            # If it's not a valid continuation byte, return False
            if num_bytes == 0:
                return False
            # Decrease the number of expected continuation bytes
            num_bytes -= 1
        else:
            # Check the number of bytes in the current UTF-8 character
            if num_bytes != 0:
                return False
            # Determine the number of bytes in the current UTF-8 character
            if num >> 7 == 0b0:
                num_bytes = 0
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False

    # If there are remaining expected continuation bytes, return False
    if num_bytes != 0:
        return False

    # All checks passed, return True
    return True
