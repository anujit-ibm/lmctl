from typing import Dict, Union
from .sp_api_base import SitePlannerAPIGroup, SitePlannerCrudAPI, SitePlannerAPI, SitePlannerGetMixin, SitePlannerDeleteMixin, SitePlannerListMixin
from .utils import make_call, check_response_and_get_json, check_response
from lmctl.client.utils import read_response_location_header, read_response_body_as_json
from lmctl.client.exceptions import SitePlannerClientError
from pynetbox.core.query import Request

class AutomationContextProcessesAPI(SitePlannerAPI, SitePlannerGetMixin, SitePlannerDeleteMixin, SitePlannerListMixin):
    _endpoint_chain = 'plugins.nfvi-automation.automation_context_processes'
    

class AutomationContextsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'plugins.nfvi-automation.automation_contexts'

    def build(self, object_type: str, object_pk: str) -> str:
        return self._build(object_type, object_pk, dry_run=False)

    def build_dry_run(self, object_type: str, object_pk: str) -> Dict:
        return self._build(object_type, object_pk, dry_run=True)

    def _build(self, object_type: str, object_pk: str, dry_run: bool = False) -> Union[str, Dict]:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + '/build/',
            data={
                'object_type': object_type,
                'object_pk': object_pk,
                'dry_run': dry_run
            }
        )
        if dry_run:
            return read_response_body_as_json(response, error_class=SitePlannerClientError)
        else:
            return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, object_type: str, object_pk: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + '/teardown/',
            data={
                'object_type': object_type,
                'object_pk': object_pk
            }
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

class AutomationContextAPIMixin:
    """
    To be used with an instance of sp_api_base.SitePlannerAPI to call build/teardown Automation Context APIs on a given object type
    """

    def _get_object_type(self):
        if hasattr(self, '_object_type'):
            return getattr(self, '_object_type')
        else:
            return self._endpoint_chain

    def build(self, id: str) -> str:
        return AutomationContextsAPI(self._sp_client).build(object_type=self._get_object_type(), object_pk=id)

    def build_dry_run(self, id: str) -> Dict:
        return AutomationContextsAPI(self._sp_client).build_dry_run(object_type=self._get_object_type(), object_pk=id)

    def teardown(self, id: str) -> str:
        return AutomationContextsAPI(self._sp_client).teardown(object_type=self._get_object_type(), object_pk=id)