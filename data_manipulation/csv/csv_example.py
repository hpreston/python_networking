#! /usr/bin/env python
"""This script illustrates how to manipulate csv data easily in Python with
the csv library.

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

# Import the csv library
import csv

# Open the sample csv file and print it to screen
with open("csv_example.csv") as f:
    print(f.read())

# Open the sample csv file, and create a csv.reader object
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
