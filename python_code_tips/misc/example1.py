#! /usr/bin/env python
"""Example Python script.

Copyright (c) 2018 Cisco and/or its affiliates."""

import os

def say_hello(name):
    """Function that will say hello to someone.
    """

    # Print out a hello message to the name given
    print("Hello there {name}. It's great to see you.".format(name = name))



def script_details():
    """Function that reports by printing to screen some details about the execution of the script."""
    # Get the current directory and print it out.
    cur_dir = os.getcwd()
    print("Current directory is {}".format(cur_dir))

    # Get the User ID and Group List for the User
    user_id = os.getuid()
    group_list = os.getgroups()

    # Print to screen
    print("The user id is {}".format(user_id))
    print("The user is a member of the following groups:")
    print(",".join(str(g) for g in group_list))


if __name__ == "__main__":
    # If executed as a script, run this block.

    # Check Script details
    script_details()

    # List of names, and say hello to them
    names = ["Hank","Eric","Stuart","Bryan"]
    for name in names:
        say_hello(name)
