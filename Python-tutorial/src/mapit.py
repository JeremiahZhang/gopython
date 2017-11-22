#! /usr/bin/python3
# mapit.py - Launches a map in the browser using an address from
# the command line or clipboard.

import sys
import webbrowser

if len(sys.argv) > 1:
    # Get address from command line.
