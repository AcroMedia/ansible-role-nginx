# ansible-role-nginx

Install and configure NGINX for acro hosting environments


## Requirements

* Ubuntu 14.04+ or RedHat/CentOS 6+
* Your playbook must gather facts

## Role Variables

See defaults/main.yml

## Dependencies

None

## Example Playbook
```yaml
---
- hosts: servers
  become: true
  gather_facts: true
  roles:
    - name: Install NGINX
      role: acromedia.nginx
```

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/
