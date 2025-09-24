#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: dem_spa_applications
short_description: DEM SPA Application Resource
description:
  - DEM SPA Application Resource.
  - Use API "/resource-api/v2/dem/spa-applications".
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
            latencyThreshold:
                type: int
                description: no description
            jitterThreshold:
                type: int
                description: no description
            packetlossThreshold:
                type: int
                description: no description
            interval:
                type: int
                description: no description
            failTime:
                type: int
                description: no description
            recoveryTime:
                type: int
                description: no description
"""

EXAMPLES = """
- name: Dem SPA Applications
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "example_name"
  tasks:
    - name: Create/Update Dem SPA Applications
      fortinet.fortisase.dem_spa_applications:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          server: "string"
          latencyThreshold: 10000000
          jitterThreshold: 10000000
          packetlossThreshold: 100
          interval: 20
          failTime: 1
          recoveryTime: 1
    - name: Delete Dem SPA Applications
      fortinet.fortisase.dem_spa_applications:
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
    url = "/resource-api/v2/dem/spa-applications"
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
                "latencyThreshold": {"type": "int"},
                "jitterThreshold": {"type": "int"},
                "packetlossThreshold": {"type": "int"},
                "interval": {"type": "int"},
                "failTime": {"type": "int"},
                "recoveryTime": {"type": "int"}
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
