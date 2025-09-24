#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_application_control_profile
short_description: Application Control Profile Resource
description:
  - Application Control Profile Resource.
  - Use API "/resource-api/v2/security/application-control-profile/{direction}/{primaryKey}".
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
            applicationCategoryControls:
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
                    category:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            applicationControls:
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
                    applications:
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
            unknownApplicationAction:
                type: str
                description: no description
                choices:
                    - "allow"
                    - "block"
                    - "monitor"
            networkProtocolEnforcement:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            networkProtocols:
                type: list
                description: no description
                elements: dict
                suboptions:
                    port:
                        type: int
                        description: no description
                    action:
                        type: str
                        description: no description
                        choices:
                            - "block"
                            - "monitor"
                            - "pass"
                    services:
                        type: list
                        description: no description
                        elements: str
            blockNonDefaultPortApplications:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
"""

EXAMPLES = """
# To configure this resource, please disable proxy configuration.
- name: Update security application control profile
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
    - name: Update security application control profile
      fortinet.fortisase.security_application_control_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          applicationControls: []
          blockNonDefaultPortApplications: "disable"
          networkProtocolEnforcement: "disable"
          networkProtocols: []
          unknownApplicationAction: "monitor"
          applicationCategoryControls:
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: P2P
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: VoIP
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Video/Audio
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Proxy
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Remote.Access
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Game
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: General.Interest
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Network.Service
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Update
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Email
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Storage.Backup
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Social.Media
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Web.Client
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Industrial
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Collaboration
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Business
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Cloud.IT
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Mobile
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: Unknown Applications
            - action: allow
              category:
                datasource: security/application-categories
                primaryKey: GenAI
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
    url = "/resource-api/v2/security/application-control-profile/{direction}/{primaryKey}"
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
                "applicationCategoryControls": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "monitor"]},
                        "category": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "applicationControls": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "monitor"]},
                        "applications": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "unknownApplicationAction": {"type": "str", "choices": ["allow", "block", "monitor"]},
                "networkProtocolEnforcement": {"type": "str", "choices": ["disable", "enable"]},
                "networkProtocols": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "port": {"type": "int"},
                        "action": {"type": "str", "choices": ["block", "monitor", "pass"]},
                        "services": {"type": "list", "elements": "str"}
                    }
                },
                "blockNonDefaultPortApplications": {"type": "str", "choices": ["disable", "enable"]}
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
