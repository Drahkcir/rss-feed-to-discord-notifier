import logging

def setup_custom_logger(name,level):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s', datefmt='%Y-%m-%d %H:%m:%S %z' )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level) 
    
    logger.addHandler(handler)
    return logger