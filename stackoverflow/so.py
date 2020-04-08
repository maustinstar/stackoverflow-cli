import sys
from . import so_parser
from . import query
from . import color

import argparse
import readline

parser = argparse.ArgumentParser(description='Search Stack Overflow.')
parser.add_argument('query', type=str, nargs='+', help='keywords to search in the archive')
parser.add_argument('-l', '--limit', type=int, help='max number of results to return')
parser.add_argument('-s', '--sort', type=str, help='sort by <relevance, newest, active, votes> or <r, n, a, v>')

args = parser.parse_args()

parser = so_parser.SearchParser(query.QueryBuilder(args.query, args.sort).webpage)
parser.print(args.limit)
limit = args.limit
if args.limit is None:
    limit = 5

while True:
    n = input(color.paint('select:', color.Color.cyan))
    if so_parser.numeric(n) is not '' and (int(n) < limit):
        parser.open(int(n))
        parser.print(args.limit)
    else:
        print(color.paint('Type a question number.', color.Color.red))
