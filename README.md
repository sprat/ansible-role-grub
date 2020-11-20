Ansible Role: grub
==================

[![Ansible Galaxy][galaxy_image]][galaxy_link]
[![Build Status][travis_image]][travis_link]

Configure Grub on Ubuntu or Debian

Requirements
------------

None.

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: server
  roles:
    - role: sprat.grub
```

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Sylvain Prat](https://github.com/sprat).


[travis_image]:  https://travis-ci.com/sprat/ansible-role-grub.svg?branch=master
[travis_link]:   https://travis-ci.com/sprat/ansible-role-grub
[galaxy_image]:  https://img.shields.io/badge/galaxy-sprat.grub-660198.svg?style=flat
[galaxy_link]:   https://galaxy.ansible.com/sprat/grub
