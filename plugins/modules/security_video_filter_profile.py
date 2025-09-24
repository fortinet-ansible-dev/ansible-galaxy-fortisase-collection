#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_video_filter_profile
short_description: Video Filter Profile Resource
description:
  - Video Filter Profile Resource.
  - Use API "/resource-api/v2/security/video-filter-profile/{direction}/{primaryKey}".
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
            fortiguardFilters:
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
                            - "default"
                            - "monitor"
                            - "warning"
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
            defaultAction:
                type: str
                description: no description
            channels:
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
                    name:
                        type: str
                        description: no description
                    channelId:
                        type: str
                        description: no description
"""

EXAMPLES = """
- name: Update security video filter profile
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
    - name: Update security video filter profile
      fortinet.fortisase.security_video_filter_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          defaultAction: "monitor"
          channels: []
          fortiguardFilters:
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Not Rated"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Business"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Entertainment"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Games"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Knowledge"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Lifestyle"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Music"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "News"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "People"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Society"
            - action: "default"
              category:
                datasource: "security/video-filter-fortiguard-categories"
                primaryKey: "Sports"
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
    url = "/resource-api/v2/security/video-filter-profile/{direction}/{primaryKey}"
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
                "fortiguardFilters": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "default", "monitor", "warning"]},
                        "category": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "defaultAction": {"type": "str"},
                "channels": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "monitor"]},
                        "name": {"type": "str"},
                        "channelId": {"type": "str"}
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
