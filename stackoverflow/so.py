import sys
from . import parser
from . import query
from . import color

import argparse
import readline

def main():
    cli = argparse.ArgumentParser(description='Search Stack Overflow.')
    cli.add_argument('query', type=str, nargs='+', help='keywords to search in the archive')
    cli.add_argument('-l', '--limit', type=int, help='max number of results to return')
    cli.add_argument('-s', '--sort', type=str, help='sort by <relevance, newest, active, votes> or <r, n, a, v>')

    args = cli.parse_args()

    search = parser.SearchParser(query.QueryBuilder(args.query, args.sort).webpage)
    search.print(args.limit)
    limit = args.limit
    if args.limit is None:
        limit = 5

    while True:
        n = input(color.paint('select: ', color.Color.cyan))
        if parser.numeric(n) != '' and (int(n) < limit):
            search.open(int(n))
            search.print(args.limit)
        else:
            print(color.paint('Type a question number.', color.Color.red))

if __name__ == "__main__":
    main()
