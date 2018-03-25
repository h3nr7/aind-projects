"""
# setup.py
"""

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

setup(
    name='aind-projects',
    version='0.1.0',
    description='AIND projects on github',
    long_description=README,
    author='Henry YP Ho',
    author_email='henryyp@monkiki.co',
    url='https://henryyp.github.io/aind-projects',
    packages=find_packages(exclude=('test', 'docs'))
)
