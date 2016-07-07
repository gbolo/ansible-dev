provider "vsphere" {
    user                 = "${var.vsphere.user}"
    vsphere_server       = "${var.vsphere.server}"
    password             = "${var.vsphere.pass}"
    allow_unverified_ssl = true
}


# Create Ansible Server
resource "vsphere_virtual_machine" "ansible" {
  count        = 1
  name         = "${var.ansible.name}"
  folder       = "${var.ansible.folder}"
  vcpu         = "${var.ansible.vcpu}"
  memory       = "${var.ansible.memory}"
  datacenter   = "${var.ansible.datacenter}"
  cluster      = "${var.ansible.cluster}"
  domain       = "${var.ansible.domain}"
  dns_suffixes = ["${var.ansible.domain}"]
  dns_servers  = ["${var.ansible.dns1}","${var.ansible.dns2}","${var.ansible.dns3}"]
  time_zone    = "America/Toronto"
  gateway      = "${var.ansible.gateway}"

  network_interface {
    label              = "${var.ansible.network}"
    ipv4_address       = "${var.ansible.ip}"
    ipv4_prefix_length = "${var.ansible.prefix}"
  }

  disk {
    template  = "${var.ansible.template}"
    datastore = "${var.ansible.datastore}"
  }

}
