#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: endpoint_sandbox_profiles
short_description: Sandbox Profile Resource
description:
  - Sandbox Profile Resource.
  - Use API "/resource-api/v2/endpoint/sandbox-profiles/{primaryKey}".
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
            sandboxMode:
                type: str
                description: no description
                choices:
                    - "Disabled"
                    - "FortiSASE"
                    - "StandaloneFortiSandbox"
            notificationType:
                type: raw
                description:
                    - Integer representing how notifications should be handled on FortiSandbox file submission.
                    - 0 - display notification balloon when malware is detected in a submission.
                    - 1 - display a popup for all file submissions.
                choices:
                    - "0"
                    - "1"
            timeoutAwaitingSandboxResults:
                type: int
                description: no description
            fileSubmissionOptions:
                type: dict
                description: no description
                suboptions:
                    allEmailDownloads:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    allFilesMappedNetworkDrives:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    allFilesRemovableMedia:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    allWebDownloads:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
            detectionVerdictLevel:
                type: str
                description: no description
                choices:
                    - "Clean"
                    - "High"
                    - "Low"
                    - "Malicious"
                    - "Medium"
            exceptions:
                type: dict
                description: no description
                suboptions:
                    excludeFilesFromTrustedSources:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
                    files:
                        type: list
                        description: no description
                        elements: str
                    folders:
                        type: list
                        description: no description
                        elements: str
            remediationActions:
                type: str
                description: no description
                choices:
                    - "alert"
                    - "quarantine"
            hostName:
                type: str
                description: no description
            authentication:
                type: bool
                description: no description
            username:
                type: str
                description: no description
            password:
                type: str
                description: no description
"""

EXAMPLES = """
- name: Update sandbox profile
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
    - name: Update sandbox profile
      fortinet.fortisase.endpoint_sandbox_profiles:
        params:
          primaryKey: "{{ primaryKey }}"
          sandboxMode: "FortiSASE"  # Disabled, FortiSASE, StandaloneFortiSandbox
          detectionVerdictLevel: "Medium"
          exceptions:
            excludeFilesFromTrustedSources: "disable"
            files: []
            folders: []
          fileSubmissionOptions:
            allEmailDownloads: "enable"
            allFilesMappedNetworkDrives: "enable"
            allFilesRemovableMedia: "enable"
            allWebDownloads: "enable"
          remediationActions: "quarantine"
          timeoutAwaitingSandboxResults: 0
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
    url = "/resource-api/v2/endpoint/sandbox-profiles/{primaryKey}"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "only_in": ["url"], "no_log": False},
                "sandboxMode": {"type": "str", "choices": ["Disabled", "FortiSASE", "StandaloneFortiSandbox"]},
                "notificationType": {"type": "raw", "choices": ["0", "1"]},
                "timeoutAwaitingSandboxResults": {"type": "int"},
                "fileSubmissionOptions": {
                    "type": "dict",
                    "options": {
                        "allEmailDownloads": {"type": "str", "choices": ["disable", "enable"]},
                        "allFilesMappedNetworkDrives": {"type": "str", "choices": ["disable", "enable"]},
                        "allFilesRemovableMedia": {"type": "str", "choices": ["disable", "enable"]},
                        "allWebDownloads": {"type": "str", "choices": ["disable", "enable"]}
                    }
                },
                "detectionVerdictLevel": {"type": "str", "choices": ["Clean", "High", "Low", "Malicious", "Medium"]},
                "exceptions": {
                    "type": "dict",
                    "options": {
                        "excludeFilesFromTrustedSources": {"type": "str", "choices": ["disable", "enable"]},
                        "files": {"type": "list", "elements": "str"},
                        "folders": {"type": "list", "elements": "str"}
                    }
                },
                "remediationActions": {"type": "str", "choices": ["alert", "quarantine"]},
                "hostName": {"type": "str"},
                "authentication": {"type": "bool"},
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
        agent.process_ru(url)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
