#! /usr/bin/env python3
""" notebook_cleaner

Removes code and prompts from an HTML export of an iPython notebook.

Usage:
  notebook_cleaner <infile> [<outfile>]
  notebook_cleaner (-h | --help)

Option:
  -h --help  	Prints this message
  -f --force    Don't prompt when execution will overwrite existing file
"""

import sys
from bs4 import BeautifulSoup
from docopt import docopt

JUNK_CLASSES = ['input', 'prompt']

def notebook_cleaner(infile, outfile):
	""" Removes code and prompts from HTML exports of an iPython notebook """

	with open(infile, 'r') as in_f:
		soup = BeautifulSoup(in_f.read())

	junk_tags = soup.find_all(class_=JUNK_CLASSES)
	for tag in junk_tags:
		tag.decompose()

	with open(outfile, 'w') as out_f:
		out_f.write(str(soup))

def main():
	""" Flow for command line usage """
	cli_context = docopt(__doc__)
	infile = cli_context['<infile>']
	outfile = cli_context['<outfile>']
	print(cli_context)
	if infile.split('.')[-1].lower() != 'html':
		raise Exception("Not reading from a *.html file")

	if not outfile:
		outfile = infile

	if infile == outfile:
		confirm = input("Overwrite {0}? (y/n):\t".format(infile))
		if confirm.lower() not in ['y', 'yes']:
			return 0

	notebook_cleaner(infile, outfile)
	print("New file {0}".format(outfile))
	sys.exit(0)

if __name__ == '__main__':
	main()
