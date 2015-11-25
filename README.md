# `notebook_cleaner`

A command line tool for removing code blocks and prompts from an HTML export of an iPython notebook.

## Why?

You want to do some data analysis in iPython and you want to show your results to someone who doesn't care to see your code.

## Installation

`pip install notebook_cleaner`

## Usage

```
Usage:
  notebook_cleaner <infile> [<outfile>]
  notebook_cleaner (-h | --help)

Option:
  -h --help  	Prints this message
  -f --force    Don't prompt if a file is goint to be overwritten
```

If `<outfile>` doesn't exist or matches `<infile>`, you'll be prompted to verify it's okay to overwrite `<infile>`.

## An example

```
$ cd examples
$ ipython nbconvert my_notebook.ipynb
... nbconvert just created the new file examples/my_notebook.html ...
$ python notebook_cleaner.py my_notebook.html clean_notebook.html
New file: clean_notebook.html
```

[Here is link to the *before* picture](https://htmlpreview.github.io/?https://github.com/RAvdek/notebook_cleaner/blob/master/examples/my_notebook.html)

[... and a link to the *after* picture](https://htmlpreview.github.io/?https://github.com/RAvdek/notebook_cleaner/blob/master/examples/clean_notebook.html)

## To do
- Need to work out the removal of warnings.
- Images also leave behind some undesireable junk.
- More edge cases could become apparent with use
