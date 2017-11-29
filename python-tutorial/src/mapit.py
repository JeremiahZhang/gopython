#! /usr/bin/python3
# mapit.py - Launches a map in the browser using an address from
# the command line or clipboard.

import sys
import webbrowser
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

print("Finished! Go to your browser to see the location.")
