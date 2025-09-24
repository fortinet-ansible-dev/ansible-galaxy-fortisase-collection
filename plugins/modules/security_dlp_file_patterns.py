#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_dlp_file_patterns
short_description: DLP File Pattern Resource
description:
  - DLP File Pattern Resource.
  - Use API "/resource-api/v2/security/dlp-file-patterns".
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
            tag:
                type: str
                description: no description
            entries:
                type: list
                description: no description
                elements: dict
                suboptions:
                    pattern:
                        type: str
                        description: no description
                    filterType:
                        type: str
                        description: no description
                        choices:
                            - "pattern"
                            - "type"
                    fileType:
                        type: str
                        description: no description
                        choices:
                            - ".net"
                            - "7z"
                            - "activemime"
                            - "arj"
                            - "aspack"
                            - "avi"
                            - "base64"
                            - "bat"
                            - "binhex"
                            - "bmp"
                            - "bzip"
                            - "bzip2"
                            - "cab"
                            - "chm"
                            - "class"
                            - "cod"
                            - "crx"
                            - "dmg"
                            - "elf"
                            - "exe"
                            - "flac"
                            - "fsg"
                            - "gif"
                            - "gzip"
                            - "hibun"
                            - "hlp"
                            - "hta"
                            - "html"
                            - "iso"
                            - "jad"
                            - "javascript"
                            - "jpeg"
                            - "lzh"
                            - "mach-o"
                            - "mime"
                            - "mov"
                            - "mp3"
                            - "mpeg"
                            - "msi"
                            - "msoffice"
                            - "msofficex"
                            - "pdf"
                            - "petite"
                            - "png"
                            - "rar"
                            - "rm"
                            - "sis"
                            - "tar"
                            - "tiff"
                            - "torrent"
                            - "unknown"
                            - "upx"
                            - "uue"
                            - "wav"
                            - "wma"
                            - "xar"
                            - "xz"
                            - "zip"
"""

EXAMPLES = """
- name: Security DLP File Patterns
  hosts: fortisase
  gather_facts: false
  vars:
    dlp_file_pattern_name: "dlp_file_patterns_example"
  tasks:
    # The primaryKey is a digital id, it is "result.response.primaryKey"
    # Please use the primaryKey in the result to update/delete the target resource
    - name: Create Security DLP File Patterns
      fortinet.fortisase.security_dlp_file_patterns:
        state: present
        params:
          primaryKey: "Placeholder, not in use in create"
          tag: "{{ dlp_file_pattern_name }}"
          entries:
            - pattern: "string"
              filterType: "type"
              fileType: "7z"
      register: result
    - name: Update Security DLP File Patterns
      fortinet.fortisase.security_dlp_file_patterns:
        state: present
        params:
          primaryKey: "{{ result.response.primaryKey }}"
          tag: "{{ dlp_file_pattern_name }}"
          entries:
            - pattern: "string_modified"
              filterType: "type"
              fileType: "7z"
    - name: Delete Security DLP File Patterns
      fortinet.fortisase.security_dlp_file_patterns:
        state: absent
        params:
          primaryKey: "{{ result.response.primaryKey }}"
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
    url = "/resource-api/v2/security/dlp-file-patterns"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {
                "primaryKey": {"type": "str", "required": True, "only_in": ["update"], "no_log": False},
                "tag": {"type": "str"},
                "entries": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "pattern": {"type": "str"},
                        "filterType": {"type": "str", "choices": ["pattern", "type"]},
                        "fileType": {
                            "type": "str",
                            "choices": [
                                ".net", "7z", "activemime", "arj", "aspack", "avi", "base64", "bat", "binhex", "bmp", "bzip", "bzip2", "cab", "chm",
                                "class", "cod", "crx", "dmg", "elf", "exe", "flac", "fsg", "gif", "gzip", "hibun", "hlp", "hta", "html", "iso", "jad",
                                "javascript", "jpeg", "lzh", "mach-o", "mime", "mov", "mp3", "mpeg", "msi", "msoffice", "msofficex", "pdf", "petite",
                                "png", "rar", "rm", "sis", "tar", "tiff", "torrent", "unknown", "upx", "uue", "wav", "wma", "xar", "xz", "zip"
                            ]
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
