#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: infra_ssids
short_description: FortiAP SSID Resource
description:
  - FortiAP SSID Resource.
  - Use API "/resource-api/v2/infra/ssids".
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
            wifiSsid:
                type: str
                description: no description
            broadcastSsid:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            clientLimit:
                type: int
                description: no description
            securityMode:
                type: str
                description: no description
                choices:
                    - "captive-portal"
                    - "open"
                    - "wpa2-only-enterprise"
                    - "wpa2-only-personal"
                    - "wpa2-only-personal+captive-portal"
                    - "wpa3-only-enterprise"
                    - "wpa3-sae"
            captivePortal:
                type: bool
                description: no description
            securityGroups:
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
            preSharedKey:
                type: str
                description: no description
            radiusServer:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            userGroups:
                type: list
                description: no description
                elements: dict
                suboptions:
                    datasource:
                        type: str
                        description: no description
"""

EXAMPLES = """
- name: Infrastructure SSIDs
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "example"
  tasks:
    - name: Create/Update Infrastructure SSIDs
      fortinet.fortisase.infra_ssids:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          broadcastSsid: "enable"
          securityMode: "wpa2-only-personal"
          preSharedKey: "1234567890"
          wifiSsid: "wifi_ssid_example"
          clientLimit: 101
    - name: Delete Infrastructure SSIDs
      fortinet.fortisase.infra_ssids:
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
    url = "/resource-api/v2/infra/ssids"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "wifiSsid": {"type": "str"},
                "broadcastSsid": {"type": "str", "choices": ["disable", "enable"]},
                "clientLimit": {"type": "int"},
                "securityMode": {
                    "type": "str",
                    "choices": [
                        "captive-portal", "open", "wpa2-only-enterprise", "wpa2-only-personal", "wpa2-only-personal+captive-portal",
                        "wpa3-only-enterprise", "wpa3-sae"
                    ]
                },
                "captivePortal": {"type": "bool"},
                "securityGroups": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "preSharedKey": {"type": "str", "no_log": True},
                "radiusServer": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "userGroups": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "datasource": {"type": "str"}
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
