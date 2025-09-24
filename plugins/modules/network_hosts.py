#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: network_hosts
short_description: Host Resource
description:
  - Host Resource.
  - Use API "/resource-api/v2/network/hosts".
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
                type: str
                required: true
                description: no description
            type:
                type: str
                description: no description
                choices:
                    - "fqdn"
                    - "geography"
                    - "ipmask"
                    - "iprange"
            location:
                type: str
                description: no description
                choices:
                    - "external"
                    - "internal"
                    - "private-access"
                    - "unspecified"
            subnet:
                type: str
                description: no description
            startIp:
                type: str
                description: no description
            endIp:
                type: str
                description: no description
            fqdn:
                type: str
                description: no description
            countryId:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Network Host
  hosts: fortisase
  gather_facts: false
  vars:
    host: "network_host_example"
  tasks:
    - name: Create/Update Network Host
      fortinet.fortisase.network_hosts:
        state: present
        params:
          primaryKey: "{{ host }}"
          type: "ipmask"
          location: "internal"
          subnet: "192.168.4.0/24"
    - name: Delete Network Host
      fortinet.fortisase.network_hosts:
        state: absent
        params:
          primaryKey: "{{ host }}"
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
    url = "/resource-api/v2/network/hosts"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "type": {"type": "str", "choices": ["fqdn", "geography", "ipmask", "iprange"]},
                "location": {"type": "str", "choices": ["external", "internal", "private-access", "unspecified"]},
                "subnet": {"type": "str"},
                "startIp": {"type": "str"},
                "endIp": {"type": "str"},
                "fqdn": {"type": "str"},
                "countryId": {"type": "str"}
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
