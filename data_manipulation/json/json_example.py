#! /usr/bin/env python
"""This script illustrates how to manipulate JSON data easily in Python with
the json library.

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

# Import the jsontodict library
import json

# Open the sample json file and read it into variable
with open("json_example.json") as f:
    json_example = f.read()

# Print the raw json data
print(json_example)

# Parse the json into a Python dictionary
json_dict = json.loads(json_example)

# Save the interface name into a variable
int_name = json_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
json_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.2"

# Revert to the json string version of the dictionary
print(json.dumps(json_dict))
