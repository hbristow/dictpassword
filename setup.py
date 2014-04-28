import os
import sys
import time
import subprocess
from setuptools import setup

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def read(file):
    """Read the contents of a file into a string"""
    with open(file, 'r') as f:
        return f.read()

# ----------------------------------------------------------------------------
# SETUP
# ----------------------------------------------------------------------------
setup(name='dictpassword',
    version='0.1',
    description='Cryptographically secure passphrase generator',
    long_description=read('README.md'),
    keywords='python password passphrase crypto entropy',
    url='https://github.com/hbristow/dictpassword/',
    author='Hilton Bristow',
    author_email='hilton.bristow+dictpassword@gmail.com',
    license='GPL',
    packages=['dictpassword'],
    package_data = {
        'dictpassword': [
            'common',
            'full'
        ]
    },
    entry_points = {
        'console_scripts': [
            'dictpassword = dictpassword.dictpassword:main'
        ]
    },
    zip_safe=False
)
