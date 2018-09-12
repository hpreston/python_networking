#! /usr/bin/env python
"""Configure the baseline on Vagrant device

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
from device_apis.device_info import vagrant_iosxe as device # noqa

# Open and read in configuration template
with open("vagrant_device_config.xml") as f:
    config_data = f.read()

# Open NETCONF connection to device
with manager.connect(host = device["address"],
                     port = device["netconf_port"],
                     username = device["username"],
                     password = device["password"],
                     hostkey_verify = False) as m:

    # Create desired NETCONF config payload and <edit-config>
    r = m.edit_config(target = "running", config = config_data)

    # Print OK status
    print("NETCONF RPC OK: {}".format(r.ok))
