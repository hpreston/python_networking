#! /usr/bin/env python
"""
Demo script showing how to create network configurations by combining data from CSV files with Jinja templates. 
"""

import csv
from jinja2 import Template

source_file = "switch-ports.csv"
interface_template_file = "switchport-interface-template.j2"

# String that will hold final full configuration of all interfaces
interface_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object 
with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

# Open up the CSV file containing the data 
with open(source_file) as f:
    # Use DictReader to access data from CSV 
    reader = csv.DictReader(f)
    # For each row in the CSV, generate an interface configuration using the jinja template 
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            vlan = row["VLAN"],
            server = row["Server"],
            link = row["Link"],
            purpose = row["Purpose"]
        )

        # Append this interface configuration to the full configuration 
        interface_configs += interface_config

# Save the final configuraiton to a file 
with open("interface_configs.txt", "w") as f:
    f.write(interface_configs)
