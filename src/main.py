#!/bin/python3
import re
import feedparser
from discord_webhook import DiscordWebhook,DiscordEmbed

# getting the
WEBHOOK_URL=''
with open('.webhook_url') as f:
    WEBHOOK_URL=f.readlines()[0]


class Webhook:

    # constructor
    def __init__(self,url,title='CERT-FR',description='notifier'):
        self.webhook = DiscordWebhook(
            url=url,
            rate_limit_retry=True,
            description=description,
            title=title
            )
        return
        

    def send_message(self):
        pass

    def edit_message(self, content):

        self.webhook.content=content


    def edit_embeded(self):
        # create embed object for webhook
        # you can set the color as a decimal (color=242424) or hex (color="03b2f8") number
        embed = DiscordEmbed(title="CERT-FR", description="Lorem ipsum dolor sit", color="03b2f8")

        # add embed object to webhook
        self.webhook.add_embed(embed)

    def sendMessages(self):
        response = self.webhook.execute()
        





obj1=Webhook(WEBHOOK_URL)
obj1.edit_embeded()
obj1.sendMessages()