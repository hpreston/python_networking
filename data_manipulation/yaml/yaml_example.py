#! /usr/bin/env python
"""This script illustrates how to manipulate yaml data easily in Python with
the PyYAML library.

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

# Import the yamltodict library
import yaml

# Open the sample yaml file and read it into variable
with open("yaml_example.yaml") as f:
    yaml_example = f.read()

# Print the raw yaml data
print(yaml_example)

# Parse the yaml into a Python dictionary
yaml_dict = yaml.load(yaml_example)

# Save the interface name into a variable
int_name = yaml_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
yaml_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.2"

# Revert to the yaml string version of the dictionary
print(yaml.dump(yaml_dict, default_flow_style=False))
