# multiprocess_02_class.py

import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def process_function(self):
        print('Process {}: start'.format(self.name))
        time.sleep(2)
        print('Process {}: end'.format(self.name))
    
    def run(self):
        print('run start')
        self.process_function()

if __name__ == '__main__':
    myProcess = MyProcess('Matsuda')
    myProcess.start()

    # myProcess.join()
    print('Main end')