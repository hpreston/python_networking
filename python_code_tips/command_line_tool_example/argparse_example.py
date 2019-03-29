#! /usr/bin/env python
"""Simple CLI Tool Example to check routing table using ietf-routing YANG model and NETCONF
"""

from ncclient import manager
from ncclient.transport.errors import SSHError
import xmltodict
from xml.dom import minidom


def get_ipv4_default_rib(host, username, password, port=830):
    """Use NETCONF to connect to device, retrieve IPv4 default RIP, and return as dictionary
    """
    filter = """
        <filter>
            <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing"
                           xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">
                <routing-instance>
                    <name>default</name>
                    <ribs>
                        <rib>
                            <name>ipv4-default</name>
                        </rib>
                    </ribs>
                </routing-instance>
            </routing-state>
        </filter>
        """

    # Open NETCONF connection to device
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            r = m.get(filter)
    except SSHError:
        print(
            "Unable to connect to device {} with NETCONF on port {}.".format(
                host, port
            )
        )
        exit(1)

    # Pretty print raw xml to screen
    # xml_doc = minidom.parseString(r.xml)
    # print(xml_doc.toprettyxml(indent = "  "))

    # Process the XML data into Python Dictionary and use
    response_dict = xmltodict.parse(r.xml)

    routes = response_dict["rpc-reply"]["data"]["routing-state"][
        "routing-instance"
    ]["ribs"]["rib"]["routes"]["route"]

    return routes


def print_routes(routes):
    """Print out the routing table based on ietf-routing ipv4 ribs
    """
    if len(routes) == 0:
        print("No routes found.")
        exit(1)

    try:
        print(
            "{route:<20} {source:<10} {nexthop:<20}".format(
                route="Prefix", source="Source", nexthop="Next Hop"
            )
        )
        for route in routes:
            print(
                "{route:<20} {source:<10} {nexthop:<20}".format(
                    route=route["destination-prefix"],
                    source=route["source-protocol"],
                    nexthop=route["next-hop"]["next-hop-address"],
                )
            )
    except Exception:
        print("Problem in routing table, unable to print.")
        exit(1)


# Script Entry Point
if __name__ == "__main__":
    # Use Arg Parse to retrieve device details
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", help="Host address for network device", required=True
    )
    parser.add_argument(
        "--port", help="Override default NETCONF port of 830", default=830
    )
    parser.add_argument("--username", help="Device username", required=False)
    parser.add_argument("--password", help="Device password", required=False)

    args = parser.parse_args()
    username = args.username
    password = args.password

    # If Username or Password not provided as arguments, check OS ENV
    if username is None:
        username = os.getenv("USERNAME")
    if password is None:
        password = os.getenv("PASSWORD")

    if username is None or password is None:
        print(
            "You must provide a username and password as a command argument,"
        )
        print("or as Environment Variables of USERNAME or PASSWORD")
        exit(1)

    print("Getting route list from device...")
    print("")

    # Get route list
    routes = get_ipv4_default_rib(
        host=args.host, port=args.port, username=username, password=password
    )

    # Print route list
    print_routes(routes)
