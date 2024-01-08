#!/usr/bin/python3
def max_integer(num_list=[]):
    if not num_list:
        return None
    else:
        num_list.sort(reverse=True)
        return num_list[0]
