"""This module contains setting to build PyPi packet """

from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='TickTickAPI',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://gitlab.com/barabass/tick',
    author='Akulinushkin Oleg',
    author_email='oleg.akulinishkin.01@mail.ru',
    python_requires=">=3.8",
    install_requires=[
        'requests==2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'tick = src.cli.tick_cli:main',
        ],
    }
)
