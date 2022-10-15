import os
import logging

SOME_BUCKET = os.getenv('SOME_BUCKET')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info('incoming event: {}'.format(event))
    logger.info('Environment variable: {}'.format(SOME_BUCKET))

    return {
      'statusCode': 200,
      'body': 'hey from lambda!'
    }