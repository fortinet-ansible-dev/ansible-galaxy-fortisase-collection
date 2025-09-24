#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_internal_reverse_policies
short_description: Internal Reverse Policy Resource
description:
  - Internal Reverse Policy Resource.
  - Use API "/resource-api/v2/security/internal-reverse-policies".
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
            enabled:
                type: bool
                description: no description
            scope:
                type: str
                description: no description
                choices:
                    - "all"
                    - "specify"
                    - "thin-edge"
                    - "vpn-user"
            sources:
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
                            - "network/host-groups"
                            - "network/hosts"
                            - "security/ip-threat-feeds"
            services:
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
                            - "security/service-groups"
                            - "security/services"
            action:
                type: str
                description: no description
                choices:
                    - "accept"
                    - "deny"
            schedule:
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
                            - "security/onetime-schedules"
                            - "security/recurring-schedules"
                            - "security/schedule-groups"
            comments:
                type: str
                description: no description
            profileGroup:
                type: dict
                description: no description
                suboptions:
                    group:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
                    forceCertInspection:
                        type: bool
                        description: no description
            logTraffic:
                type: str
                description: no description
                choices:
                    - "all"
                    - "disable"
                    - "utm"
            destinations:
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
                            - "infra/extenders"
                            - "infra/fortigates"
                            - "infra/ssids"
                            - "network/host-groups"
                            - "network/hosts"
"""

EXAMPLES = """
- name: Security internal reverse policies
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "reverse_policy_ansible"
  tasks:
    - name: Create/Update security internal reverse policies
      fortinet.fortisase.security_internal_reverse_policies:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          enabled: true
          scope: "vpn-user"
          services:
            - primaryKey: "SSH"
              datasource: "security/services"
            - primaryKey: "RDP"
              datasource: "security/services"
          action: "deny"
          logTraffic: "all"
          profileGroup:
            group:
              primaryKey: "internal"
              datasource: "security/profile-groups"
            forceCertInspection: false
          sources:
            - primaryKey: "gui_test"
              datasource: "network/hosts"
          schedule:
            primaryKey: "always"
            datasource: "security/recurring-schedules"
          comments: "Allow IT Admins remote access to machines of mobile workers"
    - name: Delete security internal reverse policies
      fortinet.fortisase.security_internal_reverse_policies:
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
    url = "/resource-api/v2/security/internal-reverse-policies"
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
                "scope": {"type": "str", "choices": ["all", "specify", "thin-edge", "vpn-user"]},
                "sources": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str", "choices": ["network/host-groups", "network/hosts", "security/ip-threat-feeds"]}
                    }
                },
                "services": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str", "choices": ["security/service-groups", "security/services"]}
                    }
                },
                "action": {"type": "str", "choices": ["accept", "deny"]},
                "schedule": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {
                            "type": "str",
                            "choices": ["security/onetime-schedules", "security/recurring-schedules", "security/schedule-groups"]
                        }
                    }
                },
                "comments": {"type": "str"},
                "profileGroup": {
                    "type": "dict",
                    "options": {
                        "group": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "forceCertInspection": {"type": "bool"}
                    }
                },
                "logTraffic": {"type": "str", "choices": ["all", "disable", "utm"]},
                "destinations": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {
                            "type": "str",
                            "choices": ["infra/extenders", "infra/fortigates", "infra/ssids", "network/host-groups", "network/hosts"]
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
