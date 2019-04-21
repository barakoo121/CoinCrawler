import logging
import redis
from bitcoin_crawler import BitcoinCrawler


def create_logger():
    # create logger with 'spam_application'
    logger = logging.getLogger('spam_application')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def create_db_connection():
    try:
        r = redis.Redis(host="localhost", port=6379)
        return r
    except Exception as e:
        print(e)
        exit()


def main():
    logger = create_logger()
    db = create_db_connection()

    bc1 = BitcoinCrawler(1, logger,
                         'https://api.coinmarketcap.com/v1/ticker/bitcoin/',
                         10, db)


if __name__ == "__main__":
    main()
