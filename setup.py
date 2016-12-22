from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()
    
    
setup(
    name = 'DuckDuckGo Python3 Library',
    version = '1.0',
    description = 'A Python3 library for DuckDuckGo instant answer API and full search via browser.',
    long_description = long_description,
    author = 'Abhishek Poonia',
    author_email = 'abhishekpoonia22@gmail.com',
    license = 'GNU AFFERO GENERAL PUBLIC LICENSE',
    
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.5',
    ],
    
    keywords = ['web search', 'web scraping', 'DuckDuckGo'],
    
)
    

