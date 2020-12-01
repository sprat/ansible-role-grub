Ansible Role: grub
==================

[![Ansible Galaxy][galaxy_image]][galaxy_link]
[![Build Status][travis_image]][travis_link]

Configure Grub on Ubuntu or Debian using the `/etc/default/grub.d` directory.

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
  vars:
    grub_d_files:
      98-docker:  # file to remove if present
      99-audit:
        GRUB_CMDLINE_LINUX_DEFAULT: $GRUB_CMDLINE_LINUX_DEFAULT audit=1
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
