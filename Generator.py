"""
Create a generator function that YIELDS a value at each iteration. Assign an instance of the function to a variable.
Use the 'next' keyword to call the instance. Each call will produce a single value, and only that value is held in
memory.
"""
def gen_func(nums):
    for num in nums:
        yield num * 2

li = [1, 2, 3, 4]

gen = gen_func(li)

while True:
    try:
        print(next(gen), end=' ')
    except StopIteration:
        print('')
        break

# Any iterable object can be turned into an ITERATOR object using the iter() function. The next keyword can then be
# used on the iterator in the same way as it is with a generator.

li_iter = iter(li)

while True:
    try:
        print(next(li_iter), end=' ')
    except StopIteration:
        print('')
        break

# iter() can be used with a sentinel value to continually yield an output until the sentinel value is reached.

from random import randint

my_rando = iter(lambda: randint(1, 10), 7)

while True:
    try:
        print(next(my_rando))
    except StopIteration:
        break
