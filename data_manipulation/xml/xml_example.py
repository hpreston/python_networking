#! /usr/bin/env python
"""This script illustrates how to manipulate XML data easily in Python with
the xmltodict library.

Prep with:
  pip install xmltodict

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

# Import the xmltodict library
import xmltodict

# Open the sample xml file and read it into variable
with open("xml_example.xml") as f:
    xml_example = f.read()

# Print the raw XML data
print(xml_example)

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)

# Save the interface name into a variable using XML nodes as keys
int_name = xml_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.0.2"

# Revert to the XML string version of the dictionary
print(xmltodict.unparse(xml_dict))
