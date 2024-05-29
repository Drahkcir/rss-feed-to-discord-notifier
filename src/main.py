#!/bin/python3
import re
import feedparser
from discord_webhook import DiscordWebhook,DiscordEmbed

# getting the
WEBHOOK_URL=''
with open('.webhook_url') as f:
    WEBHOOK_URL=f.readlines()[0]
    #TODO perform sanitizing of the url to avoid trailing newline or other potential problem
    return WEBHOOK_URL





obj1=Webhook(WEBHOOK_URL)
obj1.edit_embeded()
obj1.sendMessages()