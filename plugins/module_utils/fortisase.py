# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.connection import Connection
from ansible.module_utils.basic import _load_params
import os


class FortiSASEAPI:
    def __init__(self, module, src_arg_spec=None):
        self.module = module
        if not module._socket_path:
            raise_connection_error(module, "This module MUST run in httpapi connection mode.\n")
        self.connection = Connection(module._socket_path)
        validate_ansible_os(self.module, self.connection)
        self.src_arg_spec = src_arg_spec
        self.mkey = None
        self.task = None
        self.url = None
        self.params_in_url = []

    def handle_force_method(self):
        params = self.module.params
        force_method = params.get("force_method", "none")
        if force_method != "none":
            mkey_value = self.get_mkey_value(self.mkey)
            base_url = self.url
            child_url = f"{self.url}/{mkey_value}".rstrip("/")
            msg = f"Force method: {force_method}"
            if force_method == "create":
                response, http_code = self.create(f"{base_url}", data=params["params"])
            elif force_method == "read":
                response, http_code = self.read(f"{child_url}")
            elif force_method == "update":
                if self.task == "CRD":
                    response, http_code = self.delete(f"{child_url}")
                    response, http_code = self.create(f"{base_url}", data=params["params"])
                else:
                    response, http_code = self.update(f"{child_url}", data=params["params"])
            elif force_method == "delete":
                response, http_code = self.delete(f"{child_url}")
            self.do_exit(response, http_code, changed=(force_method != "read"), msg=msg)

    def _modify_user_input(self, params, metadata, method):
        """
        Modify the user input.
        Remove the key if its value is None.
        Rename the key if the key is in the metadata and has api_name property.

        Method: Can be "create", "update". Different methods have different params.
        If method is specified, the key will ignore the params that are not in the method.
        """
        if not isinstance(params, dict):
            return params
        if not isinstance(metadata, dict):
            metadata = {}
        return_params = {}
        for key, value in params.items():
            sub_metadata = metadata.get(key, {})
            if "api_name" in sub_metadata:
                key = sub_metadata["api_name"]
            param_in_method = sub_metadata.get("only_in", [])
            if param_in_method and method not in param_in_method:
                continue
            if value is None:
                continue
            if isinstance(value, dict):
                return_params[key] = self._modify_user_input(value, sub_metadata.get("options", {}), method)
            elif isinstance(value, list):
                return_params[key] = [self._modify_user_input(item, sub_metadata.get("options", {}), method) for item in value]
            else:
                return_params[key] = value
        return return_params

    def process_facts(self, facts_schema):
        params = self.module.params
        selector = params["selector"]
        url = facts_schema[selector]
        user_spec = params["params"] or {}
        for key, value in user_spec.items():
            replace_value = str(value) if value is not None else ""
            url = url.replace(f"{{{key}}}", replace_value)
        if "{" in url:
            missing_keys = [key.replace("{", "").replace("}", "") for key in url.split("/") if "{" in key]
            self.module.fail_json(msg=f"Missing param(s): {missing_keys}")
        url = url.rstrip("/")  # remove trailing "/"
        response, http_code = self.read(f"{url}")
        self.do_exit(response, http_code, changed=False, msg=None)

    def process_generic(self, method, url, data):
        response, http_code = {}, -1
        if method == "get":
            response, http_code = self.read(url)
        elif method == "post":
            response, http_code = self.create(url, data=data)
        elif method == "put":
            response, http_code = self.update(url, data=data)
        elif method == "delete":
            response, http_code = self.delete(url)
        self.do_exit(response, http_code, changed=False, msg=None)

    def process_crud(self, url, mkey=None):
        self.task = "CRUD"
        self.url = self.parse_url(url)
        self.mkey = mkey
        self.handle_force_method()
        create_params = self._modify_user_input(self.module.params, self.src_arg_spec, "create")
        update_params = self._modify_user_input(self.module.params, self.src_arg_spec, "update")
        mkey_value = self.get_mkey_value(mkey)
        base_url = self.url
        child_url = f"{self.url}/{mkey_value}".rstrip("/")
        state = create_params["state"]
        response, http_code = {}, -1
        changed = False
        msg = None
        if state == 'present':
            response, http_code = self.read(f"{child_url}")
            if http_code == 200 and response:
                if self.check_need_update(update_params["params"], response):
                    response, http_code = self.update(f"{child_url}", data=update_params["params"])
                    changed = True
                else:
                    msg = "Local data is the same as remote data. Skipped update. To force update, set 'force_method: update'."
            else:
                response, http_code = self.create(f"{base_url}", data=create_params["params"])
                changed = True
        elif state == 'absent':
            response, http_code = self.delete(f"{child_url}")
            if http_code == 200:
                changed = True
        self.do_exit(response, http_code, changed=changed, msg=msg)

    def process_crd(self, url, mkey=None):
        self.task = "CRD"
        self.url = self.parse_url(url)
        self.mkey = mkey
        self.handle_force_method()
        create_params = self._modify_user_input(self.module.params, self.src_arg_spec, "create")
        mkey_value = self.get_mkey_value(mkey)
        base_url = self.url
        child_url = f"{self.url}/{mkey_value}".rstrip("/")
        state = create_params["state"]
        response, http_code = {}, -1
        changed = False
        msg = None
        if state == 'present':
            response, http_code = self.read(f"{child_url}")
            if http_code == 200:
                if self.check_need_update(create_params["params"], response):
                    # delete and create
                    response, http_code = self.delete(f"{child_url}")
                    response, http_code = self.create(f"{base_url}", data=create_params["params"])
                    changed = True
                else:
                    msg = "Local data is the same as remote data. Skipped update. To force update, set 'force_method: update'."
            else:
                response, http_code = self.create(f"{base_url}", data=create_params["params"])
                changed = True
        elif state == 'absent':
            response, http_code = self.delete(f"{child_url}")
            if http_code == 200:
                changed = True
        self.do_exit(response, http_code, changed=changed, msg=msg)

    def process_ru(self, url):
        self.task = "RU"
        self.url = self.parse_url(url)
        self.handle_force_method()
        update_params = self._modify_user_input(self.module.params, self.src_arg_spec, "update")
        state = update_params["state"]
        if state == "absent":
            self.module.fail_json(msg="This module can not delete resource. And 'state: absent' is not supported.")
        changed = False
        msg = None
        response, http_code = self.read(self.url)
        if http_code == 200:
            if self.check_need_update(update_params["params"], response):
                response, http_code = self.update(self.url, data=update_params["params"])
                changed = True
            else:
                msg = "Local data is the same as remote data. Skipped update. To force update, set 'force_method: update'."
        else:
            response, http_code = self.update(self.url, data=update_params["params"])
            changed = True
        self.do_exit(response, http_code, changed=changed, msg=msg)

    def check_need_update(self, local_data, remote_data):
        """
        Compare local and remote data, return True if need update
        local_data: dict
        remote_data: dict or list, if list, check first element
        """
        def _is_different(local_data, remote_data):
            # check based on local_data type
            if isinstance(local_data, dict):
                if not isinstance(remote_data, dict):
                    return True
                for key, value in local_data.items():
                    if key in remote_data:
                        if _is_different(value, remote_data[key]):
                            return True
                    else:
                        return True
            elif isinstance(local_data, list):
                if not isinstance(remote_data, list):
                    return True
                if len(local_data) != len(remote_data):
                    return True
                try:
                    if str(sorted(local_data)) != str(sorted(remote_data)):
                        return True
                except Exception:
                    return True
            else:
                if isinstance(local_data, (int, float)) and isinstance(remote_data, (int, float)):
                    return local_data != remote_data
                return str(local_data) != str(remote_data)
            return False

        # preprocess data
        if isinstance(remote_data, list):
            if len(remote_data) == 1:
                remote_data = remote_data[0]
            else:
                return True
        # params in url also considered as remote data, only for compare purpose
        for param in self.params_in_url:
            if param in local_data and param not in remote_data and isinstance(local_data[param], str):
                remote_data[param] = local_data[param]
        return _is_different(local_data, remote_data)

    def get_mkey_value(self, mkey):
        if not mkey or "params" not in self.module.params:
            return ""
        if mkey not in self.module.params["params"]:
            return ""
        mkey_value = self.module.params["params"][mkey]
        if not mkey_value:
            return ""
        return mkey_value

    def parse_url(self, url):
        params_in_url = [item.replace("{", "").replace("}", "") for item in url.split("/") if item.startswith("{") and item.endswith("}")]
        self.params_in_url = params_in_url
        for param in params_in_url:
            url = url.replace("{" + param + "}", self.module.params["params"][param])
        return url

    def create(self, url, data):
        """Send POST request (create)"""
        if self.module.check_mode:
            self.module.exit_json(changed=True, response=data, msg="Check mode is enabled. Data will be created in remote server if not in check mode.")
        response, http_code = self.connection.send_request("POST", path=url, data=data)
        return response, http_code

    def read(self, url):
        """Send GET request (read)"""
        response, http_code = self.connection.send_request("GET", path=url)
        return response, http_code

    def update(self, url, data):
        """Send PUT request (update)"""
        if self.module.check_mode:
            self.module.exit_json(changed=True, response=data, msg="Check mode is enabled. Data will be updated in remote server if not in check mode.")
        response, http_code = self.connection.send_request("PUT", path=url, data=data)
        return response, http_code

    def delete(self, url):
        """Send DELETE request (delete)"""
        if self.module.check_mode:
            self.module.exit_json(changed=True, response={"url": url}, msg="Check mode is enabled. Data will be deleted in remote server if not in check mode.")
        response, http_code = self.connection.send_request("DELETE", path=url)
        return response, http_code

    def do_exit(self, response, http_code, changed=False, msg=None):
        """Exit the module with the response"""
        if http_code != 200:
            changed = False
            error_msg = response.get("error", {}).get("message", "")
            self.module.fail_json(msg=error_msg, http_code=http_code, response=response)
        self.module.exit_json(changed=changed, http_code=http_code, response=response, msg=msg)


def modify_argument_spec(metadata):
    """
    Modify the argument spec based on the bypass_validation parameter.
    If bypass_validation is True, the params argument spec will be removed.
    """

    def get_bypass(params):
        bypass = params.get('bypass_validation', False)
        if isinstance(bypass, bool):
            return bypass
        elif isinstance(bypass, str):
            return bypass.lower() in ['true', 'y', 'yes', 't', '1', 'on']
        elif isinstance(bypass, int):
            return bypass != 0
        return True

    def get_argument_spec(metadata):
        if not isinstance(metadata, dict):
            return metadata
        argument_spec = {}
        # remove api_name since this is used for internal only
        for key in metadata:
            if key not in ["api_name", "only_in"]:
                argument_spec[key] = get_argument_spec(metadata[key])
        return argument_spec

    params = _load_params()  # This function doesn't return params' default value.
    # if params is None, it probably means sanity-test
    if not params or not isinstance(params, dict):
        return get_argument_spec(metadata)
    is_bypass = get_bypass(params)
    if is_bypass:
        top_level_schema = {}
        for key in metadata:
            if key != "params":
                top_level_schema[key] = metadata[key]
            elif not params.get("params", None) or isinstance(params["params"], dict):
                top_level_schema["params"] = {"type": "dict"}
            elif isinstance(params["params"], list):
                top_level_schema["params"] = {"type": "list"}
        return top_level_schema

    argument_spec = get_argument_spec(metadata)
    return argument_spec


def raise_connection_error(module, start_error_msg="", end_error_msg=""):
    """Validate connection mode and network OS settings"""
    error_template = """
{start_error_msg}

Please ensure your playbook and inventory file are configured correctly:

1. Your playbook (example.yml):
   - name: Your playbook name
     hosts: fortisase
     gather_facts: false
     tasks:
       - name: Your task
         fortinet.fortisase.<task_name>:
           state: present
           other_param: value

2. Your inventory file (inventory.ini):
    [fortisase]
    public_cloud ansible_host=portal.prod.fortisase.com

    [fortisase:vars]
    # Set network OS for FortiSASE httpapi plugin
    ansible_network_os=fortinet.fortisase.fortisase
    ansible_connection=httpapi
    # Authentication credentials
    ansible_user="your_username"
    ansible_password="your_password"
    # Connection settings
    ansible_httpapi_port=443
    ansible_httpapi_use_ssl=true
    ansible_httpapi_validate_certs=false

3. Run ansible-playbook -i inventory.ini 'path/to/example.yml'

{end_error_msg}
"""
    module.fail_json(msg=error_template.format(start_error_msg=start_error_msg,
                                               end_error_msg=end_error_msg).strip())


def validate_ansible_os(module, connection):
    # Check ansible_network_os setting
    network_os = None
    # Try to get network_os from multiple possible sources
    for env_var in ['ANSIBLE_NETWORK_OS', 'ansible_network_os']:
        if env_var in os.environ:
            network_os = os.environ[env_var]
            break
    # If not in environment variables, try to get from connection
    if not network_os and connection:
        # Try to get connection options
        if hasattr(connection, 'get_option'):
            network_os = connection.get_option('network_os')

    if network_os != 'fortinet.fortisase.fortisase':
        start_error_msg = f"""
ansible_network_os is not configured correctly!

Current setting: {network_os or 'Not set'}
Required setting: fortinet.fortisase.fortisase
"""
        raise_connection_error(module, start_error_msg)
