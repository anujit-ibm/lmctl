import logging
from .sp_api_base import SitePlannerAPIGroup, SitePlannerCrudAPI
from .automation_context import AutomationContextAPIMixin
from lmctl.client.utils import read_response_location_header
from lmctl.client.exceptions import SitePlannerClientError
from typing import Dict, List


logger = logging.getLogger(__name__)

class ClusterGroupsAPI(SitePlannerCrudAPI, AutomationContextAPIMixin):
    _endpoint_chain = 'virtualization.cluster_groups'

    _object_type = 'virtualization.cluster_group'

class ClusterTypesAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.cluster_types'

    def get_by_name(self, name: str) -> Dict:
        override_url = self._pynb_endpoint.url + f'/?name={name}'
        resp = self._make_direct_http_call(
            verb='get',
            override_url=override_url,
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

class ClustersAPI(SitePlannerCrudAPI, AutomationContextAPIMixin):
    _endpoint_chain = 'virtualization.clusters'
    _relation_fields = ['type', 'group', 'tenant', 'site']

    _object_type = 'virtualization.cluster'

    def get_by_name(self, name: str) -> Dict:
        override_url = self._pynb_endpoint.url + f'/?name={name}'
        resp = self._make_direct_http_call(
            verb='get',
            override_url=override_url,
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

class InterfacesAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.interfaces'
    _relation_fields = ['virtual_machine', 'untagged_vlan', 'tagged_vlans']

class VirtualMachinesAPI(SitePlannerCrudAPI, AutomationContextAPIMixin):
    _endpoint_chain = 'virtualization.virtual_machines'
    _relation_fields = ['site', 'cluster', 'role', 'tenant', 'platform', 'primary_ip', 'primary_ip4', 'primary_ip6']

    _object_type = 'virtualization.virtualmachine'

    def get_by_name(self, name: str) -> Dict:
        override_url = self._pynb_endpoint.url + f'/?name={name}'
        resp = self._make_direct_http_call(
            verb='get',
            override_url=override_url,
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)


class CloudAccountTypesAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.cloudaccounttypes'

    def get_by_name(self, name: str) -> Dict:
        override_url = self._pynb_endpoint.url + f'/?name={name}'
        resp = self._make_direct_http_call(
            verb='get',
            override_url=override_url,
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)


class CloudAccountsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.cloudaccounts'

    def get_by_name(self, name: str) -> Dict:
        override_url = self._pynb_endpoint.url + f'/?name={name}'
        logger.info(f'CloudAccounts name={name} override_url={override_url}')
        resp = self._make_direct_http_call(
            verb='get',
            override_url=override_url,
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def build(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/build/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/teardown/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)


class AzureSubscriptionsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.azuresubscriptions'

    def get_by_name(self, name: str) -> Dict:
        override_url = self._pynb_endpoint.url + f'/?name={name}'
        logger.info(f'AzureSubscriptions name={name} override_url={override_url}')
        resp = self._make_direct_http_call(
            verb='get',
            override_url=override_url,
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def build(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/build/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/teardown/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)
    

class AzureLocationsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.azurelocations'

    def get_by_name(self, name: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?name={name}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    
class VPCsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.vpcs'

    def get_by_name(self, name: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?name={name}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def get_by_cloud_provider_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?cloud_account_id={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def get_by_configured_vpc_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?configured_vpc_id={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def get_by_cloud_provider_vpc_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?cloud_provider_vpc_id={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def build(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/build/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/teardown/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)


class VNetsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.vnets'

    def get_by_name(self, name: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?name={name}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def get_by_subscription_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?azure_subscription_id={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def get_by_configured_vnet_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?configured_vnet_id={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def get_by_cloud_provider_vnet_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?cloud_provider_vnet_id={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def build(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/build/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/teardown/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)
    
    
class AWSRegionsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.awsregions'
    
    def get_by_regionid(self, regionid: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?regionid={regionid}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on regionid: {regionid}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def get_by_name(self, name: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?name={name}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

class AWSTGWsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.awstgws'

    def get_by_name(self, name: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?name={name}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def get_by_awsregion(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?awsregion={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def get_by_awsaccount_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?awsaccount={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def build(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/build/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/teardown/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

class AWSTGWPeeringsAPI(SitePlannerCrudAPI):
    _endpoint_chain = 'virtualization.awstgwpeerings'

    def get_by_name(self, name: str) -> Dict:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?name={name}',
        ).json()
        count = resp.get('count', 0)
        if count == 0:
            return None
        if count > 1:
            raise SitePlannerClientError(f'Too many matches on name: {name}')
        results = resp.get('results', None)
        if results is None:
            return None
        obj = results[0]
        return self._record_to_dict(obj)

    def get_by_targettgw_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?target_tgw={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def get_by_sourcetgw_id(self, id: str) -> List:
        resp = self._make_direct_http_call(
            verb='get',
            override_url=self._pynb_endpoint.url + f'/?source_tgw={id}',
        ).json()
        return [self._record_to_dict(r) for r in resp.get('results', [])]

    def build(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/build/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)

    def teardown(self, id: str) -> str:
        response = self._make_direct_http_call(
            verb='post',
            override_url=self._pynb_endpoint.url + f'/{id}/teardown/',
            data={}
        )
        return read_response_location_header(response, error_class=SitePlannerClientError)
    
    
class VirtualizationGroup(SitePlannerAPIGroup):

    @property
    def cluster_groups(self):
        return ClusterGroupsAPI(self._sp_client)

    @property
    def cluster_types(self):
        return ClusterTypesAPI(self._sp_client)

    @property
    def clusters(self):
        return ClustersAPI(self._sp_client)

    @property
    def interfaces(self):
        return InterfacesAPI(self._sp_client)

    @property
    def virtual_machines(self):
        return VirtualMachinesAPI(self._sp_client)

    @property
    def cloud_account_types(self):
        return CloudAccountTypesAPI(self._sp_client)    

    @property
    def cloud_accounts(self):
        return CloudAccountsAPI(self._sp_client)    

    @property
    def vpcs(self):
        return VPCsAPI(self._sp_client)
    
    @property
    def azure_subscriptions(self):
        return AzureSubscriptionsAPI(self._sp_client)  
    
    @property
    def azure_locations(self):
        return AzureLocationsAPI(self._sp_client)    

    @property
    def vnets(self):
        return VNetsAPI(self._sp_client)
    
    @property
    def awsregions(self):
        return AWSRegionsAPI(self._sp_client)

    @property
    def awstgws(self):
        return AWSTGWsAPI(self._sp_client)

    @property
    def awstgwpeerings(self):
        return AWSTGWPeeringsAPI(self._sp_client)
    