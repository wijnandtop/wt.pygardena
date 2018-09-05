from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wt.pygardena',
    version='0.9.3',
    packages=['wt.pygardena'],
    url='https://github.com/wijnandtop/wt.pygardena',
    license='GNU General Public License v3.0',
    author='Wijnand Top',
    author_email='wijnand@bammes.nl',
    description='Library to connect to Garena Smart',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'objectpath',
    ]
)
