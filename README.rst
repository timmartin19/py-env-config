===============================
env-config
===============================


.. image:: https://img.shields.io/pypi/v/env_config.svg
        :target: https://pypi.python.org/pypi/env_config

.. image:: https://img.shields.io/travis/timmartin19/env_config.svg
        :target: https://travis-ci.org/timmartin19/env_config

.. image:: https://readthedocs.org/projects/env-config/badge/?version=latest
        :target: https://env-config.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/timmartin19/env_config/shield.svg
     :target: https://pyup.io/repos/github/timmartin19/env_config/
     :alt: Updates


A tool for configuring your application via environment variables


* Free software: MIT license
* Documentation: https://env-config.readthedocs.io.


Features
--------

Gets configuration from environment variables that start with
app_name optionally allowing you to load the environment variables
as json

    Example with load_as_json=True

    .. code-block:: python

        from env_config import get_envvar_configuration

        # Assuming that there are the following environment variables
        # MYAPP_BOOL=false
        # MYAPP_DICT={"some_key": "some_value"}
        # MYAPP_STRING=blahblahblah
        # NOTMYAPP_VARIABLE=this wont be recognized

        config = get_envvar_configuration('myapp')
        print(config)

        # prints out {'BOOL': False, 'DICT': {'some_key': 'some_value'}, 'STRING': 'blahblahblah'}

    Example with load_as_json=False

    .. code-block:: python

        config = get_envvar_configuration('myapp', load_as_json=False)
        print(config)

        # prints out {'BOOL': 'false', 'DICT': '{"some_key": "some_value"}', 'STRING': 'blahblahblah'}

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

