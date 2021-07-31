import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dependencies_installed(host):
    assert host.package("crontabs").is_installed
    assert host.package("zip").is_installed
    assert host.package("unzip").is_installed


def test_monitor_file(host):
    assert host.file("/opt/aws-scripts-mon").is_directory

    file = host.file("/opt/aws-scripts-mon/mon-put-instance-data.pl")
    assert file.is_file
    assert file.size > 0
