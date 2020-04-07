import requests
import sys
from color import *
from parser import Parser
import argparse

parser = argparse.ArgumentParser(description='Search Stack Overflow.')
parser.add_argument('query', type=str, nargs='+', help='keywords to search in the archive')
parser.add_argument('-l', '--limit', type=int, help='max number of results to return')

args = parser.parse_args()

max_results = 5
if args.limit:
    max_results = int(args.limit)

webpage = requests.get("https://stackoverflow.com/questions").text

if args.query:
    webpage = requests.get('https://stackoverflow.com/search?q=' + '+'.join(args.query)).text


parser = Parser(webpage)
count = 1
for question in parser.getSummaries():
    if count > max_results:
        continue
    title = parser.getTitle(question)
    votes = color(parser.getVotes(question), Color.yellow)
    answers = parser.getAnswerCount(question)

    if int(answers) > 0:
        answers = color(answers, Color.green)
        title = color(title, Color.green)

    print(votes, answers, title)
    count += 1
