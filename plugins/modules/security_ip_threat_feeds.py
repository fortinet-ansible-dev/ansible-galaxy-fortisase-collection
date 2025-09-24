#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_ip_threat_feeds
short_description: IP Threat Feed Resource
description:
  - IP Threat Feed Resource.
  - Use API "/resource-api/v2/security/ip-threat-feeds".
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
            comments:
                type: str
                description: no description
            status:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            refreshRate:
                type: int
                description: no description
            uri:
                type: str
                description: no description
            basicAuthentication:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            username:
                type: str
                description: no description
            password:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Security IP Threat Feeds
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "asbfeeds"
  tasks:
    - name: Create/Update Security IP Threat Feeds
      fortinet.fortisase.security_ip_threat_feeds:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          refreshRate: 10
          status: "enable"
          uri: "https://www.virustotal.com/api/v3/domains/example.com/threat-feed"
          username: "fortinet"
          password: "fortinet"
          basicAuthentication: "enable"
    - name: Delete Security IP Threat Feeds
      fortinet.fortisase.security_ip_threat_feeds:
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
    url = "/resource-api/v2/security/ip-threat-feeds"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "comments": {"type": "str"},
                "status": {"type": "str", "choices": ["disable", "enable"]},
                "refreshRate": {"type": "int"},
                "uri": {"type": "str"},
                "basicAuthentication": {"type": "str", "choices": ["disable", "enable"]},
                "username": {"type": "str"},
                "password": {"type": "str", "no_log": True}
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
