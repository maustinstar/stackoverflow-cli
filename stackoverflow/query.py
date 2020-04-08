import requests

class QueryBuilder:
    """Builds queries to Stack Overflow"""

    root = "https://stackoverflow.com"

    def __init__(self, search=None, sort=None):
        if search is None:
            self.url = 'https://stackoverflow.com/questions'
        else:
            if sort is None:
                sort = 'relevance'
            if sort in ['r','n','a','v']:
                sort = {'r':'relevance','n':'newest','a':'active','v':'votes'}[sort]
            self.url = 'https://stackoverflow.com/search?tab='+sort+'&q='+'+'.join(search)
        self.webpage = requests.get(self.url).text
