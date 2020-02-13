# ansible-role-nginx

Install and configure NGINX for acro hosting environments

## Requirements

* Ubuntu 14.04+ or RedHat/CentOS 6+
* Your playbook must gather facts

## Role Variables

**nginx_server_names_hash_bucket_size**: The role sets this to 128. On shared servers, the built-in nginx default for this is usually too small.

**nginx_robots_policy**: Can be one of  'development', 'staging', or 'production'. When defined, the role creates an include file meant to be consumed by virtual hosts on the machine.  If value is set to 'staging' or 'development', and when a virtual host includes the file, requests for /robots.txt on the virtual host will be served with a 'deny all' robots policy, no matter what the local /robots.txt contains on the virtual host. This way, projects don't need to keep a separate robots files for different environments. It should be mentioned that robots offers no significant protection from indexing. Search engines generally do whatever they want anyway. So if you really don't want your dev/staging site indexed, put it behind basic http auth, or a firewall.

**nginx_global_username** / **nginx_global_password**: Put a http basic auth username / password prompt in front of all sites on a server. Intended as a simple but extremely effective measure for keeping seach engines from being able index your staging server. Anonymous access can be restored to specific sites or locations by adding `auth_basic: off;` at any level, which overrides the directive set by the role at the global level. See other nginx_auth_* variables in defaults/main.yml.

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
      vars:
        nginx_robots_policy: production
```

## Testing with Molecule

See [tests.README.md](./tests.README.md)

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/
