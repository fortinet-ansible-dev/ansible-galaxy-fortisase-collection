#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: auth_ldap_servers
short_description: LDAP Resource
description:
  - LDAP Resource.
  - Use API "/resource-api/v2/auth/ldap-servers".
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
            server:
                type: str
                description: no description
            port:
                type: int
                description: no description
            cnid:
                type: str
                description: no description
            dn:
                type: str
                description: no description
            bindType:
                type: str
                description: no description
                choices:
                    - "anonymous"
                    - "regular"
                    - "simple"
            secureConnection:
                type: bool
                description: no description
            advancedGroupMatchingEnabled:
                type: bool
                description: no description
            groupMemberCheck:
                type: str
                description: no description
                choices:
                    - "group-object"
                    - "posix-group-object"
                    - "user-attr"
            memberAttribute:
                type: str
                description: no description
            groupFilter:
                type: str
                description: no description
            groupSearchBase:
                type: str
                description: no description
            groupObjectFilter:
                type: str
                description: no description
            serverIdentityCheckEnabled:
                type: bool
                description: no description
            passwordRenewalEnabled:
                type: bool
                description: no description
            certificate:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            clientCertAuthEnabled:
                type: bool
                description: no description
            clientCert:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            username:
                type: str
                description: no description
            password:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Auth LDAP Server
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "ldap_server_example"
  tasks:
    - name: Create/Update Auth LDAP Server
      fortinet.fortisase.auth_ldap_servers:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          server: "1.1.1.1"
          port: 1111
          cnid: "test"
          dn: "cn=admin,dc=example,dc=com"
          clientCertAuthEnabled: false
          bindType: "simple"
          secureConnection: false
          serverIdentityCheckEnabled: true
          advancedGroupMatchingEnabled: true
          groupMemberCheck: "user-attr"
          groupFilter: "cn=group,dc=example,dc=com"
          groupSearchBase: "dc=example,dc=com"
          certificate:
            primaryKey: "certificate"
            datasource: "system/certificate/ca-certificates"
    - name: Delete Auth LDAP Server
      fortinet.fortisase.auth_ldap_servers:
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
    url = "/resource-api/v2/auth/ldap-servers"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "server": {"type": "str"},
                "port": {"type": "int"},
                "cnid": {"type": "str"},
                "dn": {"type": "str"},
                "bindType": {"type": "str", "choices": ["anonymous", "regular", "simple"]},
                "secureConnection": {"type": "bool"},
                "advancedGroupMatchingEnabled": {"type": "bool"},
                "groupMemberCheck": {"type": "str", "choices": ["group-object", "posix-group-object", "user-attr"]},
                "memberAttribute": {"type": "str"},
                "groupFilter": {"type": "str"},
                "groupSearchBase": {"type": "str"},
                "groupObjectFilter": {"type": "str"},
                "serverIdentityCheckEnabled": {"type": "bool"},
                "passwordRenewalEnabled": {"type": "bool"},
                "certificate": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "clientCertAuthEnabled": {"type": "bool"},
                "clientCert": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "username": {"type": "str"},
                "password": {"type": "str", "no_log": True}
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
