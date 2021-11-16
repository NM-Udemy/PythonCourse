# threading_03_multi
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def thread_function(name):
    logging.info('{} thread: start'.format(name))
    time.sleep(2)
    logging.info('{} thread: finish'.format(name))

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    with ThreadPoolExecutor(max_workers=3) as executor:
        # executor.map(thread_function, ['Taro', 'Jiro', 'Saburo'])
        executor.submit(thread_function, 'Taro')
        executor.submit(thread_function, 'Jiro')
        executor.submit(thread_function, 'Saburo')
        executor.submit(thread_function, 'Shiro')

    # threads = [] # リスト
    # for name in ('Taro', 'Jiro', 'Saboro'):
    #     logging.info('Main: create and start {}'.format(name))
    #     x = threading.Thread(target=thread_function, args=(name,))
    #     threads.append(x)
    #     x.start()
    # for i, t in enumerate(threads):
    #     logging.info('Main: before join {}'.format(i))
    #     t.join()
    #     logging.info('Main: thread done {}'.format(i))
