#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_web_filter_profile
short_description: Web Filter Profile Resource
description:
  - Web Filter Profile Resource.
  - Use API "/resource-api/v2/security/web-filter-profile/{direction}/{primaryKey}".
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
                    warningDuration:
                        type: str
                        description: no description
            fortiguardLocalCategoryFilters:
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
                            - "disable"
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
                    warningDuration:
                        type: str
                        description: no description
            fqdnThreatFeedFilters:
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
                            - "disable"
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
                    warningDuration:
                        type: str
                        description: no description
            useFortiguardFilters:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            blockInvalidUrl:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            enforceSafeSearch:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            trafficOnRatingError:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            contentFilters:
                type: list
                description: no description
                elements: dict
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    pattern:
                        type: str
                        description: no description
                    patternType:
                        type: str
                        description: no description
                        choices:
                            - "regexp"
                            - "wildcard"
                    lang:
                        type: str
                        description: no description
                        choices:
                            - "cyrillic"
                            - "french"
                            - "japanese"
                            - "korean"
                            - "simch"
                            - "spanish"
                            - "thai"
                            - "trach"
                            - "western"
                    action:
                        type: str
                        description: no description
                        choices:
                            - "block"
                            - "exempt"
                    score:
                        type: int
                        description: no description
            urlFilters:
                type: list
                description: no description
                elements: dict
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    url:
                        type: str
                        description: no description
                    type:
                        type: str
                        description: no description
                        choices:
                            - "regex"
                            - "simple"
                            - "wildcard"
                    action:
                        type: str
                        description: no description
                        choices:
                            - "allow"
                            - "block"
                            - "exempt"
                            - "monitor"
            httpHeaders:
                type: list
                description: no description
                elements: dict
                suboptions:
                    name:
                        type: str
                        description: no description
                    action:
                        type: str
                        description: no description
                        choices:
                            - "add-to-request"
                            - "add-to-response"
                            - "remove-from-request"
                            - "remove-from-response"
                    content:
                        type: str
                        description: no description
                    destinations:
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
                                choices:
                                    - "network/host-groups"
                                    - "network/hosts"
"""

EXAMPLES = """
- name: Update security web filter profile
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
    - name: Update security web filter profile
      fortinet.fortisase.security_web_filter_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          blockInvalidUrl: "disable"
          contentFilters: []
          enforceSafeSearch: "disable"
          fqdnThreatFeedFilters: []
          httpHeaders: []
          trafficOnRatingError: "enable"
          urlFilters: []
          useFortiguardFilters: "enable"
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
    url = "/resource-api/v2/security/web-filter-profile/{direction}/{primaryKey}"
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
                        "action": {"type": "str", "choices": ["allow", "block", "monitor", "warning"]},
                        "category": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "warningDuration": {"type": "str"}
                    }
                },
                "fortiguardLocalCategoryFilters": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "disable", "monitor", "warning"]},
                        "category": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "warningDuration": {"type": "str"}
                    }
                },
                "fqdnThreatFeedFilters": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "action": {"type": "str", "choices": ["allow", "block", "disable", "monitor", "warning"]},
                        "category": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "warningDuration": {"type": "str"}
                    }
                },
                "useFortiguardFilters": {"type": "str", "choices": ["disable", "enable"]},
                "blockInvalidUrl": {"type": "str", "choices": ["disable", "enable"]},
                "enforceSafeSearch": {"type": "str", "choices": ["disable", "enable"]},
                "trafficOnRatingError": {"type": "str", "choices": ["disable", "enable"]},
                "contentFilters": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "pattern": {"type": "str"},
                        "patternType": {"type": "str", "choices": ["regexp", "wildcard"]},
                        "lang": {"type": "str", "choices": ["cyrillic", "french", "japanese", "korean", "simch", "spanish", "thai", "trach", "western"]},
                        "action": {"type": "str", "choices": ["block", "exempt"]},
                        "score": {"type": "int"}
                    }
                },
                "urlFilters": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "url": {"type": "str"},
                        "type": {"type": "str", "choices": ["regex", "simple", "wildcard"]},
                        "action": {"type": "str", "choices": ["allow", "block", "exempt", "monitor"]}
                    }
                },
                "httpHeaders": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "action": {"type": "str", "choices": ["add-to-request", "add-to-response", "remove-from-request", "remove-from-response"]},
                        "content": {"type": "str"},
                        "destinations": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str", "choices": ["network/host-groups", "network/hosts"]}
                            }
                        }
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
