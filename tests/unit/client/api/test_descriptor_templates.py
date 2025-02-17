import unittest
import yaml
from unittest.mock import patch, MagicMock
from lmctl.client.api import DescriptorTemplatesAPI
from lmctl.client.client_request import TNCOClientRequest

class TestDescriptorTemplatesAPI(unittest.TestCase):

    def setUp(self):
        self.mock_client = MagicMock(kami_address='http://kami.example.com')
        self.descriptor_templates = DescriptorTemplatesAPI(self.mock_client)

    def test_all(self):
        mock_response = '- name: assembly-template::Test::1.0'
        self.mock_client.make_request.return_value = MagicMock(text=mock_response)
        response = self.descriptor_templates.all()
        self.assertEqual(response, [{'name': 'assembly-template::Test::1.0'}])
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='GET', endpoint='api/catalog/descriptorTemplates', headers={'Accept': 'application/yaml,application/json'}, override_address='http://kami.example.com'))

    def test_get(self):
        mock_response = 'name: assembly-template::Test::1.0'
        self.mock_client.make_request.return_value = MagicMock(text=mock_response)
        response = self.descriptor_templates.get('assembly-template::Test::1.0')
        self.assertEqual(response, {'name': 'assembly-template::Test::1.0'})
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='GET', endpoint='api/catalog/descriptorTemplates/assembly-template::Test::1.0', headers={'Accept': 'application/yaml,application/json'}, override_address='http://kami.example.com'))

    def test_create(self):
        obj = {'name': 'assembly-template::Test::1.0'}
        response = self.descriptor_templates.create(obj)
        self.assertIsNone(response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='POST', endpoint='api/catalog/descriptorTemplates', body=yaml.safe_dump(obj), headers={'Content-Type': 'application/yaml'}, override_address='http://kami.example.com'))

    def test_update(self):
        obj = {'name': 'assembly-template::Test::1.0'}
        response = self.descriptor_templates.update(obj)
        self.assertIsNone(response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='PUT', endpoint='api/catalog/descriptorTemplates/assembly-template::Test::1.0', body=yaml.safe_dump(obj), headers={'Content-Type': 'application/yaml'}, override_address='http://kami.example.com'))

    def test_delete(self):
        response = self.descriptor_templates.delete('assembly-template::Test::1.0')
        self.assertIsNone(response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='DELETE', endpoint='api/catalog/descriptorTemplates/assembly-template::Test::1.0', override_address='http://kami.example.com'))
    
    def test_render(self):
        mock_response = 'name: assembly::Result::1.0'
        self.mock_client.make_request.return_value = MagicMock(text=mock_response)
        render_request = {'properties': {'propA': 'valueA'}}
        response = self.descriptor_templates.render('assembly-template::Test::1.0', render_request)
        self.assertEqual(response, {'name': 'assembly::Result::1.0'})
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='POST', endpoint='api/catalog/descriptorTemplates/assembly-template::Test::1.0/render', body=yaml.safe_dump(render_request), headers={'Accept': 'application/yaml', 'Content-Type': 'application/yaml'}, override_address='http://kami.example.com'))

    def test_render_raw(self):
        mock_response = 'name: assembly::Result::1.0'
        self.mock_client.make_request.return_value = MagicMock(text=mock_response)
        render_request = {'properties': {'propA': 'valueA'}}
        response = self.descriptor_templates.render_raw('assembly-template::Test::1.0', render_request)
        self.assertEqual(response, mock_response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='POST', endpoint='api/catalog/descriptorTemplates/assembly-template::Test::1.0/render-raw', body=yaml.safe_dump(render_request), headers={'Accept': 'text/plain', 'Content-Type': 'application/yaml'}, override_address='http://kami.example.com'))
