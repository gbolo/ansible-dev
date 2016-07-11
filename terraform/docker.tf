# Create Docker Machines

resource "vsphere_virtual_machine" "docker" {
  count        = "${var.docker_count}"
  name         = "${lookup(var.docker_hostname, count.index)}"
  folder       = "${var.vme_docker_default.folder}"
  vcpu         = "${var.vme_docker_default.vcpu}"
  memory       = "${var.vme_docker_default.memory}"
  datacenter   = "${var.vme_default.datacenter}"
  cluster      = "${var.vme_default.cluster}"
  domain       = "${var.vme_default.domain}"
  dns_suffixes = ["${var.vme_default.domain}"]
  dns_servers  = ["${var.vme_default.dns1}","${var.vme_default.dns2}","${var.vme_default.dns3}"]
  time_zone    = "${var.vme_default.time_zone}"
  gateway      = "${var.vme_docker_default.gateway}"

  network_interface {
    label              = "${var.vme_docker_default.network}"
    ipv4_address       = "${lookup(var.docker_ip, count.index)}"
    ipv4_prefix_length = "${var.vme_docker_default.prefix}"
  }

  disk {
    template  = "${var.vme_default.template}"
    datastore = "${var.vme_default.datastore}"
  }

}
