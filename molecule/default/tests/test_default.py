import os

import testinfra.utils.ansible_runner

here = os.path.dirname(__file__)
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test(host):
    assert False
