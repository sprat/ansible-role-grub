import os

import testinfra.utils.ansible_runner

here = os.path.dirname(__file__)
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_grub_d_files(host):
    """Check that the /etc/default/grub.d/ files are added or removed properly"""
    assert host.file('/etc/default/grub.d/99-docker.cfg').exists
    assert not host.file('/etc/default/grub.d/98-audit.cfg').exists


def test_grub_config_regenerated(host):
    """Check that the grub config is regenerated"""
    grub_cfg = host.file('/boot/grub/grub.cfg')
    assert grub_cfg.contains(' cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1 swapaccount=1 ')
