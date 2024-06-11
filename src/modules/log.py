import logging

def setup_custom_logger(name,level):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.WARNING) # default level at object creation    

    logger.addHandler(handler)
    return logger