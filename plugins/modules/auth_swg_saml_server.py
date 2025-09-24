#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: auth_swg_saml_server
short_description: SWG User SSO Resource
description:
  - SWG User SSO Resource.
  - Use API "/resource-api/v2/auth/swg-saml-server".
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
            idpEntityId:
                type: str
                description: no description
            idpSignOnUrl:
                type: str
                description: no description
            idpLogOutUrl:
                type: str
                description: no description
            username:
                type: str
                description: no description
            groupName:
                type: str
                description: no description
            groupMatch:
                type: str
                description: no description
            spCert:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            idpCertificate:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            digestMethod:
                type: str
                description: no description
                choices:
                    - "sha1"
                    - "sha256"
            scimEnabled:
                type: bool
                description: no description
            scim:
                type: dict
                description: no description
                suboptions:
                    scimUrl:
                        type: str
                        description: no description
                    authMethod:
                        type: str
                        description: no description
                        choices:
                            - "token"
                    token:
                        type: str
                        description: no description
"""

EXAMPLES = """
- name: Auth SWG SAML Server
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "$sase-global"
  tasks:
    # To configure this resource, please enable proxy configuration.
    - name: Create/Update Auth SWG SAML Server
      fortinet.fortisase.auth_swg_saml_server:
        params:
          primaryKey: "{{ primaryKey }}"
          enabled: true
          digestMethod: "sha256"
          idpEntityId: "https://sts.windows.net/example/"
          idpSignOnUrl: "https://login.microsoftonline.com/example/saml2"
          idpLogOutUrl: "https://login.microsoftonline.com/example/saml2"
          idpCertificate:
            primaryKey: "certificate"
            datasource: "system/certificate/remote-certificates"
          username: "username"
          groupName: "group"
          groupMatch: ""
          spCert:
            primaryKey: "FortiSASE Default Certificate"
            datasource: "system/certificate/local-certificates"
          scimEnabled: false

    - name: Delete Auth SWG SAML Server
      fortinet.fortisase.auth_swg_saml_server:
        params:
          primaryKey: "{{ primaryKey }}"
          enabled: false
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
    url = "/resource-api/v2/auth/swg-saml-server"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "enabled": {"type": "bool"},
                "idpEntityId": {"type": "str"},
                "idpSignOnUrl": {"type": "str"},
                "idpLogOutUrl": {"type": "str"},
                "username": {"type": "str"},
                "groupName": {"type": "str"},
                "groupMatch": {"type": "str"},
                "spCert": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "idpCertificate": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "digestMethod": {"type": "str", "choices": ["sha1", "sha256"]},
                "scimEnabled": {"type": "bool"},
                "scim": {
                    "type": "dict",
                    "options": {
                        "scimUrl": {"type": "str"},
                        "authMethod": {"type": "str", "choices": ["token"]},
                        "token": {"type": "str", "no_log": True}
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
        agent.process_ru(url)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
