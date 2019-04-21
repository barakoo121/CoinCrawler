from bitcoin_crawler import BitcoinCrawler
from logger import Logger
from db_connection import DbConnection


def main():
    logger = Logger('coin_application', 'coins.log',
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    db = DbConnection('localhost', 6379, logger.logger)

    BitcoinCrawler(60, logger.logger,
                   'https://api.coinmarketcap.com/v1/ticker/bitcoin/',
                   10, db)


if __name__ == "__main__":
    main()
