import inspect
import itertools
from functools import wraps

def getpr(func):
    def wrapper(*args):
        args_name = func.__code__.co_varnames
        args_dict = dict(itertools.zip_longest(args_name[1:], args))
        args_values = args_dict.values()
        return args_dict
    return wrapper




