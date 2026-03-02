import functools
import time

def do_twice(fn):
    """Execute decorated function twice"""
    @functools.wraps(fn)
    def wrapper_do_twice(*args, **kwargs):
        fn(*args, **kwargs)
        fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return wrapper_do_twice

def repeat(num_times = 1):
    """Execute decorated function a specified number of times"""
    def deco_repeat(fn):
        @functools.wraps(fn)
        def wrap_repeat(*args, **kwargs):
            for _ in range(num_times):
                val = fn(*args, **kwargs)
            return val
        return wrap_repeat
    return deco_repeat

def timer(fn):
    """Print runtime of decorated function"""
    @functools.wraps(fn)
    def wrap_timer(*args, **kwargs):
        t1 = time.perf_counter()
        val = fn(*args, **kwargs)
        t2 = time.perf_counter()
        run_time = t2 - t1
        print(f'Finished {fn.__name__} in {run_time: .4f} secs')
        return val
    return wrap_timer