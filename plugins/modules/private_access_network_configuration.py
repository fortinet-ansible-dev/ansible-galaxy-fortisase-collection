#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: private_access_network_configuration
short_description: Secure Private Access Resource
description:
  - Secure Private Access Resource.
  - Use API "/resource-api/v1/private-access/network-configuration".
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
            bgp_router_ids_subnet:
                type: str
                description:
                    - Available/unused subnet that can be used to assign loopback interface IP
                    - addresses used for BGP router IDs parameter on the FortiSASE security PoPs.
                    - /28 is the minimum subnet size.
            as_number:
                type: str
                description: Autonomous System Number (ASN).
            recursive_next_hop:
                type: bool
                description:
                    - BGP Recursive Routing.
                    - Enabling this setting allows for interhub connectivity.
                    - When use BGP design on-loopback this has to be enabled.
            sdwan_rule_enable:
                type: bool
                description:
                    - Hub Selection Method.
                    - Enabling this setting the highest priority service connection that meets minimum SLA requirements is selected.
                    - Otherwise BGP MED (Multi-Exit Discriminator) will be used.
            sdwan_health_check_vm:
                type: str
                description: Health Check IP. Must be provided when enable sdwan rule which used to obtain Jitter, latency and packet loss measurements.
            bgp_design:
                type: str
                description: BGP Routing Design.
                choices:
                    - "loopback"
                    - "overlay"
"""

EXAMPLES = """
- name: Private Access Network Configuration
  hosts: fortisase
  gather_facts: false
  tasks:
    - name: Create/Update Private Access Network Configuration
      fortinet.fortisase.private_access_network_configuration:
        state: present
        params:
          bgp_design: "loopback"
          bgp_router_ids_subnet: "172.1.0.0/24"
          as_number: "65400"
          sdwan_rule_enable: true
          sdwan_health_check_vm: "10.255.255.100"
          recursive_next_hop: true
    - name: Wait until the resource config_state is success
      fortinet.fortisase.fortisase_facts:
        selector: "private_access_network_configuration"
      register: result
      until: result.response.config_state == "success"
      retries: 15
      delay: 10

    # - name: Delete Private Access Network Configuration
    #   fortinet.fortisase.private_access_network_configuration:
    #     state: absent
    #     params: {}
    # - name: Wait until can't get the resource (result is empty)
    #   fortinet.fortisase.fortisase_facts:
    #     selector: "private_access_network_configuration"
    #   register: result
    #   until: result.response == {}
    #   retries: 15
    #   delay: 10
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
    url = "/resource-api/v1/private-access/network-configuration"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "bgp_router_ids_subnet": {"type": "str"},
                "as_number": {"type": "str"},
                "recursive_next_hop": {"type": "bool"},
                "sdwan_rule_enable": {"type": "bool"},
                "sdwan_health_check_vm": {"type": "str"},
                "bgp_design": {"type": "str", "only_in": ["create"], "choices": ["loopback", "overlay"]}
            }
        }
    }

    module = AnsibleModule(
        argument_spec=modify_argument_spec(src_arg_spec),
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module, src_arg_spec=src_arg_spec)
        agent.process_crud(url, mkey=None)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
