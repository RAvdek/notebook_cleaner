""" notebook_cleaner

Removes code and prompts from an HTML export of an iPython notebook.

Usage:
  notebook_cleaner.py <infile> <outfile>
  notebook_cleaner.py (-h | --help)

Option:
  -h --help  	Prints this message
"""

import sys
from bs4 import BeautifulSoup
from docopt import docopt

def notebook_cleaner(infile, outfile):
	""" Removes code and prompts from HTML exports of an iPython notebook """
	in_f = open(infile, 'r')
	text = in_f.read()
	soup = BeautifulSoup(text)
	in_f.close()

	junk_tags = soup.find_all(class_=['input', 'prompt'])
	for tag in junk_tags:
		tag.decompose()

	out_f = open(outfile, 'w')
	out_f.write(str(soup))
	out_f.close()

def main():
	""" Flow for command line usage """
	cli_context = docopt(__doc__)	
	infile = cli_context['<infile>']
	outfile = cli_context['<outfile>']

	if infile == outfile:
		confirm = raw_input("Overwrite {0}? (y/n)".format(infile))
		if confirm.lower() not in ['y', 'yes']:
			return 0
	notebook_cleaner(infile, outfile)
	print("New file {0}".format(outfile))
	return 0

if __name__ == '__main__':
	sys.exit(main())