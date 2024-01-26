#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines unit test class for client.
"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for GithubOrgClient.
    """

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, org_url: str,
                 mock_method: MagicMock) -> None:
        """Test org method.
        """
        client = GithubOrgClient(org)
        client.org()
        mock_method.assert_called_once_with(org_url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock,
           return_value={
                'repos_url': "https://api.github.com/orgs/example_org/repos"})
    def test_public_repos_url(self, _: MagicMock) -> None:
        """Test _public_repos_url.
        """
        client = GithubOrgClient("example")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/example_org/repos")


if __name__ == "__main__":
    unittest.main()
