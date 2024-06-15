import feedparser
import logging

logger=logging.getLogger('root')

class feed_obj:

    def __init__(self,url:str):
        self.feed = feedparser.parse(url)

    def get_unprocessed_entry(self):
        pass

    def identify_author():
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
        