from setuptools import setup

install_requires = ['docopt', 'beautifulsoup4']

readme = ""
with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='notebook_cleaner',
    version='0.1',
    description="Remove code from HTML files rendered from Jupyter notebooks",
    long_description=readme,
    url="https://github.com/RAvdek/notebook_cleaner",
    author="Russell Avdek",
    author_email="russell.avdek@gmail.com",
    license="MSD 2-Clause",
    keywords='ipython',
    install_requires=install_requires,
    packages=['notebook_cleaner'],
    entry_points = { 'console_scripts': ['notebook_cleaner = notebook_cleaner.notebook_cleaner:main'] }
)

