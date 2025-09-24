#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
module: fortisase_generic
short_description: Send generic FortiSASE API request.
description:
    - This module is for generic fortisase requests. It receives raw json-rpc
      data, and sends it to fortisase, finally returns the response to users.
    - Two parameters schemes are supported, either in raw json format "json"
      or in ansible recognnizable format "params".
    - If all two parameters are provided, the "json" is preferred.
version_added: "1.0.0"
author:
    - Xinwei Du (@dux-fortinet)
options:
    method:
        description: The method of the HTTP request.
        type: str
        required: true
        choices: ["get", "post", "put", "delete"]
    url:
        description: The URL of the API.
        type: str
        required: true
    json:
        description: Raw json-rpc data.
        type: str
        required: false
    params:
        description: Ansible recognnizable parameters.
        type: dict
        required: false
"""

EXAMPLES = """
- name: FortiSASE Generic Request
  hosts: fortisase
  gather_facts: false
  tasks:
    - name: FortiSASE Generic POST (Create) Request
      fortinet.fortisase.fortisase_generic:
        method: post
        url: "/resource-api/v2/network/dns-rules"
        params:
          primaryKey: "3"
          primaryDns: "3.3.3.3"
          secondaryDns: "3.3.3.2"
          domains:
            - www.33333.com
          popDnsOverride: {}
    - name: FortiSASE Generic GET (Read) Request
      fortinet.fortisase.fortisase_generic:
        method: get
        url: "/resource-api/v2/network/dns-rules/3"
    - name: FortiSASE Generic PUT (Update) Request
      fortinet.fortisase.fortisase_generic:
        method: put
        url: "/resource-api/v2/network/dns-rules/3"
        params:
          primaryKey: "3"
          primaryDns: "4.4.4.4"
          secondaryDns: "4.4.4.2"
          domains:
            - www.44444.com
          popDnsOverride: {}
    - name: FortiSASE Generic Delete (Delete) Request
      fortinet.fortisase.fortisase_generic:
        method: delete
        url: "/resource-api/v2/network/dns-rules/3"

# Using json string
- name: FortiSASE Generic Request (Using JSON String)
  hosts: fortisase
  gather_facts: false
  tasks:
    - name: FortiSASE Generic POST (Create) Request (JSON String)
      fortinet.fortisase.fortisase_generic:
        method: post
        url: "/resource-api/v2/network/dns-rules"
        json: |
          {
            "primaryKey": "3",
            "primaryDns": "3.3.3.3",
            "secondaryDns": "3.3.3.2",
            "domains": ["www.33333.com"],
            "popDnsOverride": {}
          }
    - name: FortiSASE Generic Delete (Delete) Request (JSON String)
      fortinet.fortisase.fortisase_generic:
        method: delete
        url: "/resource-api/v2/network/dns-rules/3"
        json: "{}"
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
from ansible_collections.fortinet.fortisase.plugins.module_utils.fortisase import FortiSASEAPI
import json


def main():
    module_arg_spec = {
        "method": {"type": "str", "required": True, "choices": ["get", "post", "put", "delete"]},
        "url": {"type": "str", "required": True},
        "params": {"type": "dict"},
        "json": {"type": "str"},
    }
    module = AnsibleModule(
        argument_spec=module_arg_spec,
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module)
        params = module.params
        method = params["method"]
        url = params["url"]
        data = {}
        data = params["params"] if params.get("params") is not None else data
        data = json.loads(params["json"]) if params.get("json")else data
        agent.process_generic(method, url, data)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
