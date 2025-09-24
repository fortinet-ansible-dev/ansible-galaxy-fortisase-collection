#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: endpoint_protection_profiles
short_description: Protection Profile Resource
description:
  - Protection Profile Resource.
  - Use API "/resource-api/v2/endpoint/protection-profiles/{primaryKey}".
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
            antivirus:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            antiransomware:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            eventBasedScanning:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            vulnerabilityScan:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            automaticallyPatchVulnerabilities:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            automaticVulnerabilityPatchLevel:
                type: str
                description: no description
                choices:
                    - "critical"
                    - "high"
                    - "low"
                    - "medium"
            notifyEndpointOfBlocks:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            defaultAction:
                type: str
                description: no description
                choices:
                    - "allow"
                    - "block"
                    - "monitor"
            rules:
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
                    type:
                        type: str
                        description: no description
                        choices:
                            - "regex"
                            - "simple"
                    description:
                        type: str
                        description: no description
                    class:
                        type: str
                        description: no description
                        choices:
                            - "Bluetooth"
                            - "CDROM"
                            - "Camera"
                            - "HID"
                            - "SmartCardReader"
                            - "USBDevice"
                            - "WPD"
                    manufacturer:
                        type: str
                        description: no description
                    vendorId:
                        type: str
                        description: no description
                    productId:
                        type: str
                        description: no description
                    revision:
                        type: str
                        description: no description
            exclusions:
                type: dict
                description: no description
                suboptions:
                    files:
                        type: list
                        description: no description
                        elements: str
                    folders:
                        type: list
                        description: no description
                        elements: str
            protectedFoldersPath:
                type: list
                description: no description
                elements: str
            scheduledScan:
                type: dict
                description: no description
                suboptions:
                    time:
                        type: str
                        description: no description
                    repeat:
                        type: str
                        description: no description
                        choices:
                            - "daily"
                            - "monthly"
                            - "weekly"
                    day:
                        type: int
                        description: no description
"""

EXAMPLES = """
- name: Update protection profile
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "policy1"
  tasks:
    - name: Create a new endpoint profile, do nothing if the endpoint profile already exists
      fortinet.fortisase.endpoint_policies:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          enabled: true
    - name: Update protection profile
      fortinet.fortisase.endpoint_protection_profiles:
        params:
          primaryKey: "{{ primaryKey }}"
          antiransomware: "disable"
          antivirus: "enable"
          automaticallyPatchVulnerabilities: "disable"
          defaultAction: "allow"
          eventBasedScanning: "enable"
          notifyEndpointOfBlocks: "enable"
          rules: []
          scheduledScan:
            day: 1
            repeat: "weekly"
            time: "00:00"
          vulnerabilityScan: "enable"
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
    url = "/resource-api/v2/endpoint/protection-profiles/{primaryKey}"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "only_in": ["url"], "no_log": False},
                "antivirus": {"type": "str", "choices": ["disable", "enable"]},
                "antiransomware": {"type": "str", "choices": ["disable", "enable"]},
                "eventBasedScanning": {"type": "str", "choices": ["disable", "enable"]},
                "vulnerabilityScan": {"type": "str", "choices": ["disable", "enable"]},
                "automaticallyPatchVulnerabilities": {"type": "str", "choices": ["disable", "enable"]},
                "automaticVulnerabilityPatchLevel": {"type": "str", "choices": ["critical", "high", "low", "medium"]},
                "notifyEndpointOfBlocks": {"type": "str", "choices": ["disable", "enable"]},
                "defaultAction": {"type": "str", "choices": ["allow", "block", "monitor"]},
                "rules": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "monitor"]},
                        "type": {"type": "str", "choices": ["regex", "simple"]},
                        "description": {"type": "str"},
                        "class": {"type": "str", "choices": ["Bluetooth", "CDROM", "Camera", "HID", "SmartCardReader", "USBDevice", "WPD"]},
                        "manufacturer": {"type": "str"},
                        "vendorId": {"type": "str"},
                        "productId": {"type": "str"},
                        "revision": {"type": "str"}
                    }
                },
                "exclusions": {
                    "type": "dict",
                    "options": {
                        "files": {"type": "list", "elements": "str"},
                        "folders": {"type": "list", "elements": "str"}
                    }
                },
                "protectedFoldersPath": {"type": "list", "elements": "str"},
                "scheduledScan": {
                    "type": "dict",
                    "options": {
                        "time": {"type": "str"},
                        "repeat": {"type": "str", "choices": ["daily", "monthly", "weekly"]},
                        "day": {"type": "int"}
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
