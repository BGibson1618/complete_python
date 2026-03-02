"""
Decorator Template
"""
import functools

def deco(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # Added behavior that executes before the decorated function is called
        val = fn(*args, **kwargs)
        # added behavior that takes output from fn, or added behavior that executes after function call
        return val
    return wrapper


# Example 1

from datetime import datetime

def keep_it_down(fn):
    def wrapper():
        if 8 <= datetime.now().hour < 22:
            fn()
        else:
            pass # The neighbors are asleep
    return wrapper

@keep_it_down       # Equivalent to say_whee = keep_it_down(say_whee)
def say_whee():
    print('WHEEE!')

say_whee()

# Example 2 - Print runtime

