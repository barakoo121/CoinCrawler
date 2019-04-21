import redis


class DbConnection:
    def __init__(self, host, port, logger):
        try:
            self.db_con = redis.Redis(host=host, port=port)
        except Exception as e:
            logger.error("Error connecting to db: %s" % e)
            exit()
