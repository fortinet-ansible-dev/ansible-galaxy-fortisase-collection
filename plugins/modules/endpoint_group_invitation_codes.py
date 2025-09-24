#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: endpoint_group_invitation_codes
short_description: Group-Based Invitation Code Resource
description:
  - Group-Based Invitation Code Resource.
  - Use API "/resource-api/v2/endpoint/group-invitation-codes".
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
            expireDate:
                type: str
                description: no description
            groupAssignment:
                type: dict
                description: no description
                suboptions:
                    enabled:
                        type: bool
                        description: no description
                    group:
                        type: dict
                        description: no description
                        suboptions:
                            id:
                                type: int
                                description: no description
                            path:
                                type: str
                                description: no description
"""

EXAMPLES = """
- name: Endpoint group invitation codes
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "group1"
  tasks:
    - name: Create/Update endpoint group invitation codes
      fortinet.fortisase.endpoint_group_invitation_codes:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          expireDate: "2026-03-08T12:45:30Z"
          groupAssignment:
            enabled: true
            group:
              id: "1"
              path: "All Groups"
    - name: Delete endpoint group invitation codes
      fortinet.fortisase.endpoint_group_invitation_codes:
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
    url = "/resource-api/v2/endpoint/group-invitation-codes"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "expireDate": {"type": "str"},
                "groupAssignment": {
                    "type": "dict",
                    "no_log": False,
                    "options": {
                        "enabled": {"type": "bool"},
                        "group": {
                            "type": "dict",
                            "options": {
                                "id": {"type": "int"},
                                "path": {"type": "str"}
                            }
                        }
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
        agent.process_crud(url, mkey="primaryKey")
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
