#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: endpoint_connection_profiles
short_description: Connection Profile Resource
description:
  - Connection Profile Resource.
  - Use API "/resource-api/v2/endpoint/connection-profiles/{primaryKey}".
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
            primaryKey:
                type: str
                required: true
                description: no description
            connectToFortiSASE:
                type: str
                description: no description
                choices:
                    - "automatically"
                    - "manually"
            lockdown:
                type: dict
                description: no description
                suboptions:
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    gracePeriod:
                        type: int
                        description: no description
                    maxAttempts:
                        type: int
                        description: no description
                    ips:
                        type: list
                        description: no description
                        elements: dict
                        suboptions:
                            ip:
                                type: str
                                description: no description
                            port:
                                type: str
                                description: no description
                            protocol:
                                type: str
                                description: no description
                                choices:
                                    - ""
                                    - "icmp"
                                    - "tcp"
                                    - "udp"
                    domains:
                        type: list
                        description: no description
                        elements: dict
                        suboptions:
                            address:
                                type: str
                                description: no description
                    detectCaptivePortal:
                        type: dict
                        description: no description
                        suboptions:
                            status:
                                type: str
                                description: no description
                                choices:
                                    - "disable"
                                    - "enable"
            onFabricRuleSet:
                type: dict
                description: no description
                suboptions:
                    primaryKey:
                        type: str
                        description: no description
                    datasource:
                        type: str
                        description: no description
            offNetSplitTunnel:
                type: dict
                description: no description
                suboptions:
                    localApps:
                        type: list
                        description: no description
                        elements: str
                    isdbs:
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
                    fqdns:
                        type: list
                        description: no description
                        elements: str
                    subnets:
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
                    subnetsIpsec:
                        type: list
                        description: no description
                        elements: str
            splitTunnel:
                type: dict
                description: no description
                suboptions:
                    localApps:
                        type: list
                        description: no description
                        elements: str
                    isdbs:
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
                    fqdns:
                        type: list
                        description: no description
                        elements: str
                    subnets:
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
                    subnetsIpsec:
                        type: list
                        description: no description
                        elements: str
            allowInvalidServerCertificate:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            endpointOnNetBypass:
                type: bool
                description: no description
            authBeforeUserLogon:
                type: bool
                description: no description
            secureInternetAccess:
                type: dict
                description: no description
                suboptions:
                    authenticateWithSSO:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    enableLocalLan:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    failoverSequence:
                        type: list
                        description: no description
                        elements: str
                    postureCheck:
                        type: dict
                        description: no description
                        suboptions:
                            tag:
                                type: str
                                description: no description
                            action:
                                type: str
                                description: no description
                                choices:
                                    - "allow"
                                    - "prohibit"
                            checkFailedMessage:
                                type: str
                                description: no description
                    externalBrowserSamlLogin:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
            preferredDTLSTunnel:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            useGuiSamlAuth:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            allowPersonalVpns:
                type: bool
                description: no description
            mtuSize:
                type: int
                description: no description
            availableVPNs:
                type: list
                description: no description
                elements: dict
                suboptions:
                    type:
                        type: str
                        description: no description
                        choices:
                            - "ipSecVPN"
                            - "sslVPN"
                    name:
                        type: str
                        description: no description
                    remoteGateway:
                        type: str
                        description: no description
                    usernamePrompt:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    saveUsername:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    showAlwaysUp:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    showAutoConnect:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    showRememberPassword:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    authenticateWithSSO:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    enableLocalLan:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    externalBrowserSamlLogin:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    port:
                        type: int
                        description: no description
                    requireCertificate:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    authMethod:
                        type: str
                        description: no description
                        choices:
                            - "preSharedKey"
                            - "smartCardCert"
                            - "systemStoreCert"
                    showPasscode:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    postureCheck:
                        type: dict
                        description: no description
                        suboptions:
                            tag:
                                type: str
                                description: no description
                            action:
                                type: str
                                description: no description
                                choices:
                                    - "allow"
                                    - "prohibit"
                            checkFailedMessage:
                                type: str
                                description: no description
                    preSharedKey:
                        type: str
                        description: no description
            showDisconnectBtn:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            enableInvalidServerCertWarning:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            preLogon:
                type: dict
                description: no description
                suboptions:
                    vpnType:
                        type: str
                        description: no description
                        choices:
                            - "ipSecVPN"
                            - "sslVPN"
                    remoteGateway:
                        type: str
                        description: no description
                    commonName:
                        type: dict
                        description: no description
                        suboptions:
                            matchType:
                                type: str
                                description: no description
                                choices:
                                    - "regex"
                                    - "wildcard"
                            pattern:
                                type: str
                                description: no description
                    issuer:
                        type: dict
                        description: no description
                        suboptions:
                            matchType:
                                type: str
                                description: no description
                                choices:
                                    - "regex"
                                    - "wildcard"
                            pattern:
                                type: str
                                description: no description
                    port:
                        type: int
                        description: no description
"""

EXAMPLES = """
- name: Connection profile
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "policy1"
  tasks:
    - name: Create a new endpoint profile, do nothing if the endpoint profile already exists
      fortinet.fortisase.endpoint_policies:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          enabled: true
    - name: Update connection profile
      fortinet.fortisase.endpoint_connection_profiles:
        params:
          primaryKey: "{{ primaryKey }}"
          allowInvalidServerCertificate: "enable"
          allowPersonalVpns: false
          authBeforeUserLogon: false
          availableVPNs: []
          connectToFortiSASE: "manually"
          enableInvalidServerCertWarning: "disable"
          endpointOnNetBypass: false
          preferredDTLSTunnel: "enable"
          secureInternetAccess:
            authenticateWithSSO: "disable"
            externalBrowserSamlLogin: "disable"
          useGuiSamlAuth: "disable"
    - name: Delete connection profile
      fortinet.fortisase.endpoint_connection_profiles:
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
    url = "/resource-api/v2/endpoint/connection-profiles/{primaryKey}"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "only_in": ["url"], "no_log": False},
                "connectToFortiSASE": {"type": "str", "choices": ["automatically", "manually"]},
                "lockdown": {
                    "type": "dict",
                    "options": {
                        "status": {"type": "str", "choices": ["disable", "enable"]},
                        "gracePeriod": {"type": "int"},
                        "maxAttempts": {"type": "int"},
                        "ips": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "ip": {"type": "str"},
                                "port": {"type": "str"},
                                "protocol": {"type": "str", "choices": ["", "icmp", "tcp", "udp"]}
                            }
                        },
                        "domains": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "address": {"type": "str"}
                            }
                        },
                        "detectCaptivePortal": {
                            "type": "dict",
                            "options": {
                                "status": {"type": "str", "choices": ["disable", "enable"]}
                            }
                        }
                    }
                },
                "onFabricRuleSet": {
                    "type": "dict",
                    "options": {
                        "primaryKey": {"type": "str", "no_log": False},
                        "datasource": {"type": "str"}
                    }
                },
                "offNetSplitTunnel": {
                    "type": "dict",
                    "options": {
                        "localApps": {"type": "list", "elements": "str"},
                        "isdbs": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "fqdns": {"type": "list", "elements": "str"},
                        "subnets": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str", "choices": ["network/host-groups", "network/hosts"]}
                            }
                        },
                        "subnetsIpsec": {"type": "list", "elements": "str"}
                    }
                },
                "splitTunnel": {
                    "type": "dict",
                    "options": {
                        "localApps": {"type": "list", "elements": "str"},
                        "isdbs": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str"}
                            }
                        },
                        "fqdns": {"type": "list", "elements": "str"},
                        "subnets": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "primaryKey": {"type": "str", "no_log": False},
                                "datasource": {"type": "str", "choices": ["network/host-groups", "network/hosts"]}
                            }
                        },
                        "subnetsIpsec": {"type": "list", "elements": "str"}
                    }
                },
                "allowInvalidServerCertificate": {"type": "str", "choices": ["disable", "enable"]},
                "endpointOnNetBypass": {"type": "bool"},
                "authBeforeUserLogon": {"type": "bool"},
                "secureInternetAccess": {
                    "type": "dict",
                    "options": {
                        "authenticateWithSSO": {"type": "str", "choices": ["disable", "enable"]},
                        "enableLocalLan": {"type": "str", "choices": ["disable", "enable"]},
                        "failoverSequence": {"type": "list", "elements": "str"},
                        "postureCheck": {
                            "type": "dict",
                            "options": {
                                "tag": {"type": "str"},
                                "action": {"type": "str", "choices": ["allow", "prohibit"]},
                                "checkFailedMessage": {"type": "str"}
                            }
                        },
                        "externalBrowserSamlLogin": {"type": "str", "choices": ["disable", "enable"]}
                    }
                },
                "preferredDTLSTunnel": {"type": "str", "choices": ["disable", "enable"]},
                "useGuiSamlAuth": {"type": "str", "choices": ["disable", "enable"]},
                "allowPersonalVpns": {"type": "bool"},
                "mtuSize": {"type": "int"},
                "availableVPNs": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "type": {"type": "str", "choices": ["ipSecVPN", "sslVPN"]},
                        "name": {"type": "str"},
                        "remoteGateway": {"type": "str"},
                        "usernamePrompt": {"type": "str", "choices": ["disable", "enable"]},
                        "saveUsername": {"type": "str", "choices": ["disable", "enable"]},
                        "showAlwaysUp": {"type": "str", "choices": ["disable", "enable"]},
                        "showAutoConnect": {"type": "str", "choices": ["disable", "enable"]},
                        "showRememberPassword": {"type": "str", "choices": ["disable", "enable"], "no_log": False},
                        "authenticateWithSSO": {"type": "str", "choices": ["disable", "enable"]},
                        "enableLocalLan": {"type": "str", "choices": ["disable", "enable"]},
                        "externalBrowserSamlLogin": {"type": "str", "choices": ["disable", "enable"]},
                        "port": {"type": "int"},
                        "requireCertificate": {"type": "str", "choices": ["disable", "enable"]},
                        "authMethod": {"type": "str", "choices": ["preSharedKey", "smartCardCert", "systemStoreCert"]},
                        "showPasscode": {"type": "str", "choices": ["disable", "enable"], "no_log": False},
                        "postureCheck": {
                            "type": "dict",
                            "options": {
                                "tag": {"type": "str"},
                                "action": {"type": "str", "choices": ["allow", "prohibit"]},
                                "checkFailedMessage": {"type": "str"}
                            }
                        },
                        "preSharedKey": {"type": "str", "no_log": True}
                    }
                },
                "showDisconnectBtn": {"type": "str", "choices": ["disable", "enable"]},
                "enableInvalidServerCertWarning": {"type": "str", "choices": ["disable", "enable"]},
                "preLogon": {
                    "type": "dict",
                    "options": {
                        "vpnType": {"type": "str", "choices": ["ipSecVPN", "sslVPN"]},
                        "remoteGateway": {"type": "str"},
                        "commonName": {
                            "type": "dict",
                            "options": {
                                "matchType": {"type": "str", "choices": ["regex", "wildcard"]},
                                "pattern": {"type": "str"}
                            }
                        },
                        "issuer": {
                            "type": "dict",
                            "options": {
                                "matchType": {"type": "str", "choices": ["regex", "wildcard"]},
                                "pattern": {"type": "str"}
                            }
                        },
                        "port": {"type": "int"}
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
