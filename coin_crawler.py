from abc import ABC, abstractmethod


class CoinCrawler(ABC):

    def __init__(self, interval, logger, api, max_cache, db):
        self.cache = []
        self.max_cache = max_cache

        self.logger = logger
        self.api = api
        self.db = db

        self.interval = interval

    @staticmethod
    def average(cache):
        sum_elements = 0

        for value in cache:
            sum_elements += value

        return sum_elements / len(cache)

    @abstractmethod
    def get_current_coin(self):
        raise NotImplementedError

    @abstractmethod
    def _push_to_db(self):
        raise NotImplementedError
