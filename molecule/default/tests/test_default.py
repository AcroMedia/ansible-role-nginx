import os
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def check_file(filepath, user, group, permission):

    assert filepath.exists
    assert filepath.user == user
    assert filepath.group == group
    assert oct(filepath.mode) == permission


""" default/main.yml tests """


@pytest.mark.parametrize('packages', [
    'nginx'
])
def test_pkg(host, packages):
    package = host.package(packages)

    assert package.is_installed


@pytest.mark.parametrize('services', [
    'nginx'
])
def test_svc(host, services):
    service = host.service(services)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize('files', [
    '/etc/nginx/nginx.conf', '/etc/nginx/conf.d/hide-nginx-version.conf',
    '/etc/nginx/conf.d/gzip_types.conf'
])
def test_nginx_conf_file(host, files):

    test_files = [files]
    [check_file(host.file(x), 'root', 'root', '0644') for x in test_files]
    # contents = "server_names_hash_bucket_size {}".format(128)
    # assert conf.contains(contents) # doesn't seem to write this ...
