# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from annict import __version__

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

tests_require = ['pytest',]

setup(
    name='annict',
    version=__version__,
    description='Annict API for Python',
    long_description=readme,
    license="MIT",
    author="kk6",
    author_email="hiro.ashiya@gmail.com",
    url="https://github.com/kk6/python-annict",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'rauth>=0.7.3',
        'requests>=2.13.0',
        'furl>=1.0.0',
        'arrow>=0.10.0',
    ],
    setup_requires=['pytest-runner',],
    tests_require=tests_require,
    extras_require={'testing': tests_require},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ],
)

