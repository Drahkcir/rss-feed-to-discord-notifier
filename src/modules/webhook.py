import configparser
import logging

from . import config
from discord_webhook import DiscordWebhook,DiscordEmbed

logger=logging.getLogger('root')


class Webhook:

    # constructor
    def __init__(self,url:str, title:str, embeded_config:dict, description:str='notifier', color:str ='03b2f8'):
        
        logger.debug(f'__init__() --> url: {url}')
        self.webhook = DiscordWebhook(url, rate_limit_retry=True)  
        
        logger.debug(f'__init__() --> title: {title}  description: {description} color:{color}')
        self.embed = DiscordEmbed(title=title, description=description, color=color)


        self.create_base_embeded(embeded_config=embeded_config)
    

        # set timestamp (default is now) accepted types are int, float and datetime
        self.embed.set_timestamp()

        # add embed object to webhook
        self.webhook.add_embed(self.embed)
    

    def send_embeded(self):
        self.webhook.execute(remove_embeds=True)

    def send_message(self):
        response = self.webhook.execute()