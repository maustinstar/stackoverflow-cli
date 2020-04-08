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

class QuestionSummary:

    def __init__(self, html):
        self.html = html
        self.title = html.find('a', attrs={'class':'question-hyperlink'}).text.strip()

        votes = html.find('span', attrs={'class':'vote-count-post'})
        if votes:
            self.votes = numeric(votes.text)
        else:
            self.votes = '_'

        answer_count = html.find('div', attrs={'class':'status'})
        if answer_count:
            self.answer_count = numeric(answer_count.text)
        else:
            self.answer_count = '_'

        self.link = query.QueryBuilder.root + html.find('a').get('href')

    def open(self):
        QuestionParser(requests.get(self.link).text, self.answer_count).print()

class SearchParser:

    def __init__(self, html):
        self.html = BeautifulSoup(html, 'html.parser')
        summaries = self.html.body.find_all('div', attrs={'class':'question-summary'})
        self.summaries = [QuestionSummary(s) for s in summaries]
        self.results = 0

    def getSummary(self, n):
        return self.summaries[n]

    def open(self, n):
        self.getSummary(n).open()

    def print(self, n, mute=False):
        if n == None:
            n=5
        count = 0
        for question in self.summaries:
            if count >= n:
                continue
            title = question.title
            votes = color.paint(question.votes, color.Color.yellow)
            answers = question.answer_count

            if answers is not '_' and int(answers) > 0:
                answers = color.paint(answers, color.Color.green)
                title = color.paint(title, color.Color.green)

            if not mute:
                print(str(count) + '.', votes, answers, title)
            count += 1
        self.results = count

class QuestionParser:

    def __init__(self, html, answer_count):
        self.html = BeautifulSoup(html, 'html.parser')
        self.answer_count = int(answer_count)

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
            if self.answer_count == 0:
                input(color.paint('[Enter] to exit', color.Color.cyan))
                return
            input(color.paint('[Enter] to view '+str(self.answer_count)+' answers', color.Color.cyan))
            print('\n')

        count = 0
        for post in self.getAnswers():
            self.printPost(post)
            count += 1
            print('\n')
            if count == self.answer_count:
                input(color.paint('[Enter] to exit', color.Color.cyan))
                return
            input(color.paint('[Enter] to continue '+str(count+1)+'/'+str(self.answer_count), color.Color.cyan))
            print('\n')
