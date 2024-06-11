import configparser
import logging

from . import config
from discord_webhook import DiscordWebhook,DiscordEmbed

logger=logging.getLogger('root')


class Webhook:

    # constructor
    def __init__(self,url:str, title:str, description:str='notifier'):
        self.webhook = DiscordWebhook(url,rate_limit_retry=True)
        self.embed=None
        
        
    def create_embeded(self,config:configparser):

        # you can set the color as a decimal (color=242424) or hex (color="03b2f8") number
        self.embed = DiscordEmbed(title="CERT-FR", description="Lorem ipsum dolor sit", color="03b2f8")

        self.embed.set_author(name="", url="", icon_url=config.author_image)        
        self.embed.set_image(url=config.author_image)
        self.embed.set_thumbnail(url="")
        self.embed.set_footer(text="footer text", icon_url="")

        # set timestamp (default is now) accepted types are int, float and datetime
        self.embed.set_timestamp()

        # add embed object to webhook
        self.webhook.add_embed(self.embed)
    

    def send_embeded(self):
        self.webhook.execute(remove_embeds=True)

    def send_message(self):
        response = self.webhook.execute()