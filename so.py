import requests
import sys
from color import *
from parser import Parser

webpage = requests.get("https://stackoverflow.com/questions").text

args = sys.argv
args.remove('so.py')
if len(args) > 0:
    query = '+'.join(args)
    webpage = requests.get('https://stackoverflow.com/search?q=' + query).text


parser = Parser(webpage)
count = 0
for question in parser.getSummaries():
    if count > 6:
        continue
    title = parser.getTitle(question)
    votes = color(parser.getVotes(question), Color.yellow)
    answers = parser.getAnswerCount(question)

    if int(answers) > 0:
        answers = color(answers, Color.green)
        title = color(title, Color.green)

    print(votes, answers, title)
    count += 1
