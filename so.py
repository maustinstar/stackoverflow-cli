import sys
from parser import Parser
from query import QueryBuilder
import argparse
import readline

parser = argparse.ArgumentParser(description='Search Stack Overflow.')
parser.add_argument('query', type=str, nargs='+', help='keywords to search in the archive')
parser.add_argument('-l', '--limit', type=int, help='max number of results to return')
parser.add_argument('-s', '--sort', type=str, help='sort by <relevance, newest, active, votes> or <r, n, a, v>')

args = parser.parse_args()

parser = Parser(QueryBuilder(args.query, args.sort).webpage)
parser.print(args.limit)
limit = args.limit
if args.limit is None:
    limit = 5

while True:
    n = input("select: ")
    if int(n) is not None and (int(n) < limit):
        parser.open(int(n))
        parser.print(args.limit)
    else:
        print('Type a question number.')
