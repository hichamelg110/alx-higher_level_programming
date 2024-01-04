#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    print("Number of argument{}{}:".format('' if arg_count == 1 else 's', '' if arg_count else '.'))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

