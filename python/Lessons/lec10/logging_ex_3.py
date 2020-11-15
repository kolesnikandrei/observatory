import logging
import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
print(logger, logger.level, logger.handlers)


logger.setLevel(logging.DEBUG)
print(logger, logger.level)

logger.warning('warn_info')
logger.debug('debugging information')

response = requests.get('http://google.com')

for l in logging.Logger.manager.loggerDict:
    print(l)
