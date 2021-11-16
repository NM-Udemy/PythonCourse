# yaml

import logging
import logging.config
import yaml

with open('conf/logger_2.yaml', mode='r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('sampleLogger')

import time
for _ in range(1000):
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
    time.sleep(1)