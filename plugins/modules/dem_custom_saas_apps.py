#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: dem_custom_saas_apps
short_description: DEM Custom SaaS Applications Resource
description:
  - DEM Custom SaaS Applications Resource.
  - Use API "/resource-api/v2/dem/custom-saas-apps".
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
                description: The primary key object of the DEM custom SaaS application. Can not be updated once created.
            alias:
                type: raw
                description: no description
            fqdn:
                type: str
                description: The FQDN of the custom SaaS application.
"""

EXAMPLES = """
- name: Dem Custom SaaS Apps
  hosts: fortisase
  gather_facts: false
  vars:
    primaryKey: "example.com"
    fqdn: "example.com"
    alias: "example.com"
  tasks:
    - name: Create/Update Dem Custom SaaS Apps
      fortinet.fortisase.dem_custom_saas_apps:
        state: present
        params:
          primaryKey: "{{ primaryKey }}"
          fqdn: "{{ fqdn }}"
          alias: "{{ alias }}"
    - name: Delete Dem Custom SaaS Apps
      fortinet.fortisase.dem_custom_saas_apps:
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
    url = "/resource-api/v2/dem/custom-saas-apps"
    src_arg_spec = {
        "state": {"type": "str", "default": "present", "choices": ["present", "absent"]},
        "force_behavior": {"type": "str", "default": "none", "choices": ["none", "read", "create", "update", "delete"]},
        "bypass_validation": {"type": "bool", "default": False},
        "params": {
            "type": "dict",
            "required": True,
            "options": {"primaryKey": {"type": "str", "required": True, "no_log": False}, "alias": {"type": "raw"}, "fqdn": {"type": "str"}}
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
