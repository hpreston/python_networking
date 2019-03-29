import requests

# Diable InsecureRequestWarning
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)

headers = {"content-type": "application/json", "x-auth-token": ""}


def dnac_login(dnac, username, password):
    """
    Use the REST API to Log into an DNA Center and retrieve ticket
    """
    url = "https://{}/dna/system/api/v1/auth/token".format(dnac)

    # Make Login request and return the response body
    response = requests.request(
        "POST", url, auth=(username, password), headers=headers, verify=False
    )
    return response.json()["Token"]


# Entry point for program
if __name__ == "__main__":
    # Setup Arg Parse for Command Line parameters
    import argparse

    parser = argparse.ArgumentParser()

    # Command Line Parameters for Source and Destination IP
    parser.add_argument("dnac", help="Cisco DNA Center Address")
    parser.add_argument("username", help="Cisco DNA Center Username")
    parser.add_argument("password", help="Cisco DNA Center Password")
    args = parser.parse_args()

    # Get Source and Destination IPs from Command Line
    dnac = args.dnac
    username = args.username
    password = args.password

    # Log into the dnac Controller to get Ticket
    token = dnac_login(dnac, username, password)

    print("Your token is {}".format(token))
