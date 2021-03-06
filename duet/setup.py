
NAME = 'aoc-duet'
VERSION = '0.1.0'
DESCRIPTION = 'AoC 2017 Duet VM Assembler'
AUTHOR = 'Pavel paiv Ivashkov'
LICENSE = 'MIT'
URL = 'https://github.com/paiv/aoc2017'


from setuptools import setup

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license=LICENSE,
    url=URL,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=['duet'],

    python_requires='>=3.6',
    install_requires=['Jinja2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    entry_points={
        'console_scripts': [
            'duet=duet.cli:cli'
        ]
    },
)
