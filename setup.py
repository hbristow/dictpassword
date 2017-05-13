#
# Dictpassword
#

import setuptools

#
# Dictpassword: Cryptographically secure passphrase generator.
#
setuptools.setup(name='dictpassword',
    version='1.0',
    description='Cryptographically secure passphrase generator',
    long_description=open('README.md').read(),
    keywords='python password passphrase crypto entropy',
    url='https://github.com/hbristow/dictpassword/',
    author='Hilton Bristow',
    author_email='hilton.bristow+dictpassword@gmail.com',
    license='BSD',
    packages=[
        'dictpassword'
    ],
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
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Security :: Cryptography',
    ],
    zip_safe=False
)
