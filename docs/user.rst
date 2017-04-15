.. _user:

User Guide
==========


Installation
------------

From PyPI with the Python package manager::

   pip install Annict



Quickstart
----------

Authentication
~~~~~~~~~~~~~~

Acquire the URL for acquiring the authentication code.

.. code:: python

    >>> from annict.auth import OAuthHandler
    >>> handler = OAuthHandler(client_id='your-client-id', client_secret='your-client-secret')
    >>> url = handler.get_authorization_url(scope='read write')
    >>> print(url)

Open the browser and access the URL you obtained, the authentication code will be displayed.
It will be passed to the `handler.authenticate()` 's argument to get the access token.

.. code:: python

    >>> handler.authenticate(code='your-authentication-code')
    >>> print(handler.get_access_token())

Note that this authentication flow is unnecessary when issuing a personal access token on Annict and using it.


API
~~~

.. code:: python

    >>> from annict.api import API
    >>> annict = API('your-access-token')
    >>> results = annict.works(filter_title="Re:ゼロから始める異世界生活")
    >>> print(results[0].title)
    Re:ゼロから始める異世界生活

The API class provides access to the entire Annict RESTful API methods.
Each method can accept various parameters and return responses.
For more information about these methods please refer to :ref:`API Reference <annict>`.


Models
~~~~~~

When we invoke an API method most of the time returned back to us will be a Annict model class instance.
This will contain the data returned from Annict which we can then use inside our application.
For example the following code returns to us an User model:

.. code:: python

   >>> user = api.me()

Models contain the data and some helper methods which we can then use:

.. code:: python

   >>> print(user.name)
   >>> print(user.records_count)
   >>> for follower in user.followers():
   ...     print(follower.username)
