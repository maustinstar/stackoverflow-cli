from . import color
from . import query
import requests
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def numeric(str):
    for c in str:
        if c not in "1234567890":
            str = str.replace(c, '')
    return str

class SearchParser:

    def __init__(self, html):
        self.html = BeautifulSoup(html, 'html.parser')

    def getSummaries(self):
        return self.html.body.find_all('div', attrs={'class':'question-summary'})

    def getTitle(self, summary):
        return summary.find('a', attrs={'class':'question-hyperlink'}).text.strip()

    def getVotes(self, summary):
        result = summary.find('span', attrs={'class':'vote-count-post'})
        if result:
            return numeric(result.text)
        return '_'

    def getAnswerCount(self, summary):
        result = summary.find('div', attrs={'class':'status'})
        if result:
            return numeric(result.text)
        return '_'

    def getLink(self, summary):
        return query.QueryBuilder.root + summary.find('a').get('href')

    def open(self, number):
        webpage = requests.get(self.links[number]).text
        QuestionParser(webpage).print()

    def print(self, n):
        if n == None:
            n=5
        count = 0
        self.links = list()
        for question in self.getSummaries():
            if count >= n:
                continue
            title = self.getTitle(question)
            votes = color.paint(self.getVotes(question), color.Color.yellow)
            answers = self.getAnswerCount(question)
            self.links.append(self.getLink(question))

            if answers is not '_' and int(answers) > 0:
                answers = color.paint(answers, color.Color.green)
                title = color.paint(title, color.Color.green)

            print(str(count) + '.', votes, answers, title)
            count += 1

class QuestionParser:

    def __init__(self, html):
        self.html = BeautifulSoup(html, 'html.parser')

    def getPosts(self):
        return self.html.body.find_all('div', attrs={'class':'postcell'})

    def getAnswers(self):
        return self.html.body.find_all('div', attrs={'class':'answercell'})

    def printPost(self, post):
        for code in post.find_all('code'):
            code.name = 'p'
            code['class'] = 'code'
        for p in post.find_all('p'):
            text = p.text
            if 'class' in p.attrs and p['class'] == 'code':
                text = color.paint(text, color.Color.blue)
            print(text)

    def print(self):

        for post in self.getPosts():
            self.printPost(post)
            print('\n')
            input(color.paint('[Enter] to view answers', color.Color.cyan))
            print('\n')

        for post in self.getAnswers():
            self.printPost(post)
            print('\n')
            input(color.paint('[Enter] to continue', color.Color.cyan))
            print('\n')



            # title = self.getTitle(question)
            # votes = color.paint(self.getVotes(question), color.Color.yellow)
            # answers = self.getAnswerCount(question)
            #
            # if answers is not '_' and int(answers) > 0:
            #     answers = color.paint(answers, color.Color.green)
            #     title = color.paint(title, color.Color.green)
            #
            # print(str(count) + '.', votes, answers, title)
