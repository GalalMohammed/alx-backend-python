#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines unit test class for client.
"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
               'repos_url': "https://api.github.com/orgs/example/repos"})
    def test_public_repos_url(self, mock_method: MagicMock) -> None:
        """Test _public_repos_url.
        """
        client = GithubOrgClient("example")
        self.assertEqual(client._public_repos_url,
                         mock_method.return_value['repos_url'])

    @patch('client.get_json', return_value=[{'name': 'repo1'},
                                            {'name': 'repo2'}])
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test public_repos.
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value="https://api.github.com/orgs/example/repos")\
                as mock_url:
            client = GithubOrgClient("example")
            self.assertEqual(client.public_repos(), ['repo1', 'repo2'])
        mock_get_json.assert_called_once()
        mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: dict, license_key: str,
                         expected: bool) -> None:
        """Test has_license.
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.
    """

    @classmethod
    def setUpClass(cls):
        """Mock requests.get.
        """
        cls.get_patcher = patch('requests.get', 'json')
        cls.get_patcher.side_effect = [cls.org_payload, cls.repos_payload,
                                       cls.expected_repos, cls.apache2_repos]
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(self):
        """Stop patcher.
        """
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
