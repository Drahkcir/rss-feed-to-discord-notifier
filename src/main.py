#!/bin/python3

#standard lib imports
import logging
import argparse
import sys
import re

# local import
from modules import webhook 
from modules import rss_feed

"""
# method to create and iniatlise the logger of the script/service
"""
def get_logger(verbose=False,debug=False):
    #TODO create logger to be able to report how thing are going 
    logger= logging.getLogger()
    logger.setLevel(logging.WARNING) # default level at object creation

    if verbose:
        logger.setLevel(logging.INFO)

    if debug:
        logger.setLevel(logging.DEBUG)    


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
    logger = get_logger()

    rss=rss_feed.feed_obj('')

    # obj1=Webhook(WEBHOOK_URL)
    # obj1.edit_embeded()
    # obj1.sendMessages()
