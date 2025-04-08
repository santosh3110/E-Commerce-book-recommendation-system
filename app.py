from books_recommender.exception.exception_handler import CustomException
import sys
from books_recommender.logger.log import logging

try: 
    a=3/0

except Exception as e:
    logging.info(e)
    raise CustomException(e,sys)

