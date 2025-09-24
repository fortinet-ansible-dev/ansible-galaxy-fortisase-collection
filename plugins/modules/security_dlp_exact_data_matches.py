#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_dlp_exact_data_matches
short_description: DLP Exact Data Match Resource
description:
  - DLP Exact Data Match Resource.
  - Use API "/resource-api/v2/security/dlp-exact-data-matches".
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
            externalResourceData:
                type: dict
                description: no description
                suboptions:
                    resource:
                        type: str
                        description: no description
                    refreshRate:
                        type: int
                        description: no description
                    username:
                        type: str
                        description: no description
                    password:
                        type: str
                        description: no description
                    updateMethod:
                        type: str
                        description: no description
                        choices:
                            - "feed"
                            - "push"
            columns:
                type: list
                description: no description
                elements: dict
                suboptions:
                    index:
                        type: int
                        description: no description
                    type:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
                    optional:
                        type: bool
                        description: no description
            optionalCount:
                type: int
                description: no description
"""

EXAMPLES = """
- name: Security DLP Exact Data Matches
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "asbmatches"
  tasks:
    - name: Create/Update Security DLP Exact Data Matches
      fortinet.fortisase.security_dlp_exact_data_matches:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          externalResourceData:
            resource: "https://example-resource.com"
            username: "admin"
            password: "password123"
            refreshRate: 3600
            updateMethod: "feed"
          optionalCount: 0
          columns:
            - index: 1
              optional: false
              type:
                datasource: "security/dlp-data-types"
                primaryKey: "credit-card"
    - name: Delete Security DLP Exact Data Matches
      fortinet.fortisase.security_dlp_exact_data_matches:
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
    url = "/resource-api/v2/security/dlp-exact-data-matches"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "externalResourceData": {
                    "type": "dict",
                    "options": {
                        "resource": {"type": "str"},
                        "refreshRate": {"type": "int"},
                        "username": {"type": "str"},
                        "password": {"type": "str", "no_log": True},
                        "updateMethod": {"type": "str", "choices": ["feed", "push"]}
                    }
                },
                "columns": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "index": {"type": "int"},
                        "type": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "optional": {"type": "bool"}
                    }
                },
                "optionalCount": {"type": "int"}
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
