.. annict documentation master file, created by
   sphinx-quickstart on Sat Apr 15 04:25:07 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Annict: Annict API wrapper for Python
=====================================

.. image:: https://img.shields.io/circleci/project/kk6/python-annict.svg
    :target: https://circleci.com/gh/kk6/python-annict

.. image:: https://img.shields.io/pypi/v/annict.svg
    :target: https://pypi.python.org/pypi/annict

Annict API wrapper for Python.

.. code:: python

    >>> from annict.api import API
    >>> annict = API('your-access-token')
    >>> results = annict.works(filter_title="Re:ゼロから始める異世界生活")
    >>> print(results[0].title)
    Re:ゼロから始める異世界生活


**annict** officially supports Python 3.6.

User Guide
----------

.. toctree::
   :maxdepth: 3

   user

API Reference
-------------

.. toctree::
   :maxdepth: 2

   annict


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
