#! /usr/bin/env python
"""Sample use of the PySNMP library for SNMP interfacing

This script will query for information from a device

Uses code example from: https://github.com/etingof/pysnmp

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
from pysnmp.hlapi import *
import yaml

# Open and read in the mgmt IPs for the demo infrastructure
with open("../../setup/default_inventory.yaml") as f:
    devices = yaml.load(f.read())["all"]["children"]
    core1_ip = devices["core"]["hosts"]["core1"]["ansible_host"]
    ro_community, rw_community = "public", "private"

# Setup SNMP connection and query a MIB
iterator = getCmd(SnmpEngine(),
                  CommunityData(ro_community),
                  UdpTransportTarget((core1_ip, 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

# Process the query
errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

# Check for errors, and if OK, print returned result
if errorIndication:  # SNMP engine errors
    print(errorIndication)
else:
    if errorStatus:  # SNMP agent errors
        print('%s at %s' % (errorStatus.prettyPrint(),
                            varBinds[int(errorIndex)-1] if errorIndex else '?'))
    else:
        for varBind in varBinds:  # SNMP response contents
            print(' = '.join([x.prettyPrint() for x in varBind]))
