#!/usr/bin/python3
"""
Function to pass log files
"""
import sys


def print_m(dictStatCode, total_file_size):
    """
    Args:
        None
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dictStatCode.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dictStatCode = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        current_line = line.split()  # trimming excessspaces
        current_line = current_line[::-1]  # reversing the array

        if len(current_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(current_line[0])  # save file size
                code = current_line[1] 

                if (code in dictStatCode.keys()):
                    dictStatCode[code] += 1

            if (counter == 10):
                print_m(dictStatCode, total_file_size)
                counter = 0

finally:
    print_m(dictStatCode, total_file_size)
