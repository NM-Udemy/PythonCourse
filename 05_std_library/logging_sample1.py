# logging
import logging

logging.basicConfig(
    level=logging.ERROR, filename='sample.log', filemode='w',
    format='%(asctime)s-%(process)s-%(levelname)s-%(message)s'
    )
logging.debug('debug log')
logging.info('info log')
logging.warning('warning log')
logging.error('error log')
logging.critical('critical log')

user = 'Taro'
logging.error(f'{user=} raised error')

a = 10
b = 0
try:
    c = a / b
except Exception as e:
    logging.error(e, exc_info=True)