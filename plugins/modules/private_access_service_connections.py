#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: private_access_service_connections
short_description: Secure Private Access Resource
description:
  - Secure Private Access Resource.
  - Use API "/resource-api/v1/private-access/service-connections".
version_added: "1.0.0"
author:
    - Xinwei Du (@dux-fortinet)
options:
    state:
        description: The state of the module. "present" means create or update the resource, "absent" means delete the resource.
        type: str
        choices: [ present, absent ]
        default: present
    force_behavior:
        description: Specify this option to force the method to use to interact with the resource.
        type: str
        choices: [ none, read, create, update, delete ]
        default: none
    bypass_validation:
        description: Bypass validation of the module.
        type: bool
        default: false
    params:
        description: The parameters of the module.
        type: dict
        required: true
        suboptions:
            service_connection_id:
                type: str
                required: true
                description: no description
            alias:
                type: str
                description: alias for serivce connection
            bgp_peer_ip:
                type: str
                description: BGP Routing Peer IP.
            ipsec_remote_gw:
                type: str
                description: IPSEC Remote Gateway IP
            overlay_network_id:
                type: str
                description: integer id for overlay
            route_map_tag:
                type: str
                description: route map tag
            auth:
                type: str
                description: IPSEC authentication method
                choices:
                    - "pki"
                    - "psk"
            ipsec_pre_shared_key:
                type: str
                description: IPSEC auth by pre shared key.
            ipsec_cert_name:
                type: str
                description: the name of IPSEC authentication certificate that uploaded to SASE
            ipsec_ike_version:
                type: str
                description: IKE version for IPSEC
                choices:
                    - "2"
            ipsec_peer_name:
                type: str
                description: Peer PKI user name that created on SASE for IPSEC authentication
            backup_links:
                type: list
                description: no description
                elements: dict
                suboptions:
                    alias:
                        type: str
                        description: alias for serivce connection additional overlay
                    auth:
                        type: str
                        description: IPSEC authentication method
                        choices:
                            - "pki"
                            - "psk"
                    ipsec_cert_name:
                        type: str
                        description: the name of IPSEC authentication certificate that uploaded to SASE
                    ipsec_ike_version:
                        type: str
                        description: IKE version for IPSEC
                        choices:
                            - "2"
                    ipsec_peer_name:
                        type: str
                        description: Peer PKI user name that created on SASE for IPSEC authentication
                    ipsec_remote_gw:
                        type: str
                        description: IPSEC Remote Gateway IP
                    overlay_network_id:
                        type: str
                        description: integer id for overlay
                    ipsec_pre_shared_key:
                        type: str
                        description: IPSEC auth by pre shared key.
            type:
                type: str
                description: BGP Routing Design. Must be same as network configuration.
                choices:
                    - "loopback"
                    - "overlay"
            region_cost:
                type: dict
                description: Cost value to determine the priority of SASE spokes. Default cost is 5 if not provided through initial api request.
                suboptions:
                    sjc_f1:
                        type: int
                        description: no description
                    lon_f1:
                        type: int
                        description: no description
                    fra_f1:
                        type: int
                        description: no description
                    iad_f1:
                        type: int
                        description: no description
"""

EXAMPLES = """
- name: Private Access Service Connections
  hosts: fortisase
  gather_facts: false
  tasks:
    # !!!! private_access_network_configuration has to be created first
    # - name: Create/Update Private Access Network Configuration
    #   fortinet.fortisase.private_access_network_configuration:
    #     state: present
    #     params:
    #       bgp_design: "loopback"
    #       bgp_router_ids_subnet: "172.1.0.0/24"
    #       as_number: "65400"
    #       sdwan_rule_enable: true
    #       sdwan_health_check_vm: "10.255.255.100"
    #       recursive_next_hop: true
    # - name: Wait until the resource config_state is success
    #   fortinet.fortisase.fortisase_facts:
    #     selector: "private_access_network_configuration"
    #   register: result
    #   until: result.response.config_state == "success"
    #   retries: 15
    #   delay: 10

    - name: Create Private Access Service Connections
      fortinet.fortisase.private_access_service_connections:
        state: present
        params:
          service_connection_id: "placeholder, not in use in create"
          type: "loopback"
          alias: "AWS-Ireland-Primary"
          ipsec_remote_gw: "1.1.1.1"
          ipsec_ike_version: "2"
          auth: "psk"
          ipsec_pre_shared_key: "example_shared_key"
          route_map_tag: "100"
          bgp_peer_ip: "10.255.255.100"
          overlay_network_id: "100"
      register: create_result
    - name: Wait until the resource config_state in create_result is success
      fortinet.fortisase.fortisase_facts:
        selector: "private_access_service_connections"
        params:
          service_connection_id: "{{ create_result.response.id }}"
      register: result
      until: result.response.config_state == "success" or result.response.config_state == "failed"
      retries: 15
      delay: 10
      failed_when: result.response.config_state != "success"

    - name: Update Private Access Service Connections
      fortinet.fortisase.private_access_service_connections:
        state: present
        params:
          service_connection_id: "{{ create_result.response.id }}"
          ipsec_remote_gw: "1.1.1.2"
      register: update_result
    - name: Wait until the resource config_state in update_result is success
      fortinet.fortisase.fortisase_facts:
        selector: "private_access_service_connections"
        params:
          service_connection_id: "{{ update_result.response.id }}"
      register: result
      until: result.response.config_state == "success" or result.response.config_state == "failed"
      retries: 15
      delay: 10
      failed_when: result.response.config_state != "success"

    - name: Delete Private Access Service Connections
      fortinet.fortisase.private_access_service_connections:
        state: absent
        params:
          service_connection_id: "{{ create_result.response.id }}"
    - name: Wait until return error 403 (deleted successfully)
      fortinet.fortisase.fortisase_facts:
        selector: "private_access_service_connections"
        params:
          service_connection_id: "{{ create_result.response.id }}"
      register: result
      until: result.http_code == 403
      retries: 15
      delay: 10
      failed_when: false  # Never fail, regardless of HTTP 403 error
"""

RETURN = """
http_code:
    description: The HTTP code of the response.
    type: int
    returned: always
response:
    description: The response of the API.
    type: raw
    returned: always
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortisase.plugins.module_utils.fortisase import FortiSASEAPI, modify_argument_spec


def main():
    url = "/resource-api/v1/private-access/service-connections"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "service_connection_id": {"type": "str", "required": True, "only_in": ["url"], "api_name": "service-connection-id"},
                "alias": {"type": "str"},
                "bgp_peer_ip": {"type": "str"},
                "ipsec_remote_gw": {"type": "str"},
                "overlay_network_id": {"type": "str"},
                "route_map_tag": {"type": "str"},
                "auth": {"type": "str", "choices": ["pki", "psk"]},
                "ipsec_pre_shared_key": {"type": "str", "no_log": True},
                "ipsec_cert_name": {"type": "str"},
                "ipsec_ike_version": {"type": "str", "choices": ["2"]},
                "ipsec_peer_name": {"type": "str"},
                "backup_links": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "alias": {"type": "str"},
                        "auth": {"type": "str", "choices": ["pki", "psk"]},
                        "ipsec_cert_name": {"type": "str"},
                        "ipsec_ike_version": {"type": "str", "choices": ["2"]},
                        "ipsec_peer_name": {"type": "str"},
                        "ipsec_remote_gw": {"type": "str"},
                        "overlay_network_id": {"type": "str"},
                        "ipsec_pre_shared_key": {"type": "str", "no_log": True}
                    }
                },
                "type": {"type": "str", "only_in": ["create"], "choices": ["loopback", "overlay"]},
                "region_cost": {
                    "type": "dict",
                    "only_in": ["create"],
                    "options": {
                        "sjc_f1": {"type": "int", "api_name": "sjc-f1"},
                        "lon_f1": {"type": "int", "api_name": "lon-f1"},
                        "fra_f1": {"type": "int", "api_name": "fra-f1"},
                        "iad_f1": {"type": "int", "api_name": "iad-f1"}
                    }
                }
            }
        }
    }

    module = AnsibleModule(
        argument_spec=modify_argument_spec(src_arg_spec),
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module, src_arg_spec=src_arg_spec)
        agent.process_crud(url, mkey="service_connection_id")
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
