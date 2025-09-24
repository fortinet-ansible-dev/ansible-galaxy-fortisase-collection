![Fortinet logo|](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Fortinet_logo.svg/320px-Fortinet_logo.svg.png)

# fortinet.fortisase:1.0.0 - configuring FortiSASE

## Description

FortiSASE Ansible Collection includes the modules that are able to configure FortiSASE.

[Documentation](https://ansible-galaxy-fortisase-docs.readthedocs.io/en/latest) for the collection.

## Requirements

- Ansible 2.17.0 or above
- Python 3.10 - 3.12

## Installation

This collection is distributed via [ansible-galaxy](https://galaxy.ansible.com/fortinet/fortisase).


Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install fortinet.fortisase
```

You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:


```yaml
collections:
  - name: fortinet.fortisase
```

Note that if you install any collections from Ansible Galaxy, they will not be upgraded automatically when you upgrade the Ansible package.
To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install fortinet.fortisase --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 1.0.0:

```
ansible-galaxy collection install fortinet.fortisase:==1.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.


## Use Cases

Create a file named `hosts`:

```
[fortisase]
public_cloud ansible_host=portal.prod.fortisase.com
# private_cloud ansible_host=<your_private_cloud_address>

[fortisase:vars]
ansible_network_os=fortinet.fortisase.fortisase
ansible_connection=httpapi
ansible_facts_modules=setup
ansible_httpapi_port=443
ansible_httpapi_use_ssl=true
ansible_httpapi_validate_certs=false
# Authentication credentials (Specify the username and password in the inventory file or in environment variables)
# ansible_user="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # You can also specify the username in environment variable FORTISASE_USERNAME
# ansible_password="123123123123123!1Aa" # You can also specify the password in environment variable FORTISASE_PASSWORD
```

Create a file named `test.yml`:

```
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
```

Run the playbook:

```
ansible-playbook -i hosts test.yml
```

See [example here](https://ansible-galaxy-fortisase-docs.readthedocs.io/en/latest/playbook.html) to run your first playbook.


## Testing

Testing is done by the Fortinet team.

## Support

For any questions regarding FortiSASE Ansible, please create a [github issue](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortisase-collection/issues).


## Release Notes and Roadmap

Please check [release note here](https://ansible-galaxy-fortisase-docs.readthedocs.io/en/latest/release.html).

FortiSASE Ansible is expected to be updated every two months.


## Related Information

[Documentation](https://ansible-galaxy-fortisase-docs.readthedocs.io/en/latest) for the collection.

## Modules
The collection provides the following modules:



## License Information

FortiAnalyzer Ansible Collection follows [GNU General Public License v3.0](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortisase-collection/blob/main/LICENSE).