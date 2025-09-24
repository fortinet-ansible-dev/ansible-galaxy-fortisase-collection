# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
name: fortisase
author:
    - Xinwei Du (@dux-fortinet)
short_description: HttpApi Plugin for FortiSASE
description:
  - This HttpApi plugin provides methods to connect to FortiSASE API endpoints.
version_added: "1.0.0"
"""

import json
import os
import urllib.parse
from urllib.error import HTTPError
from ansible.module_utils.urls import open_url
from ansible.plugins.httpapi import HttpApiBase
from datetime import datetime
import time


class HttpApi(HttpApiBase):
    def __init__(self, connection):
        super(HttpApi, self).__init__(connection)
        self._token = None
        self._enable_log = os.getenv("FORTISASE_ENABLE_LOG", "false").lower() == "true"
        self._log_file = None
        host = "portal.prod.fortisase.com"
        try:
            host = self.connection._play_context.remote_addr or "portal.prod.fortisase.com"
        except AttributeError:
            host = "portal.prod.fortisase.com"
        if not host.startswith(("http://", "https://")):
            host = f"https://{host}"
        self._base_url = host

    def log(self, msg):
        if not self._enable_log:
            return
        if not self._log_file:
            log_path = "/tmp/fortisase.ansible.log"
            self._log_file = open(log_path, "a")
        log_message = str(datetime.now()) + ": " + str(msg) + "\n"
        self._log_file.write(log_message)
        self._log_file.flush()

    def login(self, username, password):
        self.log(f"FortiSASE API base URL: {self._base_url}")
        if not username:
            username = os.getenv("FORTISASE_USERNAME")
        if not password:
            password = os.getenv("FORTISASE_PASSWORD")
        if not username or not password:
            self._token = os.getenv("FORTISASE_ACCESS_TOKEN")
            if self._token:
                self.log("Using token from environment variable FORTISASE_ACCESS_TOKEN")
                return
            if not username:
                raise Exception("Username is not set, please set ansible variable ansible_user or environment variable FORTISASE_USERNAME")
            if not password:
                raise Exception("Password is not set, please set ansible variable ansible_password or environment variable FORTISASE_PASSWORD")
        login_url = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"
        data = {
            "username": username,
            "password": password,
            "client_id": "FortiSASE",
            "client_secret": "",
            "grant_type": "password"
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = open_url(url=login_url,
                                method="POST",
                                headers=headers,
                                data=json.dumps(data),
                                timeout=10)
            response_raw = response.read()
            status = response.getcode()
            response_json = json.loads(response_raw.decode("utf-8"))
            self._token = response_json.get("access_token")
            self.log(f"[LOGIN] STATUS {status}")
        except Exception as e:
            error_mgs = f"Failed to login, please check your ansible_user and ansible_password. Error: {str(e)}"
            self.log(f"[LOGIN] {error_mgs}")
            raise Exception(error_mgs)
        if not self._token:
            error_mgs = "Login failed. Login API doesn't return access token."
            self.log(f"[LOGIN] {error_mgs}")
            raise Exception(error_mgs)
        return

    def logout(self):
        try:
            if self._log_file is not None:
                self.log("Logout")
                self._log_file.close()
                self._log_file = None
        except Exception as e:
            pass
        return

    def send_one_request(self, method, path, data=None):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        masked_headers = headers.copy()
        if self._token:
            headers['Authorization'] = f'Bearer {self._token}'
            masked_headers['Authorization'] = '<masked>'
        body = None
        if data is not None:
            try:
                body = json.dumps(data)
            except Exception as e:
                self.log(f"[{path} ({method})] [Request]  | ERROR {e}")
                return None, None

        path = urllib.parse.quote(path)
        url = self._base_url + path
        self.log(f"[{path} ({method})] [Request]  | HEADERS {masked_headers} | DATA {body}")
        result = {}
        status = None
        try:
            response = open_url(
                url=url,
                method=method,
                headers=headers,
                data=body,
                timeout=10
            )
            raw = response.read()
            status = response.getcode()
            try:
                result = json.loads(raw.decode('utf-8'))
                if "code" in result and "data" in result and len(result) == 2:
                    status = result["code"]
                    result = result["data"]
            except Exception as e:
                self.log(f"[{path} ({method})] [Response] | STATUS {status} | RETURN {raw} | ERROR {e}")
                return None, status
            self.log(f"[{path} ({method})] [Response] | STATUS {status} | RETURN {result}")
            return result, status
        except HTTPError as e:
            try:
                error_body = e.read()
                error_json = json.loads(error_body)
                status = e.getcode()
                self.log(f"[{path} ({method})] [Response] | STATUS {status} | RETURN {error_json} | ERROR {e}")
                return error_json, status
            except Exception:
                self.log(f"[{path} ({method})] [Response] | STATUS {status} | RETURN {error_body} | ERROR {e}")
        except Exception as e:
            self.log(f"[{path} ({method})] [Response] | STATUS {status} | ERROR {e}")
        return result, status

    def send_request(self, method, path, data=None):
        """Send request to FortiSASE API.
        Returns:
            result (dict): Response data, JSON format
            status (int): Status code
        """
        if not self.connection._connected:
            self.connection._connect()  # explicitly call login()

        progress = 0
        result = {}
        status = None
        while progress < 100:
            result, status = self.send_one_request(method, path, data)
            if status == 200:
                break
            if status == 429:
                progress += 10
                self.log(f"[{path} ({method})] [Error: {status}] sleep 2 seconds and retry due to status {status}")
                time.sleep(2)
            if status == 500:
                progress += 30
                self.log(f"[{path} ({method})] [Error: {status}] sleep 2 seconds and retry due to status {status}")
                time.sleep(2)
            break
        return result, status
