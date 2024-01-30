def magic_string(n=None):
    n = n if n is not None else 1
    return "BestSchool, " * (n - 1) + "BestSchool"
