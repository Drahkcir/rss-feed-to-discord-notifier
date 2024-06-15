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

    def pretty_print_entries_title(self):

        pp = [f'url : {self.url}'] 

        for key in self.feed['entries'][0].keys():
            pp.append(f'{key} :  {self.feed["entries"][0][key]}')
        print ('\n'.join(pp))
        return
        