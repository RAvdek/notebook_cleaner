from setuptools import setup

install_requires = ['docopt', 'beautifulsoup4']

setup(
    name='notebook_cleaner',
    version='0.1.6',
    description="Remove code from HTML files rendered from Jupyter notebooks",
    url="https://github.com/RAvdek/notebook_cleaner",
    author="Russell Avdek",
    author_email="russell.avdek@gmail.com",
    license="MIT",
    keywords='ipython',
    install_requires=install_requires,
    packages=['notebook_cleaner'],
    entry_points = { 'console_scripts': ['notebook_cleaner = notebook_cleaner.notebook_cleaner:main'] },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.2',
       'Programming Language :: Python :: 3.3',
       'Programming Language :: Python :: 3.4',
    ],
)

