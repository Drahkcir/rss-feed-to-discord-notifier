#!/bin/python3

#standard lib imports
import logging
import argparse
import sys
import re

# local import
from modules import log
from modules import config 
from modules import rss_feed
from modules import webhook


"""
# method to create and iniatlise the logger of the script/service
"""
def get_logger(verbose=False,debug=False):
    level = logging.WARNING
    if verbose:
        level = logging.INFO

    if debug:
        level = logging.DEBUG

    logger = log.setup_custom_logger('root',level)

    return logger


"""
# method to parse the argument provided at script launch.
"""
def parse_args():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='get rss feed updates and send them on a discord server via a webhook')
    #parser.add_argument('-f', '')
    
    parser.add_argument('-d', '--debug', action='store_true', help='activate debug logs for debugging purpose')
    parser.add_argument('-v','--verbose', action='store_true', help='set the logger to info level to have more info on activity of the script')
    parser.add_argument('-c','--config', type=str, default='./src/config.ini', help='path to the config INI file to get the webhook url and the rss feed url')
    
    # parse arguments and catch the possible exception that could rise
    try:
        args = parser.parse_args()
    except BaseException as e:
        print(f'Error : parsing the arguments',file=sys.stderr)
        parser.print_help()
        exit(-1)
    return args


"""
# __main__ execution will be launch only if this is the main executed and not imported as a module.
""" 
if __name__ == "__main__" :

    args = parse_args()
    logger = get_logger(verbose=args.verbose, debug=args.debug)

    config_obj = config.configLoader(file=args.config)
    
    
    config_obj.pretty_print()
    
    # rss=rss_feed.feed_obj()

    # obj1=Webhook(WEBHOOK_URL)
    # obj1.edit_embeded()
    # obj1.sendMessages()
