/usr/bin/python3

# This script will collect the system information 

import os commands

serial_number = commands.getoutput('dmidecode -s system-serial-number')
