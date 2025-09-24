#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: auth_fsso_agents
short_description: FSSO Agent Resource
description:
  - FSSO Agent Resource.
  - Use API "/resource-api/v2/auth/fsso-agents".
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
            activeServer:
                type: str
                description: no description
            status:
                type: str
                description: no description
                choices:
                    - "connected"
                    - "disconnected"
            name:
                type: str
                description: no description
            server:
                type: str
                description: no description
            password:
                type: str
                description: no description
            server2:
                type: str
                description: no description
            password2:
                type: str
                description: no description
            server3:
                type: str
                description: no description
            password3:
                type: str
                description: no description
            server4:
                type: str
                description: no description
            password4:
                type: str
                description: no description
            server5:
                type: str
                description: no description
            password5:
                type: str
                description: no description
            sslTrustedCert:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Auth FSSO Agent
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "agent_example"
  tasks:
    - name: Create/Update Auth FSSO Agent
      fortinet.fortisase.auth_fsso_agents:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          name: "{{ primaryKey }}"
          server: "1.2.3.4"
          status: "disconnected"
          password: "password"
          sslTrustedCert: "remote_ca_certs"
    - name: Delete Auth FSSO Agent
      fortinet.fortisase.auth_fsso_agents:
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
    url = "/resource-api/v2/auth/fsso-agents"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "activeServer": {"type": "str"},
                "status": {"type": "str", "choices": ["connected", "disconnected"]},
                "name": {"type": "str"},
                "server": {"type": "str"},
                "password": {"type": "str", "no_log": True},
                "server2": {"type": "str"},
                "password2": {"type": "str", "no_log": True},
                "server3": {"type": "str"},
                "password3": {"type": "str", "no_log": True},
                "server4": {"type": "str"},
                "password4": {"type": "str", "no_log": True},
                "server5": {"type": "str"},
                "password5": {"type": "str", "no_log": True},
                "sslTrustedCert": {"type": "str"}
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
