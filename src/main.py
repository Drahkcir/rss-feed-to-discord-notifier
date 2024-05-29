#!/bin/python3
import re
import logging
import argparse

# 
import feedparser
from discord_webhook import DiscordWebhook,DiscordEmbed

# local import
from modules import webhook 


"""
# method to create and iniatlise the logger of the script/service
"""
def get_logger():
    #TODO create logger to be able to report how thing are going 
    pass

"""
# method to parse the argument provided at script launch.
"""
def parse_args(args:str):
    #TODO add arguments to be able to set differents configuration at launch and different logging level
    pass


def get_webhoot_url(path:str):
    # getting the webhook url from the default file
    WEBHOOK_URL=''
    with open('.webhook_url') as f:
        WEBHOOK_URL=f.readlines()[0]
    #TODO perform sanitizing of the url to avoid trailing newline or other potential problem
    return WEBHOOK_URL





obj1=Webhook(WEBHOOK_URL)
obj1.edit_embeded()
obj1.sendMessages()