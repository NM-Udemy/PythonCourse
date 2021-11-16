# multiprocess_08_queue.py

from multiprocessing import Process, Queue
from multiprocessing.queues import Empty, Full

def put_function(queue, list_a):
    for value in list_a:
        try:
            queue.put(value, block=True, timeout=1)
        except Full as e:
            print('Queueがいっぱい')

def get_function(queue):
    while 1:
        try:
            print(queue.get(timeout=1))
        except Empty as e:
            print('中身がない')
            return

if __name__ == '__main__':
    queue = Queue(maxsize=4)
    p1 = Process(target=put_function, args=(queue, ['A', 'B', 'C', 'D']))
    p1.start()
    p1.join()
    p2 = Process(target=get_function, args=(queue,))
    p2.start()
    p2.join()
    # while not queue.empty():
    #     print(queue.get())