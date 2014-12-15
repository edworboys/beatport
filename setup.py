#!/usr/bin/env python

from setuptools import setup

setup(
        name='beatport',
        version='0.0.1',
        description='Handles authentication for the Beatport API',
        url='https://github.com/jsakas/beatport',
        author='jsakas',
        author_email='jpsakas@gmail.com',
        install_requires=[
            'rauth','requests'
            ],
        py_modules=[
            'beatport'
            ],
        )
