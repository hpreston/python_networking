#! /usr/bin/env python
"""Sample use of the ncclient library for NETCONF

This script will retrieve information from a device.

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
import yaml, xmltodict

# Open and read in the mgmt IPs for the demo infrastructure
with open("../../setup/default_inventory.yaml") as f:
    devices = yaml.load(f.read())["all"]["children"]
    core1_ip = devices["core"]["hosts"]["core1"]["ansible_host"]
    username, password = "cisco", "cisco"

# Create filter template for an interface
interface_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>{int_name}</name>
    </interface>
  </interfaces>
</filter>
"""

# Open NETCONF connection to device
with manager.connect(host=core1_ip,
                    username=username,
                    password=password,
                    hostkey_verify=False) as m:

    # Create desired NETCONF filter and <get-config>
    filter = interface_filter.format(int_name = "GigabitEthernet2")
    r = m.get_config("running", filter)

    # Pretty print raw xml to screen
    xml_doc = minidom.parseString(r.xml)
    print(xml_doc.toprettyxml(indent = "  "))

    # Process the XML data into Python Dictionary and use
    interface = xmltodict.parse(r.xml)
    interface = interface["rpc-reply"]["data"]["interfaces"]["interface"]

    print("The interface {name} has ip address {ip}/{mask}".format(
            name = interface["name"]["#text"],
            ip = interface["ipv4"]["address"]["ip"],
            mask = interface["ipv4"]["address"]["netmask"],
            )
        )
