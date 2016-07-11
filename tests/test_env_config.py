#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_env_config
----------------------------------

Tests for `env_config` module.
"""

from os import environ
import unittest2

from env_config import get_envvar_configuration, _read_as_json


class TestEnvConfig(unittest2.TestCase):
    def test_read_as_json__when_invalid_json__returns_original(self):
        original = {'something': 'notjson'}
        resp = _read_as_json(original)
        self.assertDictEqual(original, resp)

        original = {'something': 1}
        resp = _read_as_json(original)
        self.assertDictEqual(original, resp)

    def test_read_as_json__when_valid_json_dict__returns_json_dict(self):
        original = {'something': '{"x": 1}'}
        resp = _read_as_json(original)
        expected = {'something': {'x': 1}}
        self.assertDictEqual(expected, resp)

    def test_read_as_json__when_valid_int__returns_json_loaded_dict(self):
        original = {'something': '1'}
        resp = _read_as_json(original)
        self.assertDictEqual({'something': 1}, resp)

    def test_read_as_json__when_valid_bool__returns_json_loaded(self):
        original = {'something': 'false'}
        resp = _read_as_json(original)
        self.assertDictEqual({'something': False}, resp)

    def test_get_envvar_configuration__ignores_incorrect_envvars(self):
        resp = get_envvar_configuration('myapp')
        self.assertDictEqual({}, resp)

    def test_get_envvar_configuration__retrieves_valid_envvars(self):
        environ['MYAPP_SOMETHING'] = 'blah'
        resp = get_envvar_configuration('myapp')
        self.assertDictEqual({'SOMETHING': 'blah'}, resp)

    def test_getenvvar_configuration__when_load_as_json__loads_json(self):
        environ['MYAPP_SOMETHING'] = '{"x": 1}'
        resp = get_envvar_configuration('myapp')
        self.assertDictEqual({'SOMETHING': {'x': 1}}, resp)

    def test_getenvvar_configuration__when_not_load_as_json__not_load_json(self):
        environ['MYAPP_SOMETHING'] = '{"x": 1}'
        resp = get_envvar_configuration('myapp', load_as_json=False)
        self.assertDictEqual({'SOMETHING': '{"x": 1}'}, resp)
