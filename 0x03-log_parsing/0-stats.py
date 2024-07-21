#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


# Status code and their count of appearance in the log
status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:  # Read line by line
        line_list = line.split(" ")  # Split the line by space
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            # Check if the code is in the status_code
            if code in status_code.keys():
                status_code[code] += 1
            total_size += size
            counter += 1

        if counter == 10:  # Print the size and the status code every 10 lines
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:  # Print the size and the status code when the loop ends
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
