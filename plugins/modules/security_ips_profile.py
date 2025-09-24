#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_ips_profile
short_description: IPS Profile Resource
description:
  - IPS Profile Resource.
  - Use API "/resource-api/v2/security/ips-profile/{direction}/{primaryKey}".
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
            profileType:
                type: str
                description: no description
                choices:
                    - "critical"
                    - "custom"
                    - "monitor"
                    - "recommended"
            customRuleGroups:
                type: list
                description: no description
                elements: dict
                suboptions:
                    action:
                        type: str
                        description: no description
                        choices:
                            - "allow"
                            - "block"
                            - "monitor"
                    signatures:
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
            isBlockingMaliciousUrl:
                type: bool
                description: no description
            botnetScanning:
                type: str
                description: no description
                choices:
                    - "block"
                    - "disable"
                    - "monitor"
            isExtendedLogEnabled:
                type: bool
                description: no description
            comment:
                type: str
                description: no description
            entries:
                type: list
                description: no description
                elements: dict
                suboptions:
                    rule:
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
                                choices:
                                    - "security/ips-custom-signatures"
                                    - "security/ips-rule"
                    location:
                        type: str
                        description: no description
                    severity:
                        type: str
                        description: no description
                    protocol:
                        type: str
                        description: no description
                    os:
                        type: str
                        description: no description
                    application:
                        type: str
                        description: no description
                    cve:
                        type: list
                        description: no description
                        elements: str
                    status:
                        type: str
                        description: no description
                        choices:
                            - "default"
                            - "disable"
                            - "enable"
                    log:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    logPacket:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    logAttackContext:
                        type: str
                        description: no description
                    action:
                        type: str
                        description: no description
                        choices:
                            - "block"
                            - "default"
                            - "pass"
                    vulnType:
                        type: list
                        description: no description
                        elements: dict
                        suboptions:
                            id:
                                type: int
                                description: no description
                    quarantine:
                        type: str
                        description: no description
                    exempt_ip:
                        type: list
                        description: no description
                        elements: dict
                        suboptions:
                            id:
                                type: int
                                description: no description
                            src_ip:
                                type: str
                                description: no description
                            dst_ip:
                                type: str
                                description: no description
                    defaultAction:
                        type: str
                        description: no description
                        choices:
                            - "all"
                            - "block"
                            - "pass"
                    defaultStatus:
                        type: str
                        description: no description
                        choices:
                            - "all"
                            - "disable"
                            - "enable"
"""

EXAMPLES = """
- name: Update security ips profile
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
    - name: Update security ips profile
      fortinet.fortisase.security_ips_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          botnetScanning: "block"
          comment: "Recommended"
          customRuleGroups: []
          entries:
            - action: "default"
              application: "all"
              cve: []
              defaultAction: "all"
              defaultStatus: "all"
              exempt_ip: []
              location: "all"
              log: "enable"
              logAttackContext: "disable"
              logPacket: "disable"
              os: "all"
              protocol: "all"
              quarantine: "none"
              rule: []
              severity: "all"
              status: "default"
              vulnType: []
          isBlockingMaliciousUrl: false
          isExtendedLogEnabled: false
          profileType: "recommended"
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
    url = "/resource-api/v2/security/ips-profile/{direction}/{primaryKey}"
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
                "profileType": {"type": "str", "choices": ["critical", "custom", "monitor", "recommended"]},
                "customRuleGroups": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "monitor"]},
                        "signatures": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "isBlockingMaliciousUrl": {"type": "bool"},
                "botnetScanning": {"type": "str", "choices": ["block", "disable", "monitor"]},
                "isExtendedLogEnabled": {"type": "bool"},
                "comment": {"type": "str"},
                "entries": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "rule": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str", "choices": ["security/ips-custom-signatures", "security/ips-rule"]}
                            }
                        },
                        "location": {"type": "str"},
                        "severity": {"type": "str"},
                        "protocol": {"type": "str"},
                        "os": {"type": "str"},
                        "application": {"type": "str"},
                        "cve": {"type": "list", "elements": "str"},
                        "status": {"type": "str", "choices": ["default", "disable", "enable"]},
                        "log": {"type": "str", "choices": ["disable", "enable"]},
                        "logPacket": {"type": "str", "choices": ["disable", "enable"]},
                        "logAttackContext": {"type": "str"},
                        "action": {"type": "str", "choices": ["block", "default", "pass"]},
                        "vulnType": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "id": {"type": "int"}
                            }
                        },
                        "quarantine": {"type": "str"},
                        "exempt_ip": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "id": {"type": "int"},
                                "src_ip": {"type": "str", "api_name": "src-ip"},
                                "dst_ip": {"type": "str", "api_name": "dst-ip"}
                            },
                            "api_name": "exempt-ip"
                        },
                        "defaultAction": {"type": "str", "choices": ["all", "block", "pass"]},
                        "defaultStatus": {"type": "str", "choices": ["all", "disable", "enable"]}
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
