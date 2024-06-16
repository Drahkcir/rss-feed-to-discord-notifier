import feedparser
import logging

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
        self.items= self.feed['entries']
        
        self.get_feed_general_info()
        

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

        pass

    def get_feed_general_info(self):
        #print(self.feed)
        
        print(self.feed['feed']['title'])
        print(self.feed['feed']['link'])
        print(self.feed['feed']['subtitle'])
        print(self.feed['feed']['docs'])
        print(self.feed['feed']['generator'])
        print(self.feed['feed']['language'])
        print(self.feed['feed']['updated'])

    def pretty_print_entries_title(self):

        pp = [f'url : {self.url}'] 

        for key in self.feed['entries'][0].keys():
            pp.append(f'{key} :  {self.feed["entries"][0][key]}')
        print ('\n'.join(pp))
        return
        