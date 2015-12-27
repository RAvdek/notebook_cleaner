"""
Sample script which uses the notebook_cleaner function
"""

import notebook_cleaner as nc

SAMPLE_IN = "sample_notebook.html"
SAMPLE_OUT = "script_clean_notebook.html"

if __name__ == "__main__":
    nc.notebook_cleaner(SAMPLE_IN, SAMPLE_OUT)
