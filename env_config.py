from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os


def get_envvar_configuration(app_name, load_as_json=True):
    """
    Gets configuration from environment variables that start with
    app_name

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

    :param unicode app_name: The name of the application,
        this will be uppercased and used as the prefix for
        the environment variables.  Basically if you pass in ``'app'``
        any environment variable that starts with 'APP_' will be considered
        part of the configuration
    :param bool load_as_json: Indicates whether the values of the
        configuration should be read in as JSON.  If it cannot
        read it as json it will ignore the error and assign
        the key as the original value
    :return: A dictionary of the configuration for the application
    :rtype: dict
    """
    configuration = {}
    prefix = '{0}_'.format(app_name.upper())
    for key, value in os.environ.items():
        if key.startswith(prefix):
            config_name = key[len(prefix):]
            configuration[config_name] = value
    if load_as_json:
        return _read_as_json(configuration)
    return configuration


def _read_as_json(configuration):
    """
    Attempts to read all of the values
    in the configuration dictionary as json
    string.  If it fails, it just uses the original value

    :param dict configuration: Raw configuration
    :return: Json loaded configuration
    :rtype: dict
    """
    new_config = {}
    for key, value in configuration.items():
        try:
            value = json.loads(value)
        except (ValueError, TypeError):
            pass
        new_config[key] = value
    return new_config

