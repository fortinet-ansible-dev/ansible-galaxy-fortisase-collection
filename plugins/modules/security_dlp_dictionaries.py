#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_dlp_dictionaries
short_description: DLP Dictionary Resource
description:
  - DLP Dictionary Resource.
  - Use API "/resource-api/v2/security/dlp-dictionaries".
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
            dictionaryType:
                type: str
                description: no description
                choices:
                    - "mip-label"
                    - "sensor"
            sensitivityLabelGuid:
                type: str
                description: no description
            entriesToEvaluate:
                type: str
                description: no description
                choices:
                    - "all"
                    - "any"
            entries:
                type: list
                description: no description
                elements: dict
                suboptions:
                    dlpDataType:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    repeat:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    pattern:
                        type: str
                        description: no description
                    caseSensitive:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
"""

EXAMPLES = """
- name: Security DLP Dictionaries
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "asbdictionaries"
  tasks:
    - name: Create/Update Security DLP Dictionaries
      fortinet.fortisase.security_dlp_dictionaries:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          dictionaryType: "sensor"
          entriesToEvaluate: "all"
          entries:
            - dlpDataType:
                primaryKey: "regex"
                datasource: "security/dlp-data-types"
              pattern: "string"
              status: "enable"
              repeat: "enable"
    - name: Delete Security DLP Dictionaries
      fortinet.fortisase.security_dlp_dictionaries:
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
    url = "/resource-api/v2/security/dlp-dictionaries"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "dictionaryType": {"type": "str", "choices": ["mip-label", "sensor"]},
                "sensitivityLabelGuid": {"type": "str"},
                "entriesToEvaluate": {"type": "str", "choices": ["all", "any"]},
                "entries": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "dlpDataType": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "repeat": {"type": "str", "choices": ["disable", "enable"]},
                        "pattern": {"type": "str"},
                        "caseSensitive": {"type": "str", "choices": ["disable", "enable"]}
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
