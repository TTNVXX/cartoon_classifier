# setup.py

from setuptools import setup, find_packages

setup(
    name='cartoon_classifier',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'transformers',
    ],
)
