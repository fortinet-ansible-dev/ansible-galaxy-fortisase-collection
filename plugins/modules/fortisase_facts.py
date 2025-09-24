#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
---
module: fortisase_facts
short_description: Get FortiSASE Facts
description: Get FortiSASE Facts.
version_added: "1.0.0"
author:
    - Xinwei Du (@dux-fortinet)
options:
    selector:
        description: The selector of the facts.
        type: str
        required: true
        choices:
            - 'endpoints_access_proxy'
            - 'endpoints_client_user_details'
            - 'endpoints_details'
            - 'endpoints_donut'
            - 'endpoints_endpoints_with_software'
            - 'endpoints_groups'
            - 'endpoints_software'
            - 'endpoints_software_on_client_user'
            - 'endpoints_software_on_endpoint'
            - 'endpoints_uid_tags'
            - 'endpoints_users'
            - 'endpoints_vulnerabilities'
            - 'endpoints_vulnerabilities_endpoints'
            - 'endpoints_ztna_count'
            - 'endpoints_ztna_tags'
            - 'security_botnet_domains'
            - 'security_botnet_domains_stat'
            - 'traffic_history'
            - 'traffic_history_vpn_connections'
            - 'user_swg_sessions'
            - 'user_vpn_sessions'
            - 'auth_fsso_agents'
            - 'auth_ldap_servers'
            - 'auth_radius_servers'
            - 'auth_swg_saml_server'
            - 'auth_user_groups'
            - 'auth_users'
            - 'auth_vpn_saml_server'
            - 'dem_custom_saas_apps'
            - 'dem_spa_applications'
            - 'endpoint_connection_profiles'
            - 'endpoint_fsso_profiles'
            - 'endpoint_group_ad_user_profiles'
            - 'endpoint_group_invitation_codes'
            - 'endpoint_policies'
            - 'endpoint_protection_profiles'
            - 'endpoint_sandbox_profiles'
            - 'endpoint_setting_profiles'
            - 'endpoint_ztna_profiles'
            - 'endpoint_ztna_rules'
            - 'endpoint_ztna_tags'
            - 'infra_extenders'
            - 'infra_fortigates'
            - 'infra_ssids'
            - 'network_basic_internet_services'
            - 'network_dns_rules'
            - 'network_host_groups'
            - 'network_hosts'
            - 'network_implicit_dns_rules'
            - 'network_internet_services'
            - 'network_wildcard_fqdn_customs'
            - 'security_antivirus_filetypes'
            - 'security_antivirus_profile'
            - 'security_antivirus_profiles'
            - 'security_app_custom_signatures'
            - 'security_application_categories'
            - 'security_application_control_profile'
            - 'security_application_control_profiles'
            - 'security_applications'
            - 'security_dlp_data_types'
            - 'security_dlp_dictionaries'
            - 'security_dlp_exact_data_matches'
            - 'security_dlp_file_patterns'
            - 'security_dlp_fingerprint_databases'
            - 'security_dlp_profile'
            - 'security_dlp_profiles'
            - 'security_dlp_sensors'
            - 'security_dns_filter_profile'
            - 'security_dns_filter_profiles'
            - 'security_domain_threat_feeds'
            - 'security_endpoint_to_endpoint_policies'
            - 'security_file_filter_profile'
            - 'security_file_filter_profiles'
            - 'security_fortiguard_categories'
            - 'security_fortiguard_local_categories'
            - 'security_geoip_countries'
            - 'security_internal_policies'
            - 'security_internal_reverse_policies'
            - 'security_ip_threat_feeds'
            - 'security_ips_custom_signatures'
            - 'security_ips_profile'
            - 'security_ips_profiles'
            - 'security_onetime_schedules'
            - 'security_outbound_policies'
            - 'security_profile_group'
            - 'security_profile_groups'
            - 'security_recurring_schedules'
            - 'security_schedule_groups'
            - 'security_service_categories'
            - 'security_service_groups'
            - 'security_services'
            - 'security_ssl_ssh_profile'
            - 'security_ssl_ssh_profiles'
            - 'security_url_threat_feeds'
            - 'security_video_filter_fortiguard_categories'
            - 'security_video_filter_profile'
            - 'security_video_filter_profiles'
            - 'security_video_filter_youtube_key'
            - 'security_web_filter_profile'
            - 'security_web_filter_profiles'
            - 'usage_auth_fsso_agents'
            - 'usage_auth_ldap_servers'
            - 'usage_auth_radius_servers'
            - 'usage_auth_user_groups'
            - 'usage_endpoint_ztna_tags'
            - 'usage_infra_ssids'
            - 'usage_network_host_groups'
            - 'usage_network_hosts'
            - 'usage_security_app_custom_signatures'
            - 'usage_security_dlp_dictionaries'
            - 'usage_security_dlp_exact_data_matches'
            - 'usage_security_dlp_file_patterns'
            - 'usage_security_dlp_fingerprint_databases'
            - 'usage_security_dlp_sensors'
            - 'usage_security_domain_threat_feeds'
            - 'usage_security_endpoint_to_endpoint_policies'
            - 'usage_security_fortiguard_local_categories'
            - 'usage_security_internal_policies'
            - 'usage_security_internal_reverse_policies'
            - 'usage_security_ip_threat_feeds'
            - 'usage_security_ips_custom_signatures'
            - 'usage_security_onetime_schedules'
            - 'usage_security_outbound_policies'
            - 'usage_security_profile_group'
            - 'usage_security_recurring_schedules'
            - 'usage_security_schedule_groups'
            - 'usage_security_service_groups'
            - 'usage_security_services'
            - 'usage_security_url_threat_feeds'
            - 'private_access_network_configuration'
            - 'private_access_service_connections'
            - 'security_cert_local_certs'
            - 'security_cert_remote_ca_certs'
            - 'security_pki_users'
    params:
        description: The params of the facts. Different selectors have different required params.
        type: dict
"""

EXAMPLES = """
- name: Get FortiSASE Facts
  hosts: fortisase
  gather_facts: false
  tasks:
    - name: Query one network dns rule
      fortinet.fortisase.fortisase_facts:
        selector: "network_dns_rules"
        params:
          primaryKey: "1"
    - name: Query all network dns rules
      fortinet.fortisase.fortisase_facts:
        selector: "network_dns_rules"
        params:
          primaryKey: null
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


def main():
    facts_schema = {
        "endpoints_access_proxy": "/monitor-api/v1/endpoints/access-proxy",
        "endpoints_client_user_details": "/monitor-api/v1/endpoints/client-user-details/{clientUserId}",
        "endpoints_details": "/monitor-api/v1/endpoints/details/{deviceId}",
        "endpoints_donut": "/monitor-api/v1/endpoints/donut/{donutType}",
        "endpoints_endpoints_with_software": "/monitor-api/v1/endpoints/endpoints-with-software/{softwareId}",
        "endpoints_groups": "/monitor-api/v1/endpoints/groups/{primaryKey}",
        "endpoints_software": "/monitor-api/v1/endpoints/software",
        "endpoints_software_on_client_user": "/monitor-api/v1/endpoints/software-on-client-user/{clientUserId}",
        "endpoints_software_on_endpoint": "/monitor-api/v1/endpoints/software-on-endpoint/{deviceId}",
        "endpoints_uid_tags": "/monitor-api/v1/endpoints/uid-tags",
        "endpoints_users": "/monitor-api/v1/endpoints/users",
        "endpoints_vulnerabilities": "/monitor-api/v1/endpoints/vulnerabilities",
        "endpoints_vulnerabilities_endpoints": "/monitor-api/v1/endpoints/vulnerabilities/{vulnerabilityId}/endpoints",
        "endpoints_ztna_count": "/monitor-api/v1/endpoints/ztna-count",
        "endpoints_ztna_tags": "/monitor-api/v1/endpoints/ztna-tags",
        "security_botnet_domains": "/monitor-api/v1/security/botnet-domains",
        "security_botnet_domains_stat": "/monitor-api/v1/security/botnet-domains/stat",
        "traffic_history": "/monitor-api/v1/traffic-history",
        "traffic_history_vpn_connections": "/monitor-api/v1/traffic-history/vpn-connections",
        "user_swg_sessions": "/monitor-api/v1/user/swg/sessions",
        "user_vpn_sessions": "/monitor-api/v1/user/vpn/sessions",
        "auth_fsso_agents": "/resource-api/v2/auth/fsso-agents/{primaryKey}",
        "auth_ldap_servers": "/resource-api/v2/auth/ldap-servers/{primaryKey}",
        "auth_radius_servers": "/resource-api/v2/auth/radius-servers/{primaryKey}",
        "auth_swg_saml_server": "/resource-api/v2/auth/swg-saml-server",
        "auth_user_groups": "/resource-api/v2/auth/user-groups/{primaryKey}",
        "auth_users": "/resource-api/v2/auth/users/{primaryKey}",
        "auth_vpn_saml_server": "/resource-api/v2/auth/vpn-saml-server",
        "dem_custom_saas_apps": "/resource-api/v2/dem/custom-saas-apps/{primaryKey}",
        "dem_spa_applications": "/resource-api/v2/dem/spa-applications/{primaryKey}",
        "endpoint_connection_profiles": "/resource-api/v2/endpoint/connection-profiles/{primaryKey}",
        "endpoint_fsso_profiles": "/resource-api/v2/endpoint/fsso-profiles/{primaryKey}",
        "endpoint_group_ad_user_profiles": "/resource-api/v2/endpoint/group-ad-user-profiles/{primaryKey}",
        "endpoint_group_invitation_codes": "/resource-api/v2/endpoint/group-invitation-codes/{primaryKey}",
        "endpoint_policies": "/resource-api/v2/endpoint/policies/{primaryKey}",
        "endpoint_protection_profiles": "/resource-api/v2/endpoint/protection-profiles/{primaryKey}",
        "endpoint_sandbox_profiles": "/resource-api/v2/endpoint/sandbox-profiles/{primaryKey}",
        "endpoint_setting_profiles": "/resource-api/v2/endpoint/setting-profiles/{primaryKey}",
        "endpoint_ztna_profiles": "/resource-api/v2/endpoint/ztna-profiles/{primaryKey}",
        "endpoint_ztna_rules": "/resource-api/v2/endpoint/ztna-rules/{primaryKey}",
        "endpoint_ztna_tags": "/resource-api/v2/endpoint/ztna-tags/{primaryKey}",
        "infra_extenders": "/resource-api/v2/infra/extenders/{primaryKey}",
        "infra_fortigates": "/resource-api/v2/infra/fortigates/{primaryKey}",
        "infra_ssids": "/resource-api/v2/infra/ssids/{primaryKey}",
        "network_basic_internet_services": "/resource-api/v2/network/basic-internet-services/{primaryKey}",
        "network_dns_rules": "/resource-api/v2/network/dns-rules/{primaryKey}",
        "network_host_groups": "/resource-api/v2/network/host-groups/{primaryKey}",
        "network_hosts": "/resource-api/v2/network/hosts/{primaryKey}",
        "network_implicit_dns_rules": "/resource-api/v2/network/implicit-dns-rules/{primaryKey}",
        "network_internet_services": "/resource-api/v2/network/internet-services/{primaryKey}",
        "network_wildcard_fqdn_customs": "/resource-api/v2/network/wildcard-fqdn-customs/{primaryKey}",
        "security_antivirus_filetypes": "/resource-api/v2/security/antivirus-filetypes/{primaryKey}",
        "security_antivirus_profile": "/resource-api/v2/security/antivirus-profile/{direction}/{primaryKey}",
        "security_antivirus_profiles": "/resource-api/v2/security/antivirus-profiles",
        "security_app_custom_signatures": "/resource-api/v2/security/app-custom-signatures/{primaryKey}",
        "security_application_categories": "/resource-api/v2/security/application-categories/{primaryKey}",
        "security_application_control_profile": "/resource-api/v2/security/application-control-profile/{direction}/{primaryKey}",
        "security_application_control_profiles": "/resource-api/v2/security/application-control-profiles",
        "security_applications": "/resource-api/v2/security/applications/{primaryKey}",
        "security_dlp_data_types": "/resource-api/v2/security/dlp-data-types/{primaryKey}",
        "security_dlp_dictionaries": "/resource-api/v2/security/dlp-dictionaries/{primaryKey}",
        "security_dlp_exact_data_matches": "/resource-api/v2/security/dlp-exact-data-matches/{primaryKey}",
        "security_dlp_file_patterns": "/resource-api/v2/security/dlp-file-patterns/{primaryKey}",
        "security_dlp_fingerprint_databases": "/resource-api/v2/security/dlp-fingerprint-databases/{primaryKey}",
        "security_dlp_profile": "/resource-api/v2/security/dlp-profile/{direction}/{primaryKey}",
        "security_dlp_profiles": "/resource-api/v2/security/dlp-profiles",
        "security_dlp_sensors": "/resource-api/v2/security/dlp-sensors/{primaryKey}",
        "security_dns_filter_profile": "/resource-api/v2/security/dns-filter-profile/{direction}/{primaryKey}",
        "security_dns_filter_profiles": "/resource-api/v2/security/dns-filter-profiles",
        "security_domain_threat_feeds": "/resource-api/v2/security/domain-threat-feeds/{primaryKey}",
        "security_endpoint_to_endpoint_policies": "/resource-api/v2/security/endpoint-to-endpoint-policies/{primaryKey}",
        "security_file_filter_profile": "/resource-api/v2/security/file-filter-profile/{direction}/{primaryKey}",
        "security_file_filter_profiles": "/resource-api/v2/security/file-filter-profiles",
        "security_fortiguard_categories": "/resource-api/v2/security/fortiguard-categories/{primaryKey}",
        "security_fortiguard_local_categories": "/resource-api/v2/security/fortiguard-local-categories/{primaryKey}",
        "security_geoip_countries": "/resource-api/v2/security/geoip-countries/{primaryKey}",
        "security_internal_policies": "/resource-api/v2/security/internal-policies/{primaryKey}",
        "security_internal_reverse_policies": "/resource-api/v2/security/internal-reverse-policies/{primaryKey}",
        "security_ip_threat_feeds": "/resource-api/v2/security/ip-threat-feeds/{primaryKey}",
        "security_ips_custom_signatures": "/resource-api/v2/security/ips-custom-signatures/{primaryKey}",
        "security_ips_profile": "/resource-api/v2/security/ips-profile/{direction}/{primaryKey}",
        "security_ips_profiles": "/resource-api/v2/security/ips-profiles",
        "security_onetime_schedules": "/resource-api/v2/security/onetime-schedules/{primaryKey}",
        "security_outbound_policies": "/resource-api/v2/security/outbound-policies/{primaryKey}",
        "security_profile_group": "/resource-api/v2/security/profile-group/{direction}/{primaryKey}",
        "security_profile_groups": "/resource-api/v2/security/profile-groups/{primaryKey}",
        "security_recurring_schedules": "/resource-api/v2/security/recurring-schedules/{primaryKey}",
        "security_schedule_groups": "/resource-api/v2/security/schedule-groups/{primaryKey}",
        "security_service_categories": "/resource-api/v2/security/service-categories/{primaryKey}",
        "security_service_groups": "/resource-api/v2/security/service-groups/{primaryKey}",
        "security_services": "/resource-api/v2/security/services/{primaryKey}",
        "security_ssl_ssh_profile": "/resource-api/v2/security/ssl-ssh-profile/{direction}/{primaryKey}",
        "security_ssl_ssh_profiles": "/resource-api/v2/security/ssl-ssh-profiles",
        "security_url_threat_feeds": "/resource-api/v2/security/url-threat-feeds/{primaryKey}",
        "security_video_filter_fortiguard_categories": "/resource-api/v2/security/video-filter-fortiguard-categories/{primaryKey}",
        "security_video_filter_profile": "/resource-api/v2/security/video-filter-profile/{direction}/{primaryKey}",
        "security_video_filter_profiles": "/resource-api/v2/security/video-filter-profiles",
        "security_video_filter_youtube_key": "/resource-api/v2/security/video-filter-youtube-key",
        "security_web_filter_profile": "/resource-api/v2/security/web-filter-profile/{direction}/{primaryKey}",
        "security_web_filter_profiles": "/resource-api/v2/security/web-filter-profiles",
        "usage_auth_fsso_agents": "/resource-api/v2/usage/auth/fsso-agents/{primaryKey}",
        "usage_auth_ldap_servers": "/resource-api/v2/usage/auth/ldap-servers/{primaryKey}",
        "usage_auth_radius_servers": "/resource-api/v2/usage/auth/radius-servers/{primaryKey}",
        "usage_auth_user_groups": "/resource-api/v2/usage/auth/user-groups/{primaryKey}",
        "usage_endpoint_ztna_tags": "/resource-api/v2/usage/endpoint/ztna-tags/{primaryKey}",
        "usage_infra_ssids": "/resource-api/v2/usage/infra/ssids/{primaryKey}",
        "usage_network_host_groups": "/resource-api/v2/usage/network/host-groups/{primaryKey}",
        "usage_network_hosts": "/resource-api/v2/usage/network/hosts/{primaryKey}",
        "usage_security_app_custom_signatures": "/resource-api/v2/usage/security/app-custom-signatures/{primaryKey}",
        "usage_security_dlp_dictionaries": "/resource-api/v2/usage/security/dlp-dictionaries/{primaryKey}",
        "usage_security_dlp_exact_data_matches": "/resource-api/v2/usage/security/dlp-exact-data-matches/{primaryKey}",
        "usage_security_dlp_file_patterns": "/resource-api/v2/usage/security/dlp-file-patterns/{primaryKey}",
        "usage_security_dlp_fingerprint_databases": "/resource-api/v2/usage/security/dlp-fingerprint-databases/{primaryKey}",
        "usage_security_dlp_sensors": "/resource-api/v2/usage/security/dlp-sensors/{primaryKey}",
        "usage_security_domain_threat_feeds": "/resource-api/v2/usage/security/domain-threat-feeds/{primaryKey}",
        "usage_security_endpoint_to_endpoint_policies": "/resource-api/v2/usage/security/endpoint-to-endpoint-policies/{primaryKey}",
        "usage_security_fortiguard_local_categories": "/resource-api/v2/usage/security/fortiguard-local-categories/{primaryKey}",
        "usage_security_internal_policies": "/resource-api/v2/usage/security/internal-policies/{primaryKey}",
        "usage_security_internal_reverse_policies": "/resource-api/v2/usage/security/internal-reverse-policies/{primaryKey}",
        "usage_security_ip_threat_feeds": "/resource-api/v2/usage/security/ip-threat-feeds/{primaryKey}",
        "usage_security_ips_custom_signatures": "/resource-api/v2/usage/security/ips-custom-signatures/{primaryKey}",
        "usage_security_onetime_schedules": "/resource-api/v2/usage/security/onetime-schedules/{primaryKey}",
        "usage_security_outbound_policies": "/resource-api/v2/usage/security/outbound-policies/{primaryKey}",
        "usage_security_profile_group": "/resource-api/v2/usage/security/profile-group/{direction}/{primaryKey}",
        "usage_security_recurring_schedules": "/resource-api/v2/usage/security/recurring-schedules/{primaryKey}",
        "usage_security_schedule_groups": "/resource-api/v2/usage/security/schedule-groups/{primaryKey}",
        "usage_security_service_groups": "/resource-api/v2/usage/security/service-groups/{primaryKey}",
        "usage_security_services": "/resource-api/v2/usage/security/services/{primaryKey}",
        "usage_security_url_threat_feeds": "/resource-api/v2/usage/security/url-threat-feeds/{primaryKey}",
        "private_access_network_configuration": "/resource-api/v1/private-access/network-configuration",
        "private_access_service_connections": "/resource-api/v1/private-access/service-connections/{service_connection_id}",
        "security_cert_local_certs": "/resource-api/v1/security/cert/local-certs/{primaryKey}",
        "security_cert_remote_ca_certs": "/resource-api/v1/security/cert/remote-ca-certs/{primaryKey}",
        "security_pki_users": "/resource-api/v1/security/pki-users/{primaryKey}",
    }

    argument_spec = {
        "selector": {"type": "str", "required": True, "choices": list(facts_schema.keys())},
        "params": {"type": "dict", "required": False},
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    try:
        agent = FortiSASEAPI(module, src_arg_spec=argument_spec)
        agent.process_facts(facts_schema)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
