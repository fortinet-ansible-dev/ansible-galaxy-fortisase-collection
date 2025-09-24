#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: endpoint_ztna_rules
short_description: ZTNA Rule Resource
description:
  - ZTNA Rule Resource.
  - Use API "/resource-api/v2/endpoint/ztna-rules".
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
            status:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            tag:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            comments:
                type: str
                description: no description
            rules:
                type: list
                description: no description
                elements: dict
                suboptions:
                    id:
                        type: int
                        description: no description
                    os:
                        type: str
                        description: no description
                        choices:
                            - "android"
                            - "ios"
                            - "linux"
                            - "macos"
                            - "windows"
                    type:
                        type: str
                        description: no description
                        choices:
                            - "ad-groups"
                            - "anti-virus"
                            - "certificate"
                            - "crowdstrike-zta-score"
                            - "cve"
                            - "ems-management"
                            - "fct-version"
                            - "file"
                            - "ip-range"
                            - "logged-in-domain"
                            - "on-fabric-status"
                            - "os-version"
                            - "registry-key"
                            - "running-process"
                            - "sandbox-detection"
                            - "security"
                            - "security-status"
                            - "user-identity"
                            - "vulnerable-devices"
                            - "windows-security"
                    service:
                        type: str
                        description: no description
                        choices:
                            - "Custom"
                            - "Google"
                            - "LinkedIn"
                            - "Salesforce"
                    account:
                        type: str
                        description: no description
                    matchType:
                        type: str
                        description: no description
                        choices:
                            - "regex"
                            - "simple"
                            - "wildcard"
                    subject:
                        type: str
                        description: no description
                    issuer:
                        type: str
                        description: no description
                    content:
                        type: str
                        description: no description
                        choices:
                            - "AV Signature is up-to-date"
                            - "AV Software is installed and running"
                            - "Application Guard is enabled"
                            - "Automatic Updates are enabled"
                            - "Biometrics Protected"
                            - "Bitlocker Disk Encryption is enabled on OS disk"
                            - "Bitlocker Disk Encryption is enabled on all disks"
                            - "Critical"
                            - "Exploit Guard is enabled"
                            - "High or higher"
                            - "Jail-broken"
                            - "Low or higher"
                            - "Medium or higher"
                            - "Passcode Enabled"
                            - "Windows Defender is enabled"
                            - "Windows Firewall is enabled"
                    path:
                        type: str
                        description: no description
                    negated:
                        type: bool
                        description: no description
                    enableLatestUpdateCheck:
                        type: bool
                        description: no description
                    checkUpdatesWithinDays:
                        type: int
                        description: no description
                    comparator:
                        type: str
                        description: no description
                        choices:
                            - "<"
                            - "<="
                            - "="
                            - ">"
                            - ">="
                    condition:
                        type: dict
                        description: no description
                        suboptions:
                            key:
                                type: str
                                description: no description
                            isDword:
                                type: bool
                                description: no description
                            comparator:
                                type: str
                                description: no description
                                choices:
                                    - "!="
                                    - "<"
                                    - "<="
                                    - "="
                                    - ">"
                                    - ">="
                            value:
                                type: str
                                description: no description
            logic:
                type: dict
                description: no description
                suboptions:
                    windows:
                        type: raw
                        description: no description
                    macos:
                        type: raw
                        description: no description
                    linux:
                        type: raw
                        description: no description
                    ios:
                        type: raw
                        description: no description
                    android:
                        type: raw
                        description: no description
"""

EXAMPLES = """
- name: Ztna rule
  hosts: fortisase
  gather_facts: false
  vars:
    policy: "policy1"
    tag: "tag_example"
    rule_name: "rule_example"
  tasks:
    - name: Create a new endpoint profile, do nothing if the endpoint profile already exists
      fortinet.fortisase.endpoint_policies:
        state: present
        params:
          primaryKey: "{{ policy }}"
          enabled: true
    - name: Create/Update ztna tag, do nothing if the ztna tag already exists
      fortinet.fortisase.endpoint_ztna_tags:
        state: present
        params:
          primaryKey: "{{ tag }}"
          name: "{{ tag }}"
    - name: Create/Update ztna rule
      fortinet.fortisase.endpoint_ztna_rules:
        state: present
        params:
          primaryKey: "{{ rule_name }}"
          status: "enable" # "enable" or "disable"
          tag:
            primaryKey: "{{ tag }}"
            datasource: "endpoint/ztna-tags"
          comments: "example comment"
          rules:
            - os: "windows" # "windows", "macos", "linux", "ios", "android"
              type: "anti-virus"
              content: "AV Software is installed and running"
    - name: Delete ztna rule
      fortinet.fortisase.endpoint_ztna_rules:
        state: absent
        params:
          primaryKey: "{{ rule_name }}"
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
    url = "/resource-api/v2/endpoint/ztna-rules"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "status": {"type": "str", "choices": ["disable", "enable"]},
                "tag": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "comments": {"type": "str"},
                "rules": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "id": {"type": "int"},
                        "os": {"type": "str", "choices": ["android", "ios", "linux", "macos", "windows"]},
                        "type": {
                            "type": "str",
                            "choices": [
                                "ad-groups", "anti-virus", "certificate", "crowdstrike-zta-score", "cve", "ems-management", "fct-version", "file",
                                "ip-range", "logged-in-domain", "on-fabric-status", "os-version", "registry-key", "running-process", "sandbox-detection",
                                "security", "security-status", "user-identity", "vulnerable-devices", "windows-security"
                            ]
                        },
                        "service": {"type": "str", "choices": ["Custom", "Google", "LinkedIn", "Salesforce"]},
                        "account": {"type": "str"},
                        "matchType": {"type": "str", "choices": ["regex", "simple", "wildcard"]},
                        "subject": {"type": "str"},
                        "issuer": {"type": "str"},
                        "content": {
                            "type": "str",
                            "choices": [
                                "AV Signature is up-to-date", "AV Software is installed and running", "Application Guard is enabled",
                                "Automatic Updates are enabled", "Biometrics Protected", "Bitlocker Disk Encryption is enabled on OS disk",
                                "Bitlocker Disk Encryption is enabled on all disks", "Critical", "Exploit Guard is enabled", "High or higher",
                                "Jail-broken", "Low or higher", "Medium or higher", "Passcode Enabled", "Windows Defender is enabled",
                                "Windows Firewall is enabled"
                            ]
                        },
                        "path": {"type": "str"},
                        "negated": {"type": "bool"},
                        "enableLatestUpdateCheck": {"type": "bool"},
                        "checkUpdatesWithinDays": {"type": "int"},
                        "comparator": {"type": "str", "choices": ["<", "<=", "=", ">", ">="]},
                        "condition": {
                            "type": "dict",
                            "options": {
                                "key": {"type": "str", "no_log": False},
                                "isDword": {"type": "bool"},
                                "comparator": {"type": "str", "choices": ["!=", "<", "<=", "=", ">", ">="]},
                                "value": {"type": "str"}
                            }
                        }
                    }
                },
                "logic": {
                    "type": "dict",
                    "options": {
                        "windows": {"type": "raw"},
                        "macos": {"type": "raw"},
                        "linux": {"type": "raw"},
                        "ios": {"type": "raw"},
                        "android": {"type": "raw"}
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
