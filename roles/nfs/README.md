Ansible NFS Role
=========

A simple role for redhat/centos based servers to provide/consume nfs services

Role Variables
--------------
All aspects of this role are controled via variables.

### NFS Server
for an NFS server we need to set the variable `nfs_server` to true. Then you can simply define your exports as follows:
```
nfs_server_exports:
  iso:
    src_dir: "/opt/iso"
    src_dir_mode: "0775"
    src_dir_owner: "root"
    src_dir_group: "root"
    acl: "10.0.0.0/8"
    opts: "rw,sync,no_root_squash,no_all_squash"
  www:
    src_dir: "/opt/www"
    src_dir_mode: "0775"
    src_dir_owner: "nginx"
    src_dir_group: "nginx"
    acl: "10.1.1.0/24"
    opts: "rw,sync,no_root_squash,no_all_squash"
```
The directories listed above **do not** need to pre-exist. This role will create them for you.

### NFS Client
for an NFS server we need to set the variable `nfs_client` to true (default setting). Then you can simply define your mounts as follows:
```
nfs_client_mounts:
  iso:
    path: "/mnt/iso"
    mount: "10.1.1.1:/opt/iso"
    fs: "nfs4"
    opts: "defaults"
  www:
    path: "/mnt/www"
    mount: "10.1.1.1:/opt/www"
    fs: "nfs4"
    opts: "defaults"
```
The directories listed above **do not** need to pre-exist. This role will create them for you.

Dependencies
------------

Required rpm packages are installed automatically by this role.


Author and License
-------
`nfs` role written by:
 - George Bolo | [linuxctl.com](https://linuxctl.com)

License: **MIT**

`FREE SOFTWARE, HELL YEAH!`
