import requests
import sys
from color import color
from color import Color
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def numeric(str):
    for c in str:
        if c not in "1234567890":
            str = str.replace(c, '')
    return str

webpage = requests.get("https://stackoverflow.com/questions").text

args = sys.argv
args.remove('so.py')
if len(args) > 0:
    query = '+'.join(args)
    webpage = requests.get('https://stackoverflow.com/search?q=' + query).text


# print(webpage)
parsed_html = BeautifulSoup(webpage, 'html.parser')
count = 0
for question in parsed_html.body.find_all('div', attrs={'class':'question-summary'}):
    if count > 6:
        continue
    title = question.find('a', attrs={'class':'question-hyperlink'}).text
    votes = color(numeric(question.find('span', attrs={'class':'vote-count-post'}).text), Color.yellow)
    answers = numeric(question.find('div', attrs={'class':'status'}).text)

    if int(answers) > 0:
        answers = color(answers, Color.green)
        title = color(title, Color.green)

    print(votes, answers, title)
    count += 1
