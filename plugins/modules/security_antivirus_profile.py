#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_antivirus_profile
short_description: Antivirus Profile Resource
description:
  - Antivirus Profile Resource.
  - Use API "/resource-api/v2/security/antivirus-profile/{direction}/{primaryKey}".
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
            http:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            smtp:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            pop3:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            imap:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            ftp:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            cifs:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
"""

EXAMPLES = """
- name: Update security antivirus profile
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
    - name: Update security antivirus profile
      fortinet.fortisase.security_antivirus_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          cifs: "enable"
          ftp: "enable"
          http: "enable"
          imap: "enable"
          pop3: "enable"
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
    url = "/resource-api/v2/security/antivirus-profile/{direction}/{primaryKey}"
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
                "http": {"type": "str", "choices": ["disable", "enable"]},
                "smtp": {"type": "str", "choices": ["disable", "enable"]},
                "pop3": {"type": "str", "choices": ["disable", "enable"]},
                "imap": {"type": "str", "choices": ["disable", "enable"]},
                "ftp": {"type": "str", "choices": ["disable", "enable"]},
                "cifs": {"type": "str", "choices": ["disable", "enable"]}
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
