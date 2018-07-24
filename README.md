# python_networking
Collection of scripts and examples of Python code, libraries, and utilities for working with Network Devices.  

> This repo is an active work in progress.  

# Setting Up Environment to Run
The scripts in this repository are written to target a sample network topology built as Core > Dist > Access with IOS XE devices in the Core, and NX-OS devices for Dist and Access.  The demo network can be run with Cisco VIRL or CML, and the [`topology.virl`](topology.virl) file in the repo has the details.  If you do not have your own VIRL server, you can reserve a free [DevNet VIRL Sandbox]() to use.  

## Clone and Prep the Environment
1. Clone the code repo

```bash
git clone https://github.com/hpreston/python_networking
cd python_networking
```

1. Setup Python Virtual Environment.  (This repo uses Pipenv, you can install it with `pip install pipenv`).  

```bash
python3.6 -m venv venv
source venv/bin/activate
pipenv install
```

1. After connecting to the Sandbox with VPN, start the development network.  This single line command will start the simulation, wait to completely start, and then lay down an initial configuration with Ansible.  

```bash
virl up --provision \
  && virl generate ansible -o setup/default_inventory.yaml \
  && cd setup \
  && ansible-playbook network_deploy.yaml \
  && cd ../
```
