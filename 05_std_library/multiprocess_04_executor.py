# multiprocess_04_executor.py

import time
import concurrent.futures

def process_function(name, age):
    print('Process {}: starting {}'.format(name, age))
    time.sleep(2)
    print('Process {}: finishing {}'.format(name, age))

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # executor.submit(process_function, 1, '12')
        # executor.submit(process_function, 2, '12')
        # executor.submit(process_function, 3, '12')
        # executor.submit(process_function, 4, '12')
        executor.map(process_function, ['taro', 'jiro', 'saburo'], [1,2,3])