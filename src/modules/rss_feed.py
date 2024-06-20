import feedparser
import logging
import time

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
        
        

        

    def get_unprocessed_entry(self,last_processed_date:str):
        
        if last_processed_date:
            last_processed_date = time.strptime(last_processed_date)
            for item in self.items:
                date_field = ''
                if 'pubDate' in item.keys():
                    date_field = 'pubDate_parsed'
                elif 'published' in item.keys():
                    date_field = 'published_parsed'
                else:
                    logger.error(f'get_unprocessed_entry() -> unable to identify item {item} creation date field')
                    continue
                
                if item[date_field] > last_processed_date :
                    unprocessed_entries.append(item)
                    logger.debug(f'get_unprocessed_entry() -> adding {item.title} to list of unprocessed items')
        else:
            logger.info(f'get_unprocessed_entry() -> adding all items to list of unprocessed items since last processed items isn\'t initialized')
            unprocessed_entries = self.items()
        return unprocessed_entries


    # method to identify the author of the item/entry for feed where there is multiple authors (socials, news article, ...) which will be in a field of the embeded message
    def identify_author(item:dict):
        if 'author' in item :
            print(item['author']['name'])
            
            return 
        pass

    def get_feed_general_info(self):
        self.feed_info = {}
        for key in self.feed['feed'].keys():
            if key in [ 'title', 'link', 'subtitle', 'updated']:
                self.feed_info[key] = self.feed['feed'][key]             
                print(f'{key} : {self.feed["feed"][key]}\n')

    def pretty_print_entries_title(self):
        pp = [f'url : {self.url}'] 
        for i in self.items:
            pp.append(f'{i.title}')
        print ('\n'.join(pp))
        
        