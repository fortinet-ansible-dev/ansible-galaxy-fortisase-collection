#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_dlp_fingerprint_databases
short_description: DLP Fingerprint Database Resource
description:
  - DLP Fingerprint Database Resource.
  - Use API "/resource-api/v2/security/dlp-fingerprint-databases".
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
            sensitivity:
                type: str
                description: no description
                choices:
                    - "Critical"
                    - "Private"
                    - "Warning"
            includeSubdirectories:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            serverDirectory:
                type: str
                description: no description
            filePattern:
                type: str
                description: no description
            schedule:
                type: dict
                description: no description
                suboptions:
                    period:
                        type: str
                        description: no description
                        choices:
                            - "daily"
                            - "monthly"
                            - "weekly"
                    syncHour:
                        type: int
                        description: no description
                    syncMinute:
                        type: int
                        description: no description
                    weekday:
                        type: str
                        description: no description
                        choices:
                            - "friday"
                            - "monday"
                            - "saturday"
                            - "sunday"
                            - "thursday"
                            - "tuesday"
                            - "wednesday"
                    syncDayOfTheMonth:
                        type: int
                        description: no description
            removeDeletedFileFingerprints:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            keepModified:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            scanOnCreation:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            authentication:
                type: dict
                description: no description
                suboptions:
                    username:
                        type: str
                        description: no description
                    password:
                        type: str
                        description: no description
"""

EXAMPLES = """
- name: Security DLP Fingerprint Databases
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "asbdatabases"
  tasks:
    - name: Create/Update Security DLP Fingerprint Databases
      fortinet.fortisase.security_dlp_fingerprint_databases:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          server: "example-server.com"
          sensitivity: "Warning"
          includeSubdirectories: "enable"
          serverDirectory: "/path/to/directory/"
          filePattern: "*.txt"
          schedule:
            period: "daily"
            syncHour: 2
            syncMinute: 0
          removeDeletedFileFingerprints: "enable"
          keepModified: "enable"
          scanOnCreation: "enable"
          authentication:
            username: "admin"
            password: "password123"
    - name: Delete Security DLP Fingerprint Databases
      fortinet.fortisase.security_dlp_fingerprint_databases:
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
    url = "/resource-api/v2/security/dlp-fingerprint-databases"
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
                "sensitivity": {"type": "str", "choices": ["Critical", "Private", "Warning"]},
                "includeSubdirectories": {"type": "str", "choices": ["disable", "enable"]},
                "serverDirectory": {"type": "str"},
                "filePattern": {"type": "str"},
                "schedule": {
                    "type": "dict",
                    "options": {
                        "period": {"type": "str", "choices": ["daily", "monthly", "weekly"]},
                        "syncHour": {"type": "int"},
                        "syncMinute": {"type": "int"},
                        "weekday": {"type": "str", "choices": ["friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"]},
                        "syncDayOfTheMonth": {"type": "int"}
                    }
                },
                "removeDeletedFileFingerprints": {"type": "str", "choices": ["disable", "enable"]},
                "keepModified": {"type": "str", "choices": ["disable", "enable"]},
                "scanOnCreation": {"type": "str", "choices": ["disable", "enable"]},
                "authentication": {
                    "type": "dict",
                    "options": {
                        "username": {"type": "str"},
                        "password": {"type": "str", "no_log": True}
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
