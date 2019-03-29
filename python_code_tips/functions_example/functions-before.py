#! /usr/bin/env python

import requests
import json
import argparse

# Diable InsecureRequestWarning
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)

# DevNet Always-On Sandbox DNA Center
# https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology
dnac = {
    "host": "sandboxdnac2.cisco.com",
    "username": "devnetuser",
    "password": "Cisco123!",
    "port": 443,
}


# Setup Arg Parse for Command Line parameters
parser = argparse.ArgumentParser()

# Command Line Parameters for Source and Destination IP
parser.add_argument("source_ip", help="Source IP Address")
parser.add_argument("destination_ip", help="Destination IP Address")
args = parser.parse_args()

# Get Source and Destination IPs from Command Line
source_ip = args.source_ip
destination_ip = args.destination_ip

# Print Starting message
print("Running Troubleshooting Script for ")
print("      Source IP:      {} ".format(source_ip))
print("      Destination IP: {}".format(destination_ip))
print("")

# Headers for DNAC
headers = {"content-type": "application/json", "x-auth-token": ""}


# Login to DNAC
url = "https://{}:{}/dna/system/api/v1/auth/token".format(
    dnac["host"], dnac["port"]
)

# Make Login request and return the response body
response = requests.request(
    "POST",
    url,
    auth=(dnac["username"], dnac["password"]),
    headers=headers,
    verify=False,
)
token = response.json()["Token"]
headers["x-auth-token"] = token

# URL for Host Calls
url = "https://{}/api/v1/host".format(dnac["host"])

# Get Host Infomration for Source
source_url = url + "?" + "&hostIp={}".format(source_ip)

# Make API request and return the response body
response = requests.request("GET", source_url, headers=headers, verify=False)
source_host = response.json()["response"][0]

# Print out details about source
print("Source Host Details:")
print("-" * 25)
# If optional host details missing, add as "Unavailable"
if "hostName" not in source_host.keys():
    source_host["hostName"] = "Unavailable"

# Print Standard Details
print("Host Name: {}".format(source_host["hostName"]))
print("Network Type: {}".format(source_host["hostType"]))
print(
    "Connected Network Device: {}".format(
        source_host["connectedNetworkDeviceIpAddress"]
    )
)  # noqa: E501

# Print Wired/Wireless Details
if source_host["hostType"] == "wired":
    print(
        "Connected Interface Name: {}".format(
            source_host["connectedInterfaceName"]
        )
    )  # noqa: E501
if source_host["hostType"] == "wireless":
    print("Connected AP Name: {}".format(source_host["connectedAPName"]))

# Print More Standard Details
print("VLAN: {}".format(source_host["vlanId"]))
print("Host IP: {}".format(source_host["hostIp"]))
print("Host MAC: {}".format(source_host["hostMac"]))
print("Host Sub Type: {}".format(source_host["subType"]))

# Blank line at the end
print("")

# Get Host Infomration for Destination
destination_url = url + "?" + "&hostIp={}".format(destination_ip)

# Make API request and return the response body
response = requests.request(
    "GET", destination_url, headers=headers, verify=False
)
destination_host = response.json()["response"][0]

# Print out details about source
print("Detination Host Details:")
print("-" * 25)
# If optional host details missing, add as "Unavailable"
if "hostName" not in destination_host.keys():
    destination_host["hostName"] = "Unavailable"

# Print Standard Details
print("Host Name: {}".format(destination_host["hostName"]))
print("Network Type: {}".format(destination_host["hostType"]))
print(
    "Connected Network Device: {}".format(
        destination_host["connectedNetworkDeviceIpAddress"]
    )
)  # noqa: E501

# Print Wired/Wireless Details
if destination_host["hostType"] == "wired":
    print(
        "Connected Interface Name: {}".format(
            destination_host["connectedInterfaceName"]
        )
    )  # noqa: E501
if destination_host["hostType"] == "wireless":
    print("Connected AP Name: {}".format(destination_host["connectedAPName"]))

# Print More Standard Details
print("VLAN: {}".format(destination_host["vlanId"]))
print("Host IP: {}".format(destination_host["hostIp"]))
print("Host MAC: {}".format(destination_host["hostMac"]))
print("Host Sub Type: {}".format(destination_host["subType"]))

# Blank line at the end
print("")
