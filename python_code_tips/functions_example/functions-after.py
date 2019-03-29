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

# Headers for DNAC
headers = {"content-type": "application/json", "x-auth-token": ""}


def dnac_login(dnac, port, username, password):
    """
    Use the REST API to Log into an DNA Center and retrieve ticket
    """
    url = "https://{}:{}/dna/system/api/v1/auth/token".format(dnac, port)

    # Make Login request and return the response body
    response = requests.request(
        "POST", url, auth=(username, password), headers=headers, verify=False
    )
    return response.json()["Token"]


def host_list(dnac, ticket, ip=None):
    """
    Use the REST API to retrieve the list of hosts.
    Optional parameters to filter by:
      IP address
      MAC address
      Hostname
    """
    url = "https://{}/api/v1/host?hostIp={}".format(dnac, ip)
    headers["x-auth-token"] = ticket
    filters = []

    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]


def print_host_details(host):
    """
    Print to screen interesting details about a given host.
    Input Paramters are:
      host_desc: string to describe this host.  Example "Source"
      host: dictionary object of a host returned from dnac
    Standard Output Details:
      Host Name (hostName) - If available
      Host IP (hostIp)
      Host MAC (hostMac)
      Network Type (hostType) - wired/wireless
      Host Sub Type (subType)
      VLAN (vlanId)
      Connected Network Device (connectedNetworkDeviceIpAddress)

    Wired Host Details:
      Connected Interface Name (connectedInterfaceName)

    Wireless Host Details:
      Connected AP Name (connectedAPName)
    """
    # If optional host details missing, add as "Unavailable"
    if "hostName" not in host.keys():
        host["hostName"] = "Unavailable"

    # Print Standard Details
    print("Host Name: {}".format(host["hostName"]))
    print("Network Type: {}".format(host["hostType"]))
    print(
        "Connected Network Device: {}".format(
            host["connectedNetworkDeviceIpAddress"]
        )
    )  # noqa: E501

    # Print Wired/Wireless Details
    if host["hostType"] == "wired":
        print(
            "Connected Interface Name: {}".format(
                host["connectedInterfaceName"]
            )
        )  # noqa: E501
    if host["hostType"] == "wireless":
        print("Connected AP Name: {}".format(host["connectedAPName"]))

    # Print More Standard Details
    print("VLAN: {}".format(host["vlanId"]))
    print("Host IP: {}".format(host["hostIp"]))
    print("Host MAC: {}".format(host["hostMac"]))
    print("Host Sub Type: {}".format(host["subType"]))

    # Blank line at the end
    print("")


# Entry point for program
if __name__ == "__main__":
    # Setup Arg Parse for Command Line parameters
    import argparse

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

    # Log into the dnac Controller to get Ticket
    token = dnac_login(
        dnac["host"], dnac["port"], dnac["username"], dnac["password"]
    )

    # Retrieve Host Details from dnac
    source_host = host_list(dnac["host"], token, ip=source_ip)
    destination_host = host_list(dnac["host"], token, ip=destination_ip)

    # Print Out Host details
    print("Source Host Details:")
    print("-" * 25)
    print_host_details(source_host[0])

    print("Destination Host Details:")
    print("-" * 25)
    print_host_details(destination_host[0])
