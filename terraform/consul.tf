# Create Consul Machines

resource "vsphere_virtual_machine" "consul" {
  count        = "${var.consul_count}"
  name         = "${lookup(var.consul_hostname, count.index)}"
  folder       = "${var.vme_consul_default.folder}"
  vcpu         = "${var.vme_consul_default.vcpu}"
  memory       = "${var.vme_consul_default.memory}"
  datacenter   = "${var.vme_default.datacenter}"
  cluster      = "${var.vme_default.cluster}"
  domain       = "${var.vme_default.domain}"
  dns_suffixes = ["${var.vme_default.domain}"]
  dns_servers  = ["${var.vme_default.dns1}","${var.vme_default.dns2}","${var.vme_default.dns3}"]
  time_zone    = "${var.vme_default.time_zone}"
  gateway      = "${var.vme_consul_default.gateway}"

  network_interface {
    label              = "${var.vme_consul_default.network}"
    ipv4_address       = "${lookup(var.consul_ip, count.index)}"
    ipv4_prefix_length = "${var.vme_consul_default.prefix}"
  }

  disk {
    template  = "${var.vme_default.template}"
    datastore = "${var.vme_default.datastore}"
  }

}
