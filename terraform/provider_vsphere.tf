provider "vsphere" {
    user                 = "${var.vsphere_creds.user}"
    vsphere_server       = "${var.vsphere_creds.server}"
    password             = "${var.vsphere_creds.pass}"
    allow_unverified_ssl = true
}
