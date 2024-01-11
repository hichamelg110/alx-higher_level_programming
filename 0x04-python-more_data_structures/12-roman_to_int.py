#!/usr/bin/python3
def weight_average(lst=[]):
    if not lst:
        return 0

    m = 0
    n = 0

    for tup in lst:
        m += tup[0] * tup[1]
        n += tup[1]

    return (m / n)

