import requests
import sys
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class style():
    BLACK = lambda x: '\033[30m' + str(x) + '\033[0m'
    RED = lambda x: '\033[31m' + str(x) + '\033[0m'
    GREEN = lambda x: '\033[32m' + str(x) + '\033[0m'
    YELLOW = lambda x: '\033[33m' + str(x) + '\033[0m'
    BLUE = lambda x: '\033[34m' + str(x) + '\033[0m'
    MAGENTA = lambda x: '\033[35m' + str(x) + '\033[0m'
    CYAN = lambda x: '\033[36m' + str(x) + '\033[0m'
    WHITE = lambda x: '\033[37m' + str(x) + '\033[0m'
    UNDERLINE = lambda x: '\033[4m' + str(x) + '\033[0m'
    RESET = lambda x: '\033[0m' + str(x) + '\033[0m'

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
    votes = style.YELLOW(numeric(question.find('span', attrs={'class':'vote-count-post'}).text))
    answers = numeric(question.find('div', attrs={'class':'status'}).text)

    if int(answers) > 0:
        answers = style.GREEN(answers)
        title = style.GREEN(title)

    print(votes, answers, title)
    count += 1
