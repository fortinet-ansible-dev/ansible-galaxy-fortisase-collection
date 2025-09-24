#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: auth_users
short_description: User Resource
description:
  - User Resource.
  - Use API "/resource-api/v2/auth/users".
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
            authType:
                type: str
                description: no description
                choices:
                    - "ldap"
                    - "password"
            status:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            email:
                type: str
                description: no description
            password:
                type: str
                description: no description
            ldapServer:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
"""

EXAMPLES = """
- name: Auth users
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "user_example@example.com"
  tasks:
    - name: Create auth user
      fortinet.fortisase.auth_users:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"  # For SASE authenticated users, name must match email.
          authType: "password"
          password: "example_password"
          email: "{{ primaryKey }}"
          status: "enable"
    # Only status can be updated, trying to update other parameters will fail
    - name: Update auth user
      fortinet.fortisase.auth_users:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          status: "disable"
    - name: Delete auth user
      fortinet.fortisase.auth_users:
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
    url = "/resource-api/v2/auth/users"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "authType": {"type": "str", "choices": ["ldap", "password"]},
                "status": {"type": "str", "choices": ["disable", "enable"]},
                "email": {"type": "str"},
                "password": {"type": "str", "no_log": True},
                "ldapServer": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
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
