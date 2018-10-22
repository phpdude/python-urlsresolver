#!/usr/bin/env python -u
from os import path
from setuptools import setup
from setuptools import find_packages

here = path.abspath(path.dirname(__file__))
__version__ = None
with open(path.join(here, 'urlsresolver', '__version.py')) as __version:
    exec(__version.read())

setup(
    name='urlsresolver',
    version=__version__,
    description='Python urls resolver library',
    author='Alexandr I. Shurigin',
    author_email='ya@helldude.ru',
    maintainer='Alexandr I. Shurigin',
    maintainer_email='ya@helldude.ru',
    url='https://github.com/phpdude/python-urlsresolver',
    packages=find_packages(),
    test_suite='tests',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Utilities"
    ],
    install_requires=[
        'requests',
        'future'
    ]
)
