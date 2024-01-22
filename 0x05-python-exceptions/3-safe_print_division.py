#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a/b
    except ZeroDivisionError:
        return None
    finally:
        print("{}".format(result))
        return result
