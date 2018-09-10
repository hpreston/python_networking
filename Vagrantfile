# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Create IOS XE Node
  config.vm.define "iosxe1" do |node|
    node.vm.box = "iosxe/16.09.01"

    # nic_type: "virtio" needed for IOS XE 16.7+
    node.vm.network :private_network, virtualbox__intnet: "link1", auto_config: false, nic_type: "virtio"
    node.vm.network :private_network, virtualbox__intnet: "link2", auto_config: false, nic_type: "virtio"

    node.vm.network :forwarded_port, protocol: 'udp', guest: 161, host: 2227, id: 'snmp', auto_correct: true

    # Vagrant 2.1.0 or higher
    # node.trigger.after :up do |trigger|
    #   trigger.info = "Running baseline script"
    #   trigger.run = {path: "vagrant_device_setup.py"}
    # end

  end

end
