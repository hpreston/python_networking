#! /usr/bin/env python
"""
Discover details about Cisco DNA Center connected hosts.
"""

# Import  and functions
from dnac import (
    dnac,
    dnac_login,
    host_list,
    verify_single_host,
    print_host_details,
    network_device_list,
    interface_details,
    print_network_device_details,
    print_interface_details,
)


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

    # Step 1: Identify involved hosts
    # Retrieve Host Details from dnac
    source_host = host_list(dnac["host"], token, ip=source_ip)
    destination_host = host_list(dnac["host"], token, ip=destination_ip)

    # Verify single host found for each IP
    verify_single_host(source_host, source_ip)
    verify_single_host(destination_host, destination_ip)

    # Print Out Host details
    print("Source Host Details:")
    print("-" * 25)
    print_host_details(source_host[0])

    print("Destination Host Details:")
    print("-" * 25)
    print_host_details(destination_host[0])

    # Step 2: Where are they in the network?
    # Retrieve and Print Source Device Details from dnac
    source_host_net_device = network_device_list(
        dnac["host"], token, id=source_host[0]["connectedNetworkDeviceId"]
    )  # noqa: E501
    print("Source Host Network Connection Details:")
    print("-" * 45)
    print_network_device_details(source_host_net_device[0])
    # If Host is wired, collect interface details
    if source_host[0]["hostType"] == "wired":
        source_host_interface = interface_details(
            dnac["host"], token, id=source_host[0]["connectedInterfaceId"]
        )  # noqa: E501
        print("Attached Interface:")
        print("-" * 20)
        print_interface_details(source_host_interface)

    destination_host_net_device = network_device_list(
        dnac["host"], token, id=destination_host[0]["connectedNetworkDeviceId"]
    )  # noqa: E501
    print("Destination Host Network Connection Details:")
    print("-" * 45)
    print_network_device_details(destination_host_net_device[0])
    # If Host is wired, collect interface details
    if destination_host[0]["hostType"] == "wired":
        destination_host_interface = interface_details(
            dnac["host"], token, id=destination_host[0]["connectedInterfaceId"]
        )  # noqa: E501
        print("Attached Interface:")
        print("-" * 20)
        print_interface_details(destination_host_interface)
