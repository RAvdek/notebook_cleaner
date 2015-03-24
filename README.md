# `notebook_cleaner`
Command line tool for removing code blocks and prompts from an HTML export of an iPython notebook.
Requires `docopt` and `BeautifulSoup4`

Why?
====
You want to do some data analysis in iPython and you want to show your results to someone who doesn't want to see your code.

Usage
=====
    $ ipython nbconvert some_notebook.ipynb
    # nbconvert just created the new file some_notebook.html
    $ python notebook_cleaner.py some_notebook.html clean_notebook.html
    New file: clean_notebook.html
    # Your cleaned-up report is ready :)
