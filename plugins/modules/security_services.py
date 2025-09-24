#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_services
short_description: Service Resource
description:
  - Service Resource.
  - Use API "/resource-api/v2/security/services".
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
            proxy:
                type: bool
                description: no description
            category:
                type: str
                description: no description
                choices:
                    - "Authentication"
                    - "Email"
                    - "File Access"
                    - "General"
                    - "Network Services"
                    - "Remote Access"
                    - "Tunneling"
                    - "Uncategorized"
                    - "VoIP, Messaging & Other Applications"
                    - "Web Access"
                    - "Web Proxy"
            protocol:
                type: str
                description: no description
            protocolNumber:
                type: int
                description: no description
            icmpType:
                type: int
                description: no description
            udpPortrange:
                type: list
                description: no description
                elements: dict
                suboptions:
                    destination:
                        type: dict
                        description: no description
                        suboptions:
                            low:
                                type: int
                                description: no description
                            high:
                                type: int
                                description: no description
                    source:
                        type: dict
                        description: no description
                        suboptions:
                            low:
                                type: int
                                description: no description
                            high:
                                type: int
                                description: no description
            sctpPortrange:
                type: list
                description: no description
                elements: dict
                suboptions:
                    destination:
                        type: dict
                        description: no description
                        suboptions:
                            low:
                                type: int
                                description: no description
                            high:
                                type: int
                                description: no description
                    source:
                        type: dict
                        description: no description
                        suboptions:
                            low:
                                type: int
                                description: no description
                            high:
                                type: int
                                description: no description
            tcpPortrange:
                type: list
                description: no description
                elements: dict
                suboptions:
                    destination:
                        type: dict
                        description: no description
                        suboptions:
                            low:
                                type: int
                                description: no description
                            high:
                                type: int
                                description: no description
                    source:
                        type: dict
                        description: no description
                        suboptions:
                            low:
                                type: int
                                description: no description
                            high:
                                type: int
                                description: no description
"""

EXAMPLES = """
- name: Security service
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "service_example"
  tasks:
    - name: Create/Update security service
      fortinet.fortisase.security_services:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          proxy: false
          category: "Email"
          protocol: "TCP/UDP/SCTP"
          tcpPortrange:
            - destination:
                low: 25
    - name: Delete security service
      fortinet.fortisase.security_services:
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
    url = "/resource-api/v2/security/services"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "no_log": False},
                "proxy": {"type": "bool"},
                "category": {
                    "type": "str",
                    "choices": [
                        "Authentication", "Email", "File Access", "General", "Network Services", "Remote Access", "Tunneling", "Uncategorized",
                        "VoIP, Messaging & Other Applications", "Web Access", "Web Proxy"
                    ]
                },
                "protocol": {"type": "str"},
                "protocolNumber": {"type": "int"},
                "icmpType": {"type": "int"},
                "udpPortrange": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "destination": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "int"},
                                "high": {"type": "int"}
                            }
                        },
                        "source": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "int"},
                                "high": {"type": "int"}
                            }
                        }
                    }
                },
                "sctpPortrange": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "destination": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "int"},
                                "high": {"type": "int"}
                            }
                        },
                        "source": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "int"},
                                "high": {"type": "int"}
                            }
                        }
                    }
                },
                "tcpPortrange": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "destination": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "int"},
                                "high": {"type": "int"}
                            }
                        },
                        "source": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "int"},
                                "high": {"type": "int"}
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
