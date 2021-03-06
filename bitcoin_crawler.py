import threading
import time
import datetime
import requests
from coin_crawler import CoinCrawler


class BitcoinCrawler(CoinCrawler):

    def __init__(self, interval, logger, api, max_cache, db):
        super().__init__(interval=interval, logger=logger,
                         api=api, max_cache=max_cache, db=db)

        thread = threading.Thread(target=self._run(), args=())
        thread.daemon = True
        thread.start()

    def get_current_coin(self):
        try:
            response = requests.get(self.api)
            self.logger.debug("Retrieved data from api")
            response_json = response.json()

            return float(response_json[0]['price_usd'])

        except Exception as e:
            self.logger.error("Error retrieving data from api: %s" % e)

            return None

    def _push_to_db(self):
        try:
            now_ = datetime.datetime.now().__str__()
            if self.db.set(now_, self.average(self.cache)):
                self.logger.debug("Succeded to push key %s" % now_)
            else:
                self.logger.error("Db push false reply")

        except Exception as e:
            self.logger.error("Error pushing to db: %s" % e)

    def _run(self):
        while True:
            coin = self.get_current_coin()

            if coin:
                self.logger.info("Current bitcoin currency is: %.2f$" % coin)
                self.cache.append(coin)

                if len(self.cache) == self.max_cache:
                    self.logger.info("The average rate for last cache is: %.2f$"
                                     % self.average(self.cache))
                    self._push_to_db()

                    self.cache = []

            time.sleep(self.interval)
