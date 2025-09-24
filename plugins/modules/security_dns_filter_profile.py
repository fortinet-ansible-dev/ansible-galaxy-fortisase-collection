#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: security_dns_filter_profile
short_description: DNS Filter Profile Resource
description:
  - DNS Filter Profile Resource.
  - Use API "/resource-api/v2/security/dns-filter-profile/{direction}/{primaryKey}".
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
            useForEdgeDevices:
                type: bool
                description: no description
            useFortiguardFilters:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            enableAllLogs:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            enableBotnetBlocking:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            enableSafeSearch:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            allowDnsRequestsOnRatingError:
                type: str
                description: no description
                choices:
                    - "disable"
                    - "enable"
            dnsTranslationEntries:
                type: list
                description: no description
                elements: dict
                suboptions:
                    src:
                        type: str
                        description: no description
                    dst:
                        type: str
                        description: no description
                    netmask:
                        type: str
                        description: no description
                    status:
                        type: str
                        description: no description
                        choices:
                            - "disable"
                            - "enable"
            domainFilters:
                type: list
                description: no description
                elements: dict
                suboptions:
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
                    enabled:
                        type: bool
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
            domainThreatFeedFilters:
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
"""

EXAMPLES = """
- name: Update security dns filter profile
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
    - name: Update security dns filter profile
      fortinet.fortisase.security_dns_filter_profile:
        params:
          direction: "{{ direction }}"
          primaryKey: "{{ profile_group }}"
          useForEdgeDevices: false
          allowDnsRequestsOnRatingError: "enable"
          dnsTranslationEntries: []
          domainFilters: []
          domainThreatFeedFilters: []
          enableAllLogs: "disable"
          enableBotnetBlocking: "enable"
          enableSafeSearch: "disable"
          useFortiguardFilters: "enable"
          fortiguardFilters:
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Alternative Beliefs
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Abortion
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Other Adult Materials
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Advocacy Organizations
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Gambling
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Extremist Groups
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Nudity and Risque
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Pornography
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Dating
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: "Weapons (Sales)"
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Unrated
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Marijuana
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Sex Education
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Alcohol
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Tobacco
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Lingerie and Swimsuit
            - action: monitor
              category:
                datasource: security/fortiguard-categories
                primaryKey: Sports Hunting and War Games
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Malicious Websites
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Phishing
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Spam URLs
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Dynamic DNS
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Newly Observed Domain
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Newly Registered Domain
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Terrorism
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Crypto Mining
            - action: block
              category:
                datasource: security/fortiguard-categories
                primaryKey: Potentially Unwanted Program
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Drug Abuse
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Hacking
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Illegal or Unethical
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Discrimination
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Explicit Violence
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Proxy Avoidance
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Plagiarism
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Child Sexual Abuse
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Freeware and Software Downloads
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: File Sharing and Storage
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Streaming Media and Download
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Peer-to-peer File Sharing
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Internet Radio and TV
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Internet Telephony
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Advertising
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Brokerage and Trading
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Games
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Web-based Email
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Entertainment
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Arts and Culture
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Education
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Health and Wellness
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Job Search
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Medicine
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: News and Media
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Social Networking
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Political Organizations
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Reference
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Global Religion
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Shopping
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Society and Lifestyles
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Sports
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Travel
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Personal Vehicles
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Dynamic Content
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Meaningless Content
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Folklore
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Web Chat
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Instant Messaging
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Newsgroups and Message Boards
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Digital Postcards
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Child Education
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Real Estate
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Restaurant and Dining
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Personal Websites and Blogs
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Content Servers
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Domain Parking
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Personal Privacy
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Auction
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Finance and Banking
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Search Engines and Portals
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: General Organizations
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Business
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Information and Computer Security
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Government and Legal Organizations
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Information Technology
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Armed Forces
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Web Hosting
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Secure Websites
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Web-based Applications
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Charitable Organizations
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Remote Access
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Web Analytics
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Online Meeting
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: URL Shortening
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Artificial Intelligence Technology
            - action: allow
              category:
                datasource: security/fortiguard-categories
                primaryKey: Cryptocurrency
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
    url = "/resource-api/v2/security/dns-filter-profile/{direction}/{primaryKey}"
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
                "useForEdgeDevices": {"type": "bool"},
                "useFortiguardFilters": {"type": "str", "choices": ["disable", "enable"]},
                "enableAllLogs": {"type": "str", "choices": ["disable", "enable"]},
                "enableBotnetBlocking": {"type": "str", "choices": ["disable", "enable"]},
                "enableSafeSearch": {"type": "str", "choices": ["disable", "enable"]},
                "allowDnsRequestsOnRatingError": {"type": "str", "choices": ["disable", "enable"]},
                "dnsTranslationEntries": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "src": {"type": "str"},
                        "dst": {"type": "str"},
                        "netmask": {"type": "str"},
                        "status": {"type": "str", "choices": ["disable", "enable"]}
                    }
                },
                "domainFilters": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "url": {"type": "str"},
                        "type": {"type": "str", "choices": ["regex", "simple", "wildcard"]},
                        "action": {"type": "str", "choices": ["allow", "block", "exempt", "monitor"]},
                        "enabled": {"type": "bool"}
                    }
                },
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
                        }
                    }
                },
                "domainThreatFeedFilters": {
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
