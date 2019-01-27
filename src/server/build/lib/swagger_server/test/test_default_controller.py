# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.move import Move  # noqa: E501
from swagger_server.models.opening import Opening  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_moves_get(self):
        """Test case for moves_get

        Get moves for the given position
        """
        data = dict(fen='fen_example',
                    legal=true,
                    flags='flags_example')
        response = self.client.open(
            '/api/v1/moves',
            method='GET',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_openings_get(self):
        """Test case for openings_get

        Get all ECO openings
        """
        response = self.client.open(
            '/api/v1/openings',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_openings_id_get(self):
        """Test case for openings_id_get

        Get an opening and its variants by id
        """
        response = self.client.open(
            '/api/v1/openings/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
