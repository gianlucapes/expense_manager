import logging

def setup_logger(name,level=logging.DEBUG,file='server.log'):
    logger = logging.getLogger(name)

    # Configure the custom  logger
    logger.setLevel(level=level)
    file_handler = logging.FileHandler(file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
