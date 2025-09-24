#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_dlp_profile
short_description: DLP Profile Resource
description:
  - DLP Profile Resource.
  - Use API "/resource-api/v2/security/dlp-profile/{direction}/{primaryKey}".
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
            direction:
                type: str
                required: true
                description: no description
            primaryKey:
                type: str
                required: true
                description: no description
            dlpRules:
                type: list
                description: no description
                elements: dict
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasourceType:
                        type: str
                        description: no description
                        choices:
                            - "fingerprint"
                            - "mpip-label"
                            - "none"
                            - "sensors"
                    severity:
                        type: str
                        description: no description
                        choices:
                            - "critical"
                            - "high"
                            - "informational"
                            - "low"
                            - "medium"
                    action:
                        type: str
                        description: no description
                        choices:
                            - "allow"
                            - "block"
                            - "monitor"
                    dlpRuleType:
                        type: str
                        description: no description
                        choices:
                            - "file"
                            - "message"
                    fileType:
                        type: str
                        description: no description
                        choices:
                            - "all"
                            - "specify"
                    protocols:
                        type: list
                        description: no description
                        elements: str
                    dlpSensors:
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
                    sensitivityLabel:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
                    sensitivities:
                        type: list
                        description: no description
                        elements: str
                    dlpFilePattern:
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
- name: Update security dlp profile
  hosts: fortisase
  gather_facts: false
  vars:
    direction: "outbound-profiles" # outbound-profiles or internal-profiles
    profile_group: "profile_ansible"
  tasks:
    - name: Ensure security group exists, otherwise create it
      fortinet.fortisase.security_profile_group:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
    - name: Update security dlp profile
      fortinet.fortisase.security_dlp_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          dlpRules: []
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
    url = "/resource-api/v2/security/dlp-profile/{direction}/{primaryKey}"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "direction": {"type": "str", "required": True, "only_in": ["url"]},
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "dlpRules": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasourceType": {"type": "str", "choices": ["fingerprint", "mpip-label", "none", "sensors"]},
                        "severity": {"type": "str", "choices": ["critical", "high", "informational", "low", "medium"]},
                        "action": {"type": "str", "choices": ["allow", "block", "monitor"]},
                        "dlpRuleType": {"type": "str", "choices": ["file", "message"]},
                        "fileType": {"type": "str", "choices": ["all", "specify"]},
                        "protocols": {"type": "list", "elements": "str"},
                        "dlpSensors": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "sensitivityLabel": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "sensitivities": {"type": "list", "elements": "str"},
                        "dlpFilePattern": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
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
        agent.process_ru(url)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
