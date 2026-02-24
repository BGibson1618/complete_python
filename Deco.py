"""
Decorator Template
"""

def my_deco(fn):
    def my_wrapper(*args, **kwargs):
        fn(*args, **kwargs)
    return my_wrapper

def my_func(li):
    return li * 2
