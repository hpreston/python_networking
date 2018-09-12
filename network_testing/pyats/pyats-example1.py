#! /usr/bin/env python
"""Sample use of the pyATS library.

This script will connects to a device and makes several queries.

The commands are intended to be executed from within an interactive interpreter. 

Copyright (c) 2018 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# Import in pyATS libraries and tools
from genie.conf import Genie
from ats.topology import loader
from genie.abstract import Lookup
from genie.libs import ops # noqa

# Read and process the testbed (inventory) file
genie_testbed = Genie.init("./default_testbed.yaml")

# Create a pyATS device object from testbed
vagrant_iosxe1 = genie_testbed.devices["vagrant-iosxe1"]

# Connect to the device
vagrant_iosxe1.connect()

# Create an abstract device to standardize Python API and code for platform
vagrant_iosxe1_abstract = Lookup.from_device(vagrant_iosxe1)

# Using the absract device, learn about the Interfaces on the end device
vagrant_iosxe1_interfaces = vagrant_iosxe1_abstract.ops.interface.interface.Interface(vagrant_iosxe1)
vagrant_iosxe1_interfaces.learn()

# Print out the interface details that were learned
vagrant_iosxe1_interfaces.info

# Display a single interface from the device
vagrant_iosxe1_interfaces.info["GigabitEthernet1"]

# Print the mac address for the interface
vagrant_iosxe1_interfaces.info["GigabitEthernet1"]["mac_address"]

# Notice that there was no parsing of command line output needed to access this data

# Execute a command on the device and print the output
print(vagrant_iosxe1.execute("show version"))

# Or store the output into a variable
version = vagrant_iosxe1.execute("show version")

# Send a configuration command to the
vagrant_iosxe1.configure("ntp server 10.10.10.10")

# Create a configuration command list and send to the device
config_loopback = [
                    "interface Loopback201",
                    "description Configured by pyATS",
                    "ip address 172.16.201.1 255.255.255.0",
                    "no shut"
                  ]
vagrant_iosxe1.configure(config_loopback)

# Re-learn the interfaces
vagrant_iosxe1_interfaces = vagrant_iosxe1_abstract.ops.interface.interface.Interface(vagrant_iosxe1)
vagrant_iosxe1_interfaces.learn()

# Get details about new interface
vagrant_iosxe1_interfaces.info["Loopback201"]

# Disconnect from the devices
vagrant_iosxe1.disconnect()
