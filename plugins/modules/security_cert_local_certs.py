#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_cert_local_certs
short_description: Certificate Resource
description:
  - Certificate Resource.
  - Use API "/resource-api/v1/security/cert/local-certs".
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
            format:
                type: str
                description: no description
            certName:
                type: str
                description: no description
            password:
                type: str
                description: no description
            fileContent:
                type: str
                description: no description
            keyFileContent:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Security Certificate Local Certificates
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "example_certs"
  tasks:
    - name: Create/Update Security Certificate Local Certificates
      fortinet.fortisase.security_cert_local_certs:
        state: present
        params:
          format: "regular"
          primaryKey: "{{ primaryKey }}"
          certName: "{{ primaryKey }}"
          password: "fortinet"
          fileContent: "{{ lookup('file', 'server_cert.pem') | b64encode }}"
          keyFileContent: "{{ lookup('file', 'server_key.pem') | b64encode }}"
    - name: Delete Security Certificate Local Certificates
      fortinet.fortisase.security_cert_local_certs:
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
    url = "/resource-api/v1/security/cert/local-certs"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "only_in": ["delete"], "no_log": False},
                "format": {"type": "str", "only_in": ["create"]},
                "certName": {"type": "str", "only_in": ["create"]},
                "password": {"type": "str", "only_in": ["create"], "no_log": True},
                "fileContent": {"type": "str", "only_in": ["create"]},
                "keyFileContent": {"type": "str", "only_in": ["create"], "no_log": True}
            }
        }
    }

    module = AnsibleModule(
        argument_spec=modify_argument_spec(src_arg_spec),
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module, src_arg_spec=src_arg_spec)
        agent.process_crd(url, mkey="primaryKey")
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
