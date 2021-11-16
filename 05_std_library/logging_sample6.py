# rotation, timerotation

import logging
import logging.config

logging.config.fileConfig(fname='conf/logger_2.conf')

logger = logging.getLogger('samplelogger')

import time
for _ in range(1000):
    logger.debug('デバッグログ')
    logger.info('インフォログ')
    logger.warning('ワーニングログ')
    logger.error('エラーログ')
    logger.critical('クリティカルログ')
    time.sleep(1)