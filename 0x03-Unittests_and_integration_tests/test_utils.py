#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines TestAccessNestedMap class.
"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import requests
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for access_nested_map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               expected: int) -> None:
        """Test that method.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", ), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: tuple, key: str) -> None:
        """Test that a KeyError is raised.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{key}')", repr(cm.exception))


class TestGetJson(unittest.TestCase):
    """Unit test for get_json.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Test get_json.
        """
        get = Mock()
        get.json = Mock(return_value = test_payload)
        with patch.object(requests, 'get', return_value=get) as mock_method:
            self.assertEqual(get_json(test_url), test_payload)
        mock_method.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unit test for memoize.
    """

    def test_memoize(self) -> None:
        """Test memoize.
        """
        class TestClass:
            """TestClass of test_memoize.
            """

            def a_method(self) -> None:
                """a_method.
                """
                return 42

            @memoize
            def a_property(self) -> None:
                """a_property method.
                """
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
        mock_method.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
