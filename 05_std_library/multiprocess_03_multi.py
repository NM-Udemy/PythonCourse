# multiprocess_03_multi.py

import multiprocessing
import time

def process_function(name):
    print('Process {}: start'.format(name))
    time.sleep(2)
    print('Process {}: end'.format(name))

if __name__ == '__main__':
    print('Main Start')
    process_list = []
    for index in range(3):
        process = multiprocessing.Process(target=process_function, args=(index,))
        process_list.append(process)
        process.start() # 子プロセスの処理開始
    
    for index, process in enumerate(process_list):
        print('Main: before join {}'.format(index))
        process.join() # プロセスが終了するまで処理を待ちます
        print('Main: after join {}'.format(index))
    