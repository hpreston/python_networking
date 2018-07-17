#! /usr/bin/env python
"""Sample use of the requests library for RESTCONFself.

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
import requests, urllib3
import yaml

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Open and read in the mgmt IPs for the demo infrastructure
with open("../../setup/default_inventory.yaml") as f:
    devices = yaml.load(f.read())["all"]["children"]
    core1_ip = devices["core"]["hosts"]["core1"]["ansible_host"]
    username, password = "cisco", "cisco"

# Setup base variable for request
restconf_headers = {"Accept": "application/yang-data+json"}
restconf_base = "https://{ip}/restconf/data"
interface_url = restconf_base + "/interfaces/interface={int_name}"

# Create URL and send RESTCONF request to core1 for GigE2 Config
url = interface_url.format(ip = core1_ip, int_name = "GigabitEthernet2")
r = requests.get(url,
        headers = restconf_headers,
        auth=(username, password),
        verify=False)

# Print returned data
print(r.text)

# Process JSON data into Python Dictionary and use
interface = r.json()["ietf-interfaces:interface"]
print("The interface {name} has ip address {ip}/{mask}".format(
        name = interface["name"],
        ip = interface["ietf-ip:ipv4"]["address"][0]["ip"],
        mask = interface["ietf-ip:ipv4"]["address"][0]["netmask"],
        )
    )
