import os
import sys
import json
import tempfile
import unittest
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from contextlib import contextmanager

# Import the raw source code in the python path
sys.path.insert(0, '../')
import src
from src import RootHandler
from src import BuildingHandler
from src import BuildingListHandler
from src.handlers import BaseHandler

EXAMPLE_RESULT_PROXY = [{'foo': 'bar'}]

class TestBaseHandler(TestCase):
    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))

    def test_to_json(self):
        mock_config = Mock()
        mock_db = Mock()
        x = BaseHandler(mock_config, mock_db)
        result = x._to_json(EXAMPLE_RESULT_PROXY)
        self.assertIsInstance(result, str)
        with self.assertNotRaises(Exception):
            json.loads(result)

class TestRootHandler(TestCase):
    def test_response_passthrough(self):
        mock_config = Mock()
        mock_db = Mock()
        mock_req = Mock()
        mock_resp = Mock()
        # Execute the tested unit
        x = RootHandler(mock_config, mock_db)
        resp = x.on_get(mock_req, mock_resp)
        # Call our assertions
        self.assertTrue(resp is mock_resp)
        self.assertIsNotNone(resp.body)
        self.assertIsNotNone(resp.status)
        self.assertIsNotNone(resp.content_type)

class TestBuildingHandler(TestCase):
    @patch('src.handlers.BaseHandler._to_json')
    def test_response_passthrough(self, patch_func):
        mock_config = Mock()
        mock_db = Mock()
        mock_req = Mock()
        mock_resp = Mock()
        # Execute the tested unit
        x = BuildingHandler(mock_config, mock_db)
        resp = x.on_get(mock_req, mock_resp, 2)
        # Call our assertions
        self.assertTrue(resp is mock_resp)
        self.assertTrue(patch_func.called)
        self.assertIsNotNone(resp.body)
        self.assertIsNotNone(resp.status)
        self.assertIsNotNone(resp.content_type)

class TestBuildingListHandler(TestCase):
    @patch('src.handlers.BaseHandler._to_json')
    def test_response_passthrough(self, mocked_to_json):
        mock_config = Mock()
        mock_db = Mock()
        mock_req = Mock()
        mock_resp = Mock()
        # Execute the tested unit
        x = BuildingListHandler(mock_config, mock_db)
        resp = x.on_get(mock_req, mock_resp)
        # Call our assertions
        self.assertTrue(resp is mock_resp)
        self.assertTrue(mocked_to_json.called)
        self.assertIsNotNone(resp.body)
        self.assertIsNotNone(resp.status)
        self.assertIsNotNone(resp.content_type)

EXAMPLE_YAML = """
foo:
  bar: baz
  qux:
   - quux
   - corge
"""

# TIL: https://stackoverflow.com/a/424620
EXAMPLE_DICT = {
    'foo': {
        'bar': 'baz',
        'qux': [
            'quux',
            'corge'
        ]
    }
}

class TestWsgiLoadConfig(TestCase):
    def test_open_success(self):
        tfile = tempfile.NamedTemporaryFile(mode='w', delete=False)
        tfile.write(EXAMPLE_YAML)
        tfile.close()
        # Excute the tested unit
        (cfg_success, cfg_result) = src.wsgi._load_config(tfile.name)
        os.remove(tfile.name)
        # Call our assertions
        self.assertTrue(cfg_success)
        self.assertIsInstance(cfg_result, dict)
        self.assertEqual(cfg_result, EXAMPLE_DICT)

    # Other tests that I **could** write if I dedicated the energy to it
    # def test_open_fails(self):
    #     pass

    # def test_yaml_parse_error(self):
    #     pass