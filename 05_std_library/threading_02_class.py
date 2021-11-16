# threading_02_class

from threading import Thread
import time
import logging

class MyThread(Thread):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg
    
    def run(self):
        logging.info('Thread {} start'.format(self.msg))
        time.sleep(2)
        logging.info('Thread {} end'.format(self.msg))

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    x = MyThread('Hello Sub Thread')
    x.start()
    logging.info('Main Start')
    x.join()
    logging.info('Main End')