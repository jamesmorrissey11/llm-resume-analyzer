import logging

import colorlog


def create_logger():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter("%(blue)s%(name)s: %(log_color)s%(message)s"))
    logger = colorlog.getLogger("my_logger")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


my_logger = create_logger()
