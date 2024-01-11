#!/usr/bin/python3
def weight_average(lst=[]):
    if not lst:
        return 0
    w = 0
    s = 0
    for score, weight in lst:
        w += weight
        s += score * weight
    return s / w
