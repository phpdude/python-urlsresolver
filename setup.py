#!/usr/bin/env python -u
from setuptools import setup, find_packages

setup(
    name='urlsresolver',
    version=".".join(map(str, __import__("urlsresolver").__version__)),
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
        'requests'
    ]
)
