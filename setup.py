#!/usr/bin/python2
from distutils.core import setup
setup(name='Challenge',
	  version='1.0',
	  scripts=['AdamsChallenge.py'],
	  requires=['Flask (>0.10)','redis (>2.8)','hiredis (>0.1)'])