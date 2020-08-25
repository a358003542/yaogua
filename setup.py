#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
from setuptools import setup, find_packages
import yaogua

REQUIREMENTS = ['click','pyside2']

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yaogua',
    version=yaogua.__version__,
    description='a simple command line tool for zhouyi yaogua.',
    url='https://github.com/a358003542/yaogua',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer='wanze',
    maintainer_email='a358003542@gmail.com',
    license='MIT',
    platforms='Linux, windows',
    keywords=['zhouyi', 'python'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Operating System :: Microsoft',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': ['yaogua=yaogua.__main__:main', ],
        "gui_scripts": [
            "yaogua_gui = yaogua.gui:main",
        ]
    }
)
