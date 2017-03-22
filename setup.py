# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

tests_require = ['pytest',]

setup(
    name='annict',
    version='0.4.0',
    license="MIT",
    author="kk6",
    author_email="hiro.ashiya@gmail.com",
    url="https://github.com/kk6/python-annict",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'rauth',
        'requests-cache',
        'requests',
        'furl',
        'arrow',
    ],
    setup_requires=['pytest-runner',],
    tests_require=tests_require,
    extras_require={'testing': tests_require},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ],
)

