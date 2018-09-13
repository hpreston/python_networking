# Hands On - Useful Python Libraries for Network Engineers

* [Setup and Preparation](#setup-and-preparation)
    * [Devnet Sandbox](#devnet-sandbox)
* [Libraries to Work with Data](#libraries-to-work-with-data)
    * [XML with xmltodict](#xml-with-xmltodict)
    * [JSON with json](#json-with-json)
    * [YAML with PyYAML](#yaml-with-pyyaml)
    * [CSV with csv](#csv-with-csv)
    * [YANG with pyang](#yang-with-pyang)
* [Libraries to Work with APIs](#libraries-to-work-with-apis)
    * [rest with requests](#rest-with-requests)
    * [NETCONF with ncclient](#netconf-with-ncclient)
    * [CLI with netmiko](#cli-with-netmiko)
* [Other Cool Python Stuff](#other-cool-python-stuff)
    * [Introduction to pyATS](#introduction-to-pyats)


# Setup and Preparation
## Devnet Sandbox
This lab was written to be run using the [DevNet Devbox Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/f1a51f3b-3377-444d-97f0-5ad300d976be?diagramType=Topology).  This sandbox is a basic CentOS 7 workstation with typical development tools and software installed.  Specifically used in this lab are Python 3.6 and Vagrant (used to instantiate an IOS XE router for use in the labs.)

If you are doing this lab on your own, you'll need to reserve an instance of this sandbox before beginning.  If you are doing this as part of a guided workshop, the instructor will assign you a pod.  

### Steps to complete preparation 
1. Using either AnyConnect or OpenConnect, establish a VPN to your pod.  
2. SSH to the Devbox at IP `10.10.20.20` using credentials `root / cisco123` 

    ```bash
    ssh root@10.10.20.20
    ```

1. Install the Python 3.6 development libraries.  

    ```bash
    yum install -y python36u-devel
    ```

1. Add the IOS XE 16.9 Vagrant Box to your workstation.  Instructions for creating the Box file are available on github at [github.com/hpreston/vagrant_net_prog](https://github.com/hpreston/vagrant_net_prog/tree/master/box_building#cisco-csr-1000v).  If you are completing this as part of a guided lab, the instructor will provide details on how to complete this step.  

    ```bash
    vagrant box add --name iosxe/16.09.01 serial-csr1000v-universalk9.16.09.01.box
    ```

1. Clone the code samples to the devbox from GitHub and change into the directory. 

    ```bash
    git clone https://github.com/hpreston/python_networking
    cd python_networking
    ```

1. Create a Python 3.6 virtual environment and install Python libraries for exercises.  

    ```bash
    python3.6 -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt
    ```

1. Start and baseline the IOS XE Vagrant environment.  
    
    ```bash
    vagrant up 
    
    # After it completes
    python vagrant_device_setup.py
    ```
    
# Libraries to Work with Data
Exercises in this section are intended to be executed from an interactive Python interpreter.  

[iPython](https://ipython.org) has been installed as part of the requirements.txt installation and is one option.  You can start an iPython window by simply typing `ipython`.  For each step in the list below, type the specified command (or commands) and then press enter until the iPython prompt goes to the next step, and/or shows the expected output (ie. print or pprint commands).

Other options could be just `python` or `idle`.

## XML with xmltodict 
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd data_manipulation/xml
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

1. Import the xmltodict library

    ```python
    import xmltodict
    ```

1. Open the sample xml file and read it into variable

    ```python
    with open("xml_example.xml") as f:
        xml_example = f.read()
    ```

1. Print the raw XML data

    ```python
    print(xml_example)
    ```

1. Parse the XML into a Python (Ordered) dictionary
    
    ```python
    xml_dict = xmltodict.parse(xml_example)
    ```
    
1. Pretty Print the Python Dictionary Object

    ```python
    from pprint import pprint
    pprint(xml_dict)
    ```

1. Save the interface name into a variable using XML nodes as keys
    
    ```python
    int_name = xml_dict["interface"]["name"]
    ```

1. Print the interface name

    ```python
    print(int_name)
    ```

1. Change the IP address of the interface
    
    ```python
    xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.0.2"
    ```

1. Check that the IP address has been changed in the dictionary

   ```python
   pprint(xml_dict)
   ```

1. Revert to the XML string version of the dictionary

    ```python
    print(xmltodict.unparse(xml_dict))
    ```

1. After you've completed exploring, exit the interpreter.  

    ```python
    exit()
    ```

## JSON with json 
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```python
    cd data_manipulation/json
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

1. Import the jsontodict library

    ```python
    import json
    ```

1. Open the sample json file and read it into variable

    ```python
    with open("json_example.json") as f:
        json_example = f.read()   
    ```

1. Print the raw json data

    ```python
    print(json_example)
    ```

1. Parse the json into a Python dictionary

    ```python
    json_dict = json.loads(json_example)
    ```

1. Pretty Print the Python Dictionary Object 

    ```python
    from pprint import pprint
    pprint(json_dict)
    ```

1. Save the interface name into a variable

    ```python
    int_name = json_dict["interface"]["name"]
    ```

1. Print the interface name

    ```python
    print(int_name)
    ```

1. Change the IP address of the interface
    
    ```python
    json_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.2"
    ```

1. Check that the IP address has been changed in the dictionary

   ```python
   pprint(json_dict)
   ```

1. Revert to the json string version of the dictionary

    ```python
    print(json.dumps(json_dict))
    ```

1. After you've completed exploring, exit the interpreter.  

    ```python
    exit()
    ```

## YAML with PyYAML
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```python
    cd data_manipulation/yaml
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

1. Import the yamltodict library

    ```python
    import yaml
    ```

1. Open the sample yaml file and read it into variable

    ```python
    with open("yaml_example.yaml") as f:
        yaml_example = f.read()
    ```

1. Print the raw yaml data

    ```python
    print(yaml_example)
    ```

1. Parse the yaml into a Python dictionary

    ```python
    yaml_dict = yaml.load(yaml_example)
    ```

1. Pretty Print the Python Dictionary Object 

    ```bash
    from pprint import pprint
    pprint(yaml_dict)
    ```

1. Save the interface name into a variable

    ```python
    int_name = yaml_dict["interface"]["name"]
    ```

1. Print the interface name

    ```python
    print(int_name)
    ```

1. Change the IP address of the interface

    ```python
    yaml_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.2"
    ```

1. Check that the IP address has been changed in the dictionary

   ```python
   pprint(yaml_dict)
   ```

1. Revert to the yaml string version of the dictionary

    ```python
    print(yaml.dump(yaml_dict, default_flow_style=False))
    ```

1. After you've completed exploring, exit the interpreter.  

    ```python
    exit()
    ```

## CSV with csv 
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd data_manipulation/csv
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

1. Import the csv library

    ```python
    import csv
    ```

1. Open the sample csv file and print it to screen

    ```python
    with open("csv_example.csv") as f:
        print(f.read())
    ```

1. Open the sample csv file, and create a csv.reader object

    ```python
    with open("csv_example.csv") as f:
        csv_python = csv.reader(f)
        # Loop over each row in csv and leverage the data in code
        for row in csv_python:
            print("{device} is in {location} " \
                  "and has IP {ip}.".format(
                      device = row[0],
                      location = row[2],
                      ip = row[1]
                      )
                    )
    ```

1. Create a new tuple for additional router. 

    ```python
    router4 = ("router4", "10.4.0.1", "Chicago")    
    ```

1. Add new router to CSV file. 

    ```python    
    with open("csv_example.csv", "a") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(router4)        
    ```

1. Re-read and print out the CSV content.

    ```python
    with open("csv_example.csv") as f:
        print(f.read())
    ```

1. After you've completed exploring, exit the interpreter.  

    ```python
    exit()
    ```

## YANG with pyang 
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd data_manipulation/yang
    ```

1. Print the YANG module in a simple text tree

    ```bash
    pyang -f tree ietf-interfaces.yang
    ```

1. Print only part of the tree

    ```bash
    pyang -f tree --tree-path=/interfaces/interface \
      ietf-interfaces.yang
    ```

1. Print an example XML skeleton (NETCONF)

    ```bash
    pyang -f sample-xml-skeleton ietf-interfaces.yang
    ```

1. Create an HTTP/JS view of the YANG Model (no output expected in the CLI)

    ```bash
    pyang -f jstree -o ietf-interfaces.html \
      ietf-interfaces.yang
    ```
    
1.  *Optional:* Open `ietf-interfaces.html` in a web browser.  Will need to RDP into the Devbox to do this step.  

1. Control the "nested depth" in trees

    ```bash
    pyang -f tree --tree-depth=2 ietf-ip.yang
    ```

1. Display a full module. 

    ```bash
    pyang -f tree \
      ietf-ip.yang
    ```

1. Include deviation models in the processing

    ```bash
    pyang -f tree \
      --deviation-module=cisco-xe-ietf-ip-deviation.yang \
      ietf-ip.yang
    ```

# Libraries to Work with APIs 
Exercises in this section are intended to be executed from an interactive Python interpreter.

[iPython](https://ipython.org) has been installed as part of the requirements.txt installation and is one option.  You can start an iPython window by simply typing `ipython`.  

Other options could be just `python` or `idle`.

Each exercise also includes a Python script file that can be executed directly.  

## rest with requests 
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd device_apis/rest
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

### Retrieve Network Configuration Details with RESTCONF with `restconf_example1.py`
1. Import libraries

    ```python
    import requests, urllib3
    import sys
    ```

1. Add parent directory to path to allow importing common vars

    ```python
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    ```

1. Disable Self-Signed Cert warning for demo

    ```python
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    ```

1. Setup base variable for request

    ```python
    restconf_headers = {"Accept": "application/yang-data+json"}
    restconf_base = "https://{ip}:{port}/restconf/data"
    interface_url = restconf_base + "/ietf-interfaces:interfaces/interface={int_name}"
    ```

1. Create URL GigE2 Config

    ```python
    url = interface_url.format(ip = device["address"],
                               port = device["restconf_port"],
                               int_name = "GigabitEthernet2"
                              )
    ```

1. Check the complete URL you just composed

   ```python
   print(url)
   ```

1. Send RESTCONF request to core1 for GigE2 Config

    ```python
    r = requests.get(url,
            headers = restconf_headers,
            auth=(device["username"], device["password"]),
            verify=False)
    ```

1. Print returned data

    ```python
    print(r.text)
    ```

1. If REST call was successful, report interesting details. 

    ```python
    if r.status_code == 200:
        # Process JSON data into Python Dictionary and use
        interface = r.json()["ietf-interfaces:interface"]
        print("The interface {name} has ip address {ip}/{mask}".format(
                name = interface["name"],
                ip = interface["ietf-ip:ipv4"]["address"][0]["ip"],
                mask = interface["ietf-ip:ipv4"]["address"][0]["netmask"],
                )
            )
    else:
        print("No interface {} found.".format("GigabitEthernet2"))
    ```

### Modify Network Configuration Details with RESTCONF with `restconf_example2.py`
1. Continuing from previous exercise.  If starting from new interpreter, execute these steps. 

    ```python
    import requests, urllib3, sys
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    restconf_headers = {"Accept": "application/yang-data+json"}
    restconf_base = "https://{ip}:{port}/restconf/data"
    interface_url = restconf_base + "/ietf-interfaces:interfaces/interface={int_name}"
    ```

1. Add additional `Content-Type` header.

    ```python
    restconf_headers["Content-Type"] = "application/yang-data+json"
    ```

1. Create dictionary with details on a new loopback interface. 

    ```python
    loopback = {"name": "Loopback101",
                "description": "Demo interface by RESTCONF",
                "ip": "192.168.101.1",
                "netmask": "255.255.255.0"}
    ```

1. Setup data body to create new loopback interface

    ```python
    data = {
        "ietf-interfaces:interface": {
            "name": loopback["name"],
            "description": loopback["description"],
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": loopback["ip"],
                        "netmask": loopback["netmask"]
                    }
                ]
            }
        }
    }
    ```

1. Create URL 

    ```python
    url = interface_url.format(ip = device["address"],
                               port = device["restconf_port"],
                               int_name = loopback["name"]
                              )
    ```

1. Check the complete URL you just composed

   ```python
   print(url)
   ```

1. Send RESTCONF request to device

    ```python
    r = requests.put(url,
            headers = restconf_headers,
            auth=(device["username"], device["password"]),
            json = data,
            verify=False)
    ```

1. Check Status Code (expected `201`)
    
    ```python
    print("Request Status Code: {}".format(r.status_code))
    ```

1. Query for details on the new interface you just created

    ```python
    # Create URL and send RESTCONF request to core1 for GigE2 Config
    url = interface_url.format(ip = device["address"],
                               port = device["restconf_port"],
                               int_name = "Loopback101"
                              )
    r = requests.get(url,
            headers = restconf_headers,
            auth=(device["username"], device["password"]),
            verify=False)
    
    # Print returned data
    print(r.text)
    ```

### Delete Network Configuration Details with RESTCONF with `restconf_example3.py`
1. Continuing from previous exercise.  If starting from new interpreter, execute these steps. 

    ```python
    import requests, urllib3, sys
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    restconf_headers = {"Accept": "application/yang-data+json"}
    restconf_base = "https://{ip}:{port}/restconf/data"
    interface_url = restconf_base + "/ietf-interfaces:interfaces/interface={int_name}"
    url = interface_url.format(ip = device["address"],
                               port = device["restconf_port"],
                               int_name = "Loopback101"
                              )
    ```

1. Send DELETE request to remove the Loopback. 

    ```python
    r = requests.delete(url,
            headers = restconf_headers,
            auth=(device["username"], device["password"]),
            verify=False)
    ```

1. Check Status Code (expected `204`)

    ```python
    print("Request Status Code: {}".format(r.status_code))
    ``` 

1. Query for details on the new interface (no output expected, as you just deleted it)

    ```python
    r = requests.get(url,
            headers = restconf_headers,
            auth=(device["username"], device["password"]),
            verify=False)
    ```
    
1. Check status code (expected `404`)

    ```python
    print(r.status_code)
    ```


## NETCONF with ncclient

1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd device_apis/netconf
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

### Retrieve Network Configuration Details with NETCONF with `netconf_example1.py`

1. Import libraries

    ```python
    from ncclient import manager
    from xml.dom import minidom
    import xmltodict
    import sys
    ```

1. Add parent directory to path to allow importing common vars

    ```python
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    ```

1. Create filter template for an interface

    ```python
    interface_filter = """
    <filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>{int_name}</name>
        </interface>
      </interfaces>
    </filter>
    """
    ```

1. Open NETCONF connection to device
    * *Note: Normally you'd use a `with` block to open connection to device. This avoids needing to manually `m.close_session()` at the end of a script, but for interactive use, this format is chosen.*

    ```python
    m = manager.connect(host = device["address"],
                         port = device["netconf_port"],
                         username = device["username"],
                         password = device["password"],
                         hostkey_verify = False)
    ```

1. Verify NETCONF connection is active (expected output `true`)

    ```python
    m.connected
    ```

1. Create desired NETCONF filter for a particular interface
    
    ```python
    filter = interface_filter.format(int_name = "GigabitEthernet2")
    ```

1. Execute a NETCONF <get-config> using the filter
    
    ```python
    r = m.get_config("running", filter)
    ```

1. Pretty print raw xml to screen

    ```python
    xml_doc = minidom.parseString(r.xml)
    print(xml_doc.toprettyxml(indent = "  "))
    ```

1. Process the XML data into Python Dictionary and use

    ```python
    interface = xmltodict.parse(r.xml)
    ```
    
1. Pretty Print the full Python (Ordered) Dictionary. 

    ```python
    from pprint import pprint
    pprint(interface)
    ```

1. If RPC returned data, print out the interesting pieces. 

    ```python
    if not interface["rpc-reply"]["data"] is None:
        # Create Python variable for interface details
        interface = interface["rpc-reply"]["data"]["interfaces"]["interface"]
    
        print("The interface {name} has ip address {ip}/{mask}".format(
                name = interface["name"]["#text"],
                ip = interface["ipv4"]["address"]["ip"],
                mask = interface["ipv4"]["address"]["netmask"],
                )
            )
    else:
        print("No interface {} found".format("GigabitEthernet2"))
    ```


### Modify Network Configuration Details with NETCONF with `netconf_example2.py`
1. Continuing from previous exercise. If starting from new interpreter, execute these steps.

    ```python
    from ncclient import manager
    from xml.dom import minidom
    import xmltodict
    import sys
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    interface_filter = """
    <filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>{int_name}</name>
        </interface>
      </interfaces>
    </filter>
    """
    m = manager.connect(host = device["address"],
                         port = device["netconf_port"],
                         username = device["username"],
                         password = device["password"],
                         hostkey_verify = False)
    ```

1. Verify NETCONF connection is active

    ```python
    m.connected
    ```

1. Create Python dictionary with new Loopback Details

    ```python
    loopback = {"int_name": "Loopback102",
                "description": "Demo interface by NETCONF",
                "ip": "192.168.102.1",
                "netmask": "255.255.255.0"}
    ```

1. Create NETCONF <config> template for an interface

    ```python
    config_data = """
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
          <interface>
            <name>{int_name}</name>
            <description>{description}</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
              ianaift:softwareLoopback
            </type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
              <address>
                <ip>{ip}</ip>
                <netmask>{netmask}</netmask>
              </address>
            </ipv4>
          </interface>
      </interfaces>
    </config>
    """
    ```

1. Create desired NETCONF config payload 

    ```python
    config = config_data.format(**loopback)
    ```

1. Send <edit-config> operation

    ```python
    r = m.edit_config(target = "running", config = config)
    ```

1. Print OK status (expected output `true`)
    
    ```python
    print("NETCONF RPC OK: {}".format(r.ok))
    ```

1. Create a new NETCONF <filter> to check on new loopback interface

    ```python
    filter = interface_filter.format(int_name = "Loopback102")
    ```

1. Execute a NETCONF <get-config> using this filter
    
    ```python
    r = m.get_config("running", filter)
    ```

1. Pretty print the raw XML to screen

    ```python
    xml_doc = minidom.parseString(r.xml)
    print(xml_doc.toprettyxml(indent = "  "))
    ```

### Delete Network Configuration Details with NETCONF with `netconf_example3.py`
1. Continuing from previous exercise. If starting from new interpreter, execute these steps.

    ```python
    from ncclient import manager
    from xml.dom import minidom
    import xmltodict
    import sys
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    interface_filter = """
    <filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>{int_name}</name>
        </interface>
      </interfaces>
    </filter>
    """
    loopback = {"int_name": "Loopback102",
                "description": "Demo interface by NETCONF",
                "ip": "192.168.102.1",
                "netmask": "255.255.255.0"}
    m = manager.connect(host = device["address"],
                         port = device["netconf_port"],
                         username = device["username"],
                         password = device["password"],
                         hostkey_verify = False)
    ```

1. Verify NETCONF connection is active

    ```python
    m.connected
    ```

1. Create new config template to delete an interface

    ```python
    config_data = """
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
          <interface operation="delete">
            <name>{int_name}</name>
          </interface>
      </interfaces>
    </config>
    """
    ```

1. Create desired NETCONF config payload and execute <edit-config> to delete the interface

    ```python
    config = config_data.format(**loopback)
    r = m.edit_config(target = "running", config = config)
    ```

1. Print OK status (expected output `true`)

    ```python
    print("NETCONF RPC OK: {}".format(r.ok))
    ```

1. Create a new NETCONF <filter> to check on new loopback interface

    ```python
    filter = interface_filter.format(int_name = "Loopback102")
    ```

1. Execute a NETCONF <get-config> using this filter
    
    ```python
    r = m.get_config("running", filter)
    ```

1. Pretty print the raw XML to screen (expected output will not include the loopback interface, as you just deleted it)

    ```python
    xml_doc = minidom.parseString(r.xml)
    print(xml_doc.toprettyxml(indent = "  "))
    ```

### End the NETCONF Connection 

1. Send a <close-session> RPC request to disconnect the connection. 

    ```python
    m.close_session()
    m.connected
    ```

1. End the Python interpreter. 

    ```python
    exit()
    ```

## CLI with netmiko 
1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd device_apis/cli
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

### Retrieve Network Configuration Details with CLI with `netmiko_example1.py`
1. Import libraries

    ```python
    from netmiko import ConnectHandler
    import re
    import sys
    ```

1. Add parent directory to path to allow importing common vars

    ```python
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    ```

1. Set device_type for netmiko

    ```python
    device["device_type"] = "cisco_ios"
    ```

1. Create a CLI command template

    ```python
    show_interface_config_temp = "show running-config interface {}"
    ```

1. Open CLI connection to device. 
    * *Note: Normally you'd use a with block to open connection to device. This avoids needing to manually `m.close_session()` at the end of a script, but for interactive use, this format is chosen.*

    ```python
    ch = ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"])
    ```

1. Create desired CLI command

    ```python
    command = show_interface_config_temp.format("GigabitEthernet2")
    ```

1. Verify the command has been created correctly

   ```python
   print(command)
   ```

1. Send command to device

    ```python
    interface = ch.send_command(command)
    ```

1. Print the raw command output to the screen

    ```python
    print(interface)
    ```

1. Create regular expression searches to parse the output for desired interface details

    ```python
    name = re.search(r'interface (.*)', interface).group(1)
    description = re.search(r'description (.*)', interface).group(1)
    ```

1. Pull out the ip and mask for the interface

    ```python
    ip_info = re.search(r'ip address (.*) (.*)', interface)
    ip = ip_info.group(1)
    netmask = ip_info.group(2)
    ```

1. Print the desired info to the screen

    ```python
    print("The interface {name} has ip address {ip}/{mask}".format(
            name = name,
            ip = ip,
            mask = netmask,
            )
        )
    ```

### Modify Network Configuration Details with CLI with `netmiko_example2.py`
1. Continuing from previous exercise. If starting from new interpreter, execute these steps.

    ```python
    from netmiko import ConnectHandler
    import re, sys
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    device["device_type"] = "cisco_ios"
    show_interface_config_temp = "show running-config interface {}"
    ch = ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"])
    ```

1. Create Python dictionary with new Loopback Details

    ```python
    loopback = {"int_name": "Loopback103",
                "description": "Demo interface by CLI and netmiko",
                "ip": "192.168.103.1",
                "netmask": "255.255.255.0"}
    ```

1. Create a CLI configuration

    ```python
    interface_config = [
        "interface {}".format(loopback["int_name"]),
        "description {}".format(loopback["description"]),
        "ip address {} {}".format(loopback["ip"], loopback["netmask"]),
        "no shut"
    ]
    ```

1. Send configuration to device

    ```python
    output = ch.send_config_set(interface_config)
    ```

1. Print the raw command output to the screen

    ```python
    print("The following configuration was sent: ")
    print(output)
    ```

1. Create a CLI command to retrieve the new configuration.  

    ```python
    command = show_interface_config_temp.format("Loopback103")
    interface = ch.send_command(command)
    print(interface)
    ```

### Delete Network Configuration Details with CLI with `netmiko_example3.py`
1. Continuing from previous exercise. If starting from new interpreter, execute these steps.

    ```python
    from netmiko import ConnectHandler
    import re, sys
    sys.path.append("..") 
    from device_info import vagrant_iosxe as device
    device["device_type"] = "cisco_ios"
    show_interface_config_temp = "show running-config interface {}"
    ch = ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"])
    ```

1. Create a new CLI configuration to delete the interface. 

    ```python
    interface_config = [
        "no interface {}".format(loopback["int_name"])
    ]
    ```

1. Send configuration to device

    ```python
    output = ch.send_config_set(interface_config)
    ```

1. Print the raw command output to the screen

    ```python
    print("The following configuration was sent: ")
    print(output)
    ```

1. Create a CLI command to verify configuration removed.

    ```python
    command = show_interface_config_temp.format("Loopback103")
    interface = ch.send_command(command)
    print(interface)
    ```
   *Note: attempting to view the configuration of a non-existing interface will generate a CLI error. This output is expected, and one of the reasons APIs like NETCONF or RESTCONF are better suited to programmatic interactions.*

### End the CLI connection to the device
1. Disconnect from the device.  

    ```python
    ch.disconnect()
    ```

1. End the Python interpreter. 

    ```python
    exit()
    ```

# Other Cool Python Stuff 

## Introduction to pyATS
[pyATS](https://developer.cisco.com/site/pyats) is a network testing tool developed by Cisco and made available for free, with significant elements of the underlying code open source.  

pyATS offers network developers the ability to profile the network state of hardware, interfaces, protocols, etc... before, during and after changes, to ensure the network is operating as designed, and identify problems before the dreaded phone call.  To enable this level of robust testing, pyATS offers a standard way to communicate with network elements and standardize the data returned into native Python objects.  This core functionality opens up a lot of flexibility on how pyATS can be used by network developers.  

In the following exercises, you will get a brief introduction to pyATS to connect and learn about device details.  

### Connect and Interact with a Device

1. From the root of the `python_networking` repository, change into the exercise directory.  

    ```bash
    cd network_testing/pyats
    ```

1. Start an interactive Python interpreter.  Example below:

    ```python
    # ipython
    
    Python 3.6.5 (default, Apr 10 2018, 17:08:37)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]:
    ```

1. Import in pyATS libraries and tools 

    ```python
    from genie.conf import Genie
    from ats.topology import loader
    from genie.abstract import Lookup
    from genie.libs import ops # noqa
    ```

1. Read and process the testbed (inventory) file

    ```python
    genie_testbed = Genie.init("./default_testbed.yaml")
    ```

1. Create a pyATS device object from testbed

    ```python
    vagrant_iosxe1 = genie_testbed.devices["vagrant-iosxe1"]
    ```

1. Connect to the device

    ```python
    vagrant_iosxe1.connect()
    ```
    
    * pyATS establishes a connection to the device

1. Create an abstract device to standardize Python API and code for platform

    ```python
    vagrant_iosxe1_abstract = Lookup.from_device(vagrant_iosxe1)
    ```

1. Using the abstract device, learn about the Interfaces on the end device

    ```python
    vagrant_iosxe1_interfaces = vagrant_iosxe1_abstract.ops.interface.interface.Interface(vagrant_iosxe1)
    vagrant_iosxe1_interfaces.learn()
    ```

1. Print out the interface details that were learned 

    ```python
    vagrant_iosxe1_interfaces.info
    ```

1. Display a single interface from the device 

    ```python
    vagrant_iosxe1_interfaces.info["GigabitEthernet1"]
    ```

1. Print the mac address for the interface 

    ```python
    vagrant_iosxe1_interfaces.info["GigabitEthernet1"]["mac_address"]
    ```

1. Notice that there was no parsing of command line output needed to access this data 

1. Execute a command on the device and print the output 

    ```python
    print(vagrant_iosxe1.execute("show version"))
    ```

1. Or store the output into a variable 

    ```python
    version = vagrant_iosxe1.execute("show version")
    ```

1. Send a configuration command to the device

    ```python
    vagrant_iosxe1.configure("ntp server 10.10.10.10")
    ```

1. Create a configuration command list and send to the device 

    ```python
    config_loopback = [
                        "interface Loopback201", 
                        "description Configured by pyATS", 
                        "ip address 172.16.201.1 255.255.255.0", 
                        "no shut"
                      ]
    vagrant_iosxe1.configure(config_loopback)
    ```

1. Re-learn the interfaces

    ```python
    vagrant_iosxe1_interfaces = vagrant_iosxe1_abstract.ops.interface.interface.Interface(vagrant_iosxe1)
    vagrant_iosxe1_interfaces.learn()
    ```

1. Get details about new interface 

    ```python
    vagrant_iosxe1_interfaces.info["Loopback201"]
    ```

1. Disconnect from the devices

    ```python
    vagrant_iosxe1.disconnect()
    ```
