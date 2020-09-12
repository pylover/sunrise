
from setuptools import setup, find_packages
import os.path
import re


dependencies = [
    'pymlconf',
]


setup(
    name='sunrise',
    version='0.1.0',
    author='Vahid Mardani',
    author_email='vahid.mardani@gmail.com',
    url='http://github.com/pylover/sunrise',
    description='A simple persian text-bot.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important!
    install_requires=dependencies,
    packages=find_packages(exclude=['tests']),
    license='MIT',
    # TODO: Add calssifiers.
)
