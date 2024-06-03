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
    


    pass

"""
# method to parse the argument provided at script launch.
"""
def parse_args():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='get rss feed updates and send them on a discord server via a webhook')
    #parser.add_argument('-f', '')
    
    parser.add_argument('-d', '--debug', action='store_true', help='activate debug logs for debugging purpose')
    parser.add_argument('-v','--verbose', action='store_true', help='set the logger to info level to have more info on activity of the script')

    webhook_options = parser.add_mutually_exclusive_group(required=True)

    webhook_options.add_argument('--webhook-file', type=str, help='path to file with webhook url')
    webhook_options.add_argument('--webhook-url', type=str, help='provide directly the webhook url from the argument')

    rssfeed_options = parser.add_mutually_exclusive_group(required=True)
    rssfeed_options.add_argument('--rss-file', type=str, help='path to file with RSS feed url')
    rssfeed_options.add_argument('--rss-url', type=str, help='provide directly the RSS feed url from the argument')
    
    # parse arguments and catch the possible exception that could rise
    try:
        args = parser.parse_args()
    except BaseException as e:
        print(f'Error : parsing the arguments',file=sys.stderr)
        parser.print_help()
        exit(-1)
    return args


"""
# get the webhook(s) from the file provided  
"""
def get_webhoot_url(path:str): 
    WEBHOOK_URL=''
    with open('.webhook_url') as f:
        WEBHOOK_URL=f.readlines()[0]
    #TODO perform sanitizing of the url to avoid trailing newline or other potential problem
    return WEBHOOK_URL




"""
# __main__ execution will be launch only if this is the main executed and not imported.
""" 
if __name__ == "__main__" :

    args = parse_args()
    logger = get_logger()


    # obj1=Webhook(WEBHOOK_URL)
    # obj1.edit_embeded()
    # obj1.sendMessages()
