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
    parser = argparse.ArgumentParser(description='get rss feed updates and send them on a discord server via a webhook', add_help=False)

    parser.add_argument('-h', '--help', action='help')

    parser.add_argument('-d',  '--debug', action='store_true', help='activate debug logs for debugging purpose')
    parser.add_argument('-v', '--verbose', action='store_true', help='set the logger to info level to have more info on activity of the script')
    parser.add_argument('-c', '--config', type=str, default='./src/config.ini', help='path to the config INI file to get the webhook url and the rss feed url')
    parser.add_argument('-s', '--section', type=str, default='DEFAULT', help='Section of the config INI file to get the webhook url and the rss feed url')
    parser.add_argument('-l', '--loop', type=int, choices=range(0, 1800), metavar='[0-1800]', default=0,
                        help='if set to other than 0 the programm will loop to continuously to read the feed every {X} seconds')

    # parse arguments and catch the possible exception that could rise
    args = parser.parse_args()

    return args


"""
# prepare dictionnary for our embedded message from the config object
"""
def make_webhooks_config(config:config.configLoader): 
    embed = {
        'author': (config.get_field('author_name'), 
                   config.get_field('author_url'),
                   config.get_field('author_image_url')),
        'thumbnail': config.get_field('embeded_image_url'),
        'footer': (config.get_field('footer_message'),config.get_field('footer_image_url')),
        'timestamps': ''
    }

    logger.debug(f'make_webhook_config -> creating dictionnary for embeded message : {embed}')

    return embed


"""
# main (default) process for one reading of the feed parser and process unprocessed feed item (based on last pubDate in config ini)
"""
def main_process(conf:config.configLoader):
    
    
    embeded_config = make_webhooks_config(conf)

    rss_obj=rss_feed.feed_obj(conf.get_field('rss_feed_url'))
    rss_obj.pretty_print_entries_title()
    
    
    if rss_obj.get_unprocessed_entry(conf.get_field('last_pub_date_processed')) != 0 :
        logger.info('no unprocessed entries to send to discord')
        return
     
    for item in rss_obj.unprocessed_entries:
        
        message = f'{item.description} \n\nlink : {item.link}'

        # creating the webhook 
        webhook_obj = webhook.Webhook(url = conf.get_field('webhook_url'), title=item.title, description=message, embeded_config=embeded_config) 
        # sending the webhook 
        webhook_obj.send()

    conf.set_field('last_pub_date_processed',rss_obj.process_date)
    return 0

    



"""
# __main__ execution will be launch only if this is the main executed and not imported as a module.
""" 
if __name__ == "__main__" :

    # get args and configs
    args = parse_args()
    logger = get_logger(verbose=args.verbose, debug=args.debug)
    conf = config.configLoader(file=args.config,section=args.section)
    
    main_process(conf)
    
    logger.info('script is finished...')
    exit(0)