#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: auth_user_groups
short_description: User Group Resource
description:
  - User Group Resource.
  - Use API "/resource-api/v2/auth/user-groups".
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
            groupType:
                type: str
                description: no description
                choices:
                    - "firewall"
                    - "fsso"
            localUsers:
                type: list
                description: no description
                elements: dict
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            remoteUserGroups:
                type: list
                description: no description
                elements: dict
                suboptions:
                    server:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
                                choices:
                                    - "auth/ldap-servers"
                                    - "auth/radius-servers"
                                    - "auth/swg-saml-server"
                                    - "auth/vpn-saml-server"
                    matches:
                        type: list
                        description: no description
                        elements: str
"""

EXAMPLES = """
- name: Auth User Groups
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "example_group"
  tasks:
    - name: Create/Update Auth User Groups
      fortinet.fortisase.auth_user_groups:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          groupType: "firewall"
          localUsers:
            - primaryKey: "example_user@example.com"
              datasource: "auth/users"
          remoteUserGroups:
            - server:
                primaryKey: "example_ldap_server"
                datasource: "auth/ldap-servers"
              matches: ["example_group"]
    - name: Delete Auth User Groups
      fortinet.fortisase.auth_user_groups:
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
    url = "/resource-api/v2/auth/user-groups"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "groupType": {"type": "str", "choices": ["firewall", "fsso"]},
                "localUsers": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "remoteUserGroups": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "server": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {
                                    "type": "str",
                                    "choices": ["auth/ldap-servers", "auth/radius-servers", "auth/swg-saml-server", "auth/vpn-saml-server"]
                                }
                            }
                        },
                        "matches": {"type": "list", "elements": "str"}
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
