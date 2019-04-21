import logging


class Logger:
    def __init__(self, app_name, log_file_name, formatter):
        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler(log_file_name)
        self.fh.setLevel(logging.DEBUG)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.ERROR)

        self.formatter = logging.Formatter(formatter)
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.fh)

        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setFormatter(self.formatter)

        self.logger.addHandler(self.consoleHandler)
        self.logger.addHandler(self.ch)


