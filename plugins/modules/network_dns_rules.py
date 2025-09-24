#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: network_dns_rules
short_description: DNS Rule Resource
description:
  - DNS Rule Resource.
  - Use API "/resource-api/v2/network/dns-rules".
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
            primaryKey:
                type: int
                required: true
                description: no description
            primaryDns:
                type: str
                description: no description
            secondaryDns:
                type: str
                description: no description
            domains:
                type: list
                description: no description
                elements: str
            popDnsOverride:
                type: dict
                description: no description
            forPrivate:
                type: bool
                description: no description
"""

EXAMPLES = """
- name: Network DNS Rule
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "1"
  tasks:
    - name: Create/Update Network DNS Rule
      fortinet.fortisase.network_dns_rules:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          primaryDns: "1.1.1.1"
          secondaryDns: "1.1.1.2"
          domains:
            - www.facebook.com
            - www.google.com
          popDnsOverride: {}
    - name: Delete Network DNS Rule
      fortinet.fortisase.network_dns_rules:
        state: absent
        params:
          primaryKey: "{{ primaryKey }}"
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
    url = "/resource-api/v2/network/dns-rules"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "int", "required": True, "no_log": False},
                "primaryDns": {"type": "str"},
                "secondaryDns": {"type": "str"},
                "domains": {"type": "list", "elements": "str"},
                "popDnsOverride": {
                    "type": "dict",
                    "options": {
                    }
                },
                "forPrivate": {"type": "bool"}
            }
        }
    }

    module = AnsibleModule(
        argument_spec=modify_argument_spec(src_arg_spec),
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module, src_arg_spec=src_arg_spec)
        agent.process_crud(url, mkey="primaryKey")
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
