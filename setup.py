import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='wt.pygardena',
    version='0.9.5',
    packages=setuptools.find_packages(),
    url='https://github.com/wijnandtop/wt.pygardena',
    license='Apache License 2.0',
    author='Wijnand Top',
    author_email='wijnand@bammes.nl',
    description='Library to connect to Garena Smart',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.4",
    install_requires=[
        'objectpath',
        'requests',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    tests_require = ['requests-mock']
)
