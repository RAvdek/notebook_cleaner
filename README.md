# `notebook_cleaner`

Command line tool for removing code blocks and prompts from an HTML export of an iPython notebook.
Requires [`docopt`](https://docopt.org) and [`BeautifulSoup4`](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Why?

You want to do some data analysis in iPython and you want to show your results to someone who doesn't care to see your code.

## Documentation

```
Usage:
  notebook_cleaner.py <infile> <outfile>
  notebook_cleaner.py (-h | --help)

Option:
  -h --help  	Prints this message
```

## An example

```
$ ipython nbconvert examples/my_notebook.ipynb
... nbconvert just created the new file examples/my_notebook.html ...
$ python notebook_cleaner.py examples/my_notebook.html examples/clean_notebook.html
New file: clean_notebook.html
```

[Here is link to the *before* picture](https://github.com/RAvdek/notebook_cleaner/blob/master/examples/my_notebook.html)
[... and a link to the *after* picture](iframe src="https://github.com/RAvdek/notebook_cleaner/blob/master/examples/clean_notebook.html)

## To do
- Need to work out the removal of warnings
- Images also leave behind some undesireable junk