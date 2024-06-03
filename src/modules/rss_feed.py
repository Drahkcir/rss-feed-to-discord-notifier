import feedparser


class feed_obj:

    def __init__(self,url:str):
        self.feed = feedparser.parse(url)

    def get_unprocessed_entry(self):
        pass