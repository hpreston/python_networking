#! /usr/bin/env python
"""Sample use of the ncclient library for NETCONF

This script will delete configuration on a device.

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

# Import libraries
from ncclient import manager
from xml.dom import minidom
import xmltodict
import sys

# Add parent directory to path to allow importing common vars
sys.path.append("..") # noqa
from device_info import ios_xe1 as device # noqa

# New Loopback Details
loopback = {"int_name": "Loopback102",
            "description": "Demo interface by NETCONF",
            "ip": "192.168.102.1",
            "netmask": "255.255.255.0"}


# Create config template for an interface
config_data = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface operation="delete">
        <name>{int_name}</name>
      </interface>
  </interfaces>
</config>
"""

# Open NETCONF connection to device
with manager.connect(host = device["address"],
                     port = device["netconf_port"],
                     username = device["username"],
                     password = device["password"],
                     hostkey_verify = False) as m:

    # Create desired NETCONF config payload and <edit-config>
    config = config_data.format(**loopback)
    r = m.edit_config(target = "running", config = config)

    # Print OK status
    print("NETCONF RPC OK: {}".format(r.ok))
