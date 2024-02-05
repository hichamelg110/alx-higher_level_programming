#!/usr/bin/python3
"""
Module with a custom list class, MyList.
"""

class MyList(list):
    """
    MyList inherits from list and adds print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
