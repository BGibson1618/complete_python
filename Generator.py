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

# For a class to be iterable and be able to be used as a generator, it must have the __iter__ and __next__ methods.

class MyGen:
    current = int()
    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen2 = MyGen(0, 100)

for i in gen2:
    print(i)

# Instructions in a generator can be placed after the yield statement, and they will execute on the next iteration.

def fib_gen(num):
    a, b = 0, 1
    for _ in range(num + 1):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib_gen(10):
    print(x)
