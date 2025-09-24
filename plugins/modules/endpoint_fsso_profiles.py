#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: endpoint_fsso_profiles
short_description: FSSO Profile Resource
description:
  - FSSO Profile Resource.
  - Use API "/resource-api/v2/endpoint/fsso-profiles/{primaryKey}".
version_added: "1.0.0"
author:
    - Xinwei Du (@dux-fortinet)
options:
    state:
        description: The state of the module. "present" means update the resource. This resource can't be deleted, and does not support "absent" state.
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
            enabled:
                type: bool
                description: no description
            preferEntraId:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            host:
                type: str
                description: no description
            port:
                type: int
                description: no description
            preSharedKey:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Update fsso profile
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "policy1"
  tasks:
    - name: Create a new endpoint profile, do nothing if the endpoint profile already exists
      fortinet.fortisase.endpoint_policies:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          enabled: true
    - name: Update fsso profile
      fortinet.fortisase.endpoint_fsso_profiles:
        params:
          primaryKey: "{{ primaryKey }}"
          port: 443
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
    url = "/resource-api/v2/endpoint/fsso-profiles/{primaryKey}"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "only_in": ["url"], "no_log": False},
                "enabled": {"type": "bool"},
                "preferEntraId": {"type": "str", "choices": ["disable", "enable"]},
                "host": {"type": "str"},
                "port": {"type": "int"},
                "preSharedKey": {"type": "str", "no_log": True}
            }
        }
    }

    module = AnsibleModule(
        argument_spec=modify_argument_spec(src_arg_spec),
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module, src_arg_spec=src_arg_spec)
        agent.process_ru(url)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
