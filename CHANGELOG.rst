================================
Fortinet.Fortisase Release Notes
================================

.. contents:: Topics


v1.0.0
======

Release Summary
---------------

Release 1.0.0

Minor Changes
-------------

- Support 25.3.a FortiSASE schema.

New Plugins
-----------

Httpapi
~~~~~~~

- fortinet.fortisase.fortisase - HttpApi Plugin for FortiSASE

New Modules
-----------

- fortinet.fortisase.auth_fsso_agents - FSSO Agent Resource
- fortinet.fortisase.auth_ldap_servers - LDAP Resource
- fortinet.fortisase.auth_radius_servers - RADIUS Resource
- fortinet.fortisase.auth_swg_saml_server - SWG User SSO Resource
- fortinet.fortisase.auth_user_groups - User Group Resource
- fortinet.fortisase.auth_users - User Resource
- fortinet.fortisase.auth_vpn_saml_server - VPN User SSO Resource
- fortinet.fortisase.dem_custom_saas_apps - DEM Custom SaaS Applications Resource
- fortinet.fortisase.dem_spa_applications - DEM SPA Application Resource
- fortinet.fortisase.endpoint_connection_profiles - Connection Profile Resource
- fortinet.fortisase.endpoint_fsso_profiles - FSSO Profile Resource
- fortinet.fortisase.endpoint_group_ad_user_profiles - Group & AD Users Profile Resource
- fortinet.fortisase.endpoint_group_invitation_codes - Group-Based Invitation Code Resource
- fortinet.fortisase.endpoint_policies - Endpoint Policy Resource
- fortinet.fortisase.endpoint_protection_profiles - Protection Profile Resource
- fortinet.fortisase.endpoint_sandbox_profiles - Sandbox Profile Resource
- fortinet.fortisase.endpoint_setting_profiles - Settings Profile Resource
- fortinet.fortisase.endpoint_ztna_profiles - ZTNA Profile Resource
- fortinet.fortisase.endpoint_ztna_rules - ZTNA Rule Resource
- fortinet.fortisase.endpoint_ztna_tags - ZTNA Tag Resource
- fortinet.fortisase.fortisase_facts - Get FortiSASE Facts
- fortinet.fortisase.fortisase_generic - Send generic FortiSASE API request.
- fortinet.fortisase.infra_ssids - FortiAP SSID Resource
- fortinet.fortisase.network_dns_rules - DNS Rule Resource
- fortinet.fortisase.network_host_groups - Host Group Resource
- fortinet.fortisase.network_hosts - Host Resource
- fortinet.fortisase.network_implicit_dns_rules - Implicit DNS Rule Resource
- fortinet.fortisase.network_internet_services - Internet Service Resource
- fortinet.fortisase.private_access_network_configuration - Secure Private Access Resource
- fortinet.fortisase.private_access_service_connections - Secure Private Access Resource
- fortinet.fortisase.security_antivirus_profile - Antivirus Profile Resource
- fortinet.fortisase.security_app_custom_signatures - Custom Application Signature Resource
- fortinet.fortisase.security_application_control_profile - Application Control Profile Resource
- fortinet.fortisase.security_cert_local_certs - Certificate Resource
- fortinet.fortisase.security_cert_remote_ca_certs - Certificate Resource
- fortinet.fortisase.security_dlp_dictionaries - DLP Dictionary Resource
- fortinet.fortisase.security_dlp_exact_data_matches - DLP Exact Data Match Resource
- fortinet.fortisase.security_dlp_file_patterns - DLP File Pattern Resource
- fortinet.fortisase.security_dlp_fingerprint_databases - DLP Fingerprint Database Resource
- fortinet.fortisase.security_dlp_profile - DLP Profile Resource
- fortinet.fortisase.security_dlp_sensors - DLP Sensor Resource
- fortinet.fortisase.security_dns_filter_profile - DNS Filter Profile Resource
- fortinet.fortisase.security_domain_threat_feeds - Domain Threat Feed Resource
- fortinet.fortisase.security_endpoint_to_endpoint_policies - Endpoint to Endpoint Policy Resource
- fortinet.fortisase.security_file_filter_profile - File Filter Profile Resource
- fortinet.fortisase.security_fortiguard_local_categories - FortiGuard Local Category Resource
- fortinet.fortisase.security_internal_policies - Internal Policy Resource
- fortinet.fortisase.security_internal_reverse_policies - Internal Reverse Policy Resource
- fortinet.fortisase.security_ip_threat_feeds - IP Threat Feed Resource
- fortinet.fortisase.security_ips_custom_signatures - IPS Custom Signature Resource
- fortinet.fortisase.security_ips_profile - IPS Profile Resource
- fortinet.fortisase.security_onetime_schedules - Onetime Schedule Resource
- fortinet.fortisase.security_outbound_policies - Outbound Policy Resource
- fortinet.fortisase.security_pki_users - PKI User Resource
- fortinet.fortisase.security_profile_group - Profile Group Resource
- fortinet.fortisase.security_recurring_schedules - Recurring Schedule Resource
- fortinet.fortisase.security_schedule_groups - Schedule Group Resource
- fortinet.fortisase.security_service_groups - Service Group Resource
- fortinet.fortisase.security_services - Service Resource
- fortinet.fortisase.security_ssl_ssh_profile - SSL Inspection Profile Resource
- fortinet.fortisase.security_url_threat_feeds - URL Threat Feed Resource
- fortinet.fortisase.security_video_filter_profile - Video Filter Profile Resource
- fortinet.fortisase.security_video_filter_youtube_key - Video Filter Youtube API Key Resource
- fortinet.fortisase.security_web_filter_profile - Web Filter Profile Resource
