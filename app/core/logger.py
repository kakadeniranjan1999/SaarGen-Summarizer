import logging


def get_logger(base_logger):
    logger = base_logger
    fileHandler = logging.FileHandler("app.log")
    logger.addHandler(fileHandler)
    logger.addHandler(logging.StreamHandler())

    formatter = logging.Formatter(
        '[%(asctime)s.%(msecs)03d] :: [%(levelname)s] :: [%(thread)d] :: [%(module)s] :: Line --> %(lineno)d :: %(message)s',
        '%d/%m/%Y %I:%M:%S %p',
    )

    for handler in logger.handlers:
        handler.setFormatter(formatter)

    return logger