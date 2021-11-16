# deque

from collections import deque
from time import time

# q = deque([1,2,3,4])
q = [1,2,3,4]
# print(q.pop())
# print(q.popleft())
# q.append(5)
# q.appendleft(10)
# print(q)
# print(list(q))

start_time = time()
LOOP_COUNT = 5000000
for x in range(LOOP_COUNT):
    q.append(x)
mid_time = time()
print('append time: {}'.format(mid_time - start_time))

for _ in range(LOOP_COUNT):
    tmp = q.pop()
pop_time = time()
print('pop time: {}'.format(pop_time - mid_time))

for x in range(LOOP_COUNT):
    q.insert(x,x)

end_time = time()
print('insert time: {}'.format(end_time - pop_time))

