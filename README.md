Ansible Role: grub
==================

[![Build Status][build_badge]][build_link]
[![Ansible Galaxy][galaxy_badge]][galaxy_link]

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


[build_badge]:  https://travis-ci.com/sprat/ansible-role-grub.svg?branch=master
[build_link]:   https://travis-ci.com/sprat/ansible-role-grub
[galaxy_badge]: https://img.shields.io/ansible/role/52111
[galaxy_link]:  https://galaxy.ansible.com/sprat/grub
