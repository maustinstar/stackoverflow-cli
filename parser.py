try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def numeric(str):
    for c in str:
        if c not in "1234567890":
            str = str.replace(c, '')
    return str

class Parser:

    def __init__(self, html):
        self.html = BeautifulSoup(html, 'html.parser')

    def getSummaries(self):
        return self.html.body.find_all('div', attrs={'class':'question-summary'})

    def getTitle(self, summary):
        return summary.find('a', attrs={'class':'question-hyperlink'}).text.strip()

    def getVotes(self, summary):
        return numeric(summary.find('span', attrs={'class':'vote-count-post'}).text)

    def getAnswerCount(self, summary):
        return numeric(summary.find('div', attrs={'class':'status'}).text)
