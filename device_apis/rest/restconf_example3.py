#! /usr/bin/env python
"""Sample use of the requests library for RESTCONF.

This script will delete information from a device.

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
import requests, urllib3
import sys

# Add parent directory to path to allow importing common vars
sys.path.append("..") # noqa
from device_info import ios_xe1 as device # noqa

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setup base variable for request
restconf_headers = {"Accept": "application/yang-data+json"}
restconf_base = "https://{ip}:{port}/restconf/data"
interface_url = restconf_base + "/ietf-interfaces:interfaces/interface={int_name}"

# Create URL and send RESTCONF request to core1 for GigE2 Config
url = interface_url.format(ip = device["address"],
                           port = device["restconf_port"],
                           int_name = "Loopback101"
                          )
print("URL: {}\n".format(url))

r = requests.delete(url,
        headers = restconf_headers,
        auth=(device["username"], device["password"]),
        verify=False)

# Print returned data
print("DELETE Request Status Code: {}".format(r.status_code))

# # Process JSON data into Python Dictionary and use
# interface = r.json()["ietf-interfaces:interface"]
# print("The interface {name} has ip address {ip}/{mask}".format(
#         name = interface["name"],
#         ip = interface["ietf-ip:ipv4"]["address"][0]["ip"],
#         mask = interface["ietf-ip:ipv4"]["address"][0]["netmask"],
#         )
#     )
