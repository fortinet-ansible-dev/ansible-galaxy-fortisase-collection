#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_profile_group
short_description: Profile Group Resource
description:
  - Profile Group Resource.
  - Use API "/resource-api/v2/security/profile-group/{direction}".
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
            direction:
                type: str
                required: true
                description: no description
            primaryKey:
                type: str
                required: true
                description: no description
            antivirusProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            webFilterProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            videoFilterProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            dnsFilterProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            applicationControlProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            fileFilterProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            dlpFilterProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            intrusionPreventionProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
            sslSshProfile:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                    profile:
                        type: dict
                        description: no description
                        suboptions:
                            primaryKey:
                                type: str
                                description: no description
                            datasource:
                                type: str
                                description: no description
"""

EXAMPLES = """
- name: Security profile group
  hosts: fortisase
  gather_facts: false
  vars:
    direction: "outbound-profiles" # outbound-profiles or internal-profiles
    profile_group: "profile_ansible"
  tasks:
    - name: Create/Update security profile group
      fortinet.fortisase.security_profile_group:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
    - name: Delete security profile group
      fortinet.fortisase.security_profile_group:
        state: absent
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
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
    url = "/resource-api/v2/security/profile-group/{direction}"
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
                "antivirusProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "webFilterProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "videoFilterProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "dnsFilterProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "applicationControlProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "fileFilterProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "dlpFilterProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "intrusionPreventionProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        }
                    }
                },
                "sslSshProfile": {
                    "type": "dict",
                    "only_in": ["update"],
                    "options": {
                        "status": {"type": "str"},
                        "profile": {
                            "type": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
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
        agent.process_crud(url, mkey="primaryKey")
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
