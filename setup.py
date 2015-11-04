#!/usr/bin/env python

from setuptools import setup


def parse_requirements(filename):
    return list(filter(lambda line: (line.strip())[0] != '#',
                      [line.strip() for line in open(filename).readlines()]))


requirements = parse_requirements('requirements.txt')

setup(
        name='beatport-api',
        version='0.0.1',
        description='Handles authentication for the Beatport API',
        url='https://github.com/jsakas/beatport',
        author='jsakas',
        author_email='jpsakas@gmail.com',
        license='MIT',
        install_requires=requirements,
        py_modules=[
            'beatport-api'
            ],
        )
