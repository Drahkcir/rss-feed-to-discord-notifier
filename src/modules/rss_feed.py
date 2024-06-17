import feedparser
import logging
import datetime

logger=logging.getLogger('root')

class feed_obj:

    def __init__(self,url:str):

        self.url=url
        logger.info(f'__init__() -> parsing the rss feed : {url}')
        try:
            self.feed = feedparser.parse(url)
        except:
            logger.error(f'an error occured when attempting to parse the rss feed plaease verify that the url is right in the config file : {url}')
            exit(-1)
        logger.debug(f'__init__() -> rss feed sucessfully parsed : ')
        
        # get item from the rss_feed
        self.items = self.feed['entries']
        
        self.feed_info = self.get_feed_general_info()
        

        

    def get_unprocessed_entry(self,last_processed_date:datetime):
        unprocessed_entries={}
        if last_processed_date:
            for item in self.items:
                date_field = ''
                if 'pubDate' in item.keys():
                    date_field = 'pubDate'
                elif 'published' in item.keys():
                    date_field = 'pubDate'
                else:
                    logger.error('unable to identify item {item} creation date field')
                    continue

                # TODO parse date of field
            
                if item[date_field] < last_processed_date :
                    unprocessed_entries.append(item)
            else:
                unprocessed_entries = self.items()
        return unprocessed_entries


    # method to identify the author of the item/entry for feed where there is multiple authors (socials, news article, ...) which will be in a field of the embeded message
    def identify_author(item:dict):
        if 'author' in item :
            print(item['author']['name'])
            
            return 
        pass

    def get_feed_general_info(self):
        
        for key in self.items.keys():
            print(f'{key} : {self.items[key]}')
        # TODO keys of interest : 'title' | 'link' | 'subtitle' | 'updated' 
        

    def pretty_print_entries_title(self):

        pp = [f'url : {self.url}'] 

        for key in self.feed['entries'][0].keys():
            pp.append(f'{key} :  {self.items[0][key]}')
        print ('\n'.join(pp))
        return
        