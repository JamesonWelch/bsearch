#! /usr/local/bin/python3

# bsearch

import webbrowser
import argparse


parser = argparse.ArgumentParser(description="Visit a URL or perform a Google search in your default browser")

group = parser.add_mutually_exclusive_group()

# URL
parser.add_argument(
        '-u', '--url', help='Visits the url in the default browser'
)

# Google Search
parser.add_argument(
        '-g', '--google', help='Displays the Googled query in the default browser'

)

args = parser.parse_args()


def parse():
	if args.google:
		addr = 'https://www.google.com/search?q={}'.format(args.google)
	if args.url:
		addr = 'http://www.{}'.format(args.url)
		
	webbrowser.open_new(addr)


if __name__ == '__main__':
	parse()

