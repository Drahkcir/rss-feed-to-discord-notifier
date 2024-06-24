# std lib import
import logging

# specific import 
from discord_webhook import DiscordWebhook,DiscordEmbed

# local import
from . import config
logger=logging.getLogger('root')


class Webhook:

    # constructor
    def __init__(self,url:str, title:str, embeded_config:dict, description:str='notifier', color:str ='03b2f8'):
        
        logger.debug(f'__init__() --> url: {url}')
        self.webhook = DiscordWebhook(url, rate_limit_retry=True)  
        
        logger.debug(f'__init__() --> title: {title}  description: {description} color:{color}')
        self.embed = DiscordEmbed(title=title, description=description, color=color)


        self.create_base_embeded(embeded_config=embeded_config)
    

        
    def create_base_embeded(self, embeded_config:dict):
        
        logger.debug(f"name= {embeded_config['author'][0]}, url= {embeded_config['author'][1]}, icon_url= {embeded_config['author'][2]}")
        self.embed.set_author(name= embeded_config['author'][0], 
                              url= embeded_config['author'][1], 
                              icon_url= embeded_config['author'][2])
        
        self.embed.set_thumbnail(url= embeded_config['thumbnail'])
        
        self.embed.set_footer(text= embeded_config['footer'][0], 
                              icon_url= embeded_config['footer'][1])

        # set timestamp (default is now) accepted types are int, float and datetime
        self.embed.set_timestamp()

        # add embed object to webhook
        self.webhook.add_embed(self.embed)
    

    def send(self,retries:int = 3):
        i = 0 
        
        while not ( retries <= i ):
            i += 1 
            try:
                response = self.webhook.execute()
            except TimeoutError as err:
                logger.error(f"Oops! Connection to Discord timed out: {err}")
                continue
            if response.status_code != 200:
                logger.error(f"Error while tentatively sending message to discord rc:{response.status_code} : {response.content}")
                continue

            logger.info(f'message sent to discord with success {response.status_code}')
            break

    def set_footer(self, footer_text:str = '', icon_url:str = None):
        self.embed.set_footer(text=footer_text, icon_url=icon_url)

    def set_author(self,name:str, url:str, icon:str = '' ):
        self.embed.set_author(name=name, url=url, icon_url="author icon url")

    def set_thumbnail(self, url:str = ''):
        self.embed.set_thumbnail(url=url)
