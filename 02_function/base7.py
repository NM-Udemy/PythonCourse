# list, generator memory

import sys

list_a = [i for i in range(100000)]
def num(max):
    i = 0
    while i < max:
        yield i
        i += 1

# for i in num(100000):
#     print(i)

gen = num(100000)
print(sys.getsizeof(list_a))
print(sys.getsizeof(gen))
