# -*- coding: utf-8 -*-
# Open the websites which I browse everyday.

import sys
import webbrowser

if len(sys.argv) > 1:
    if sys.argv == 'aqi':
        address = 'http://aqicn.org'
    elif sys.argv == 'aqistudy':
        address = 'https://www.aqistudy.cn/'
    elif sys.argv == 'gmail':
        address = 'https://mail.google.com'
    else:
        address = 'https://www.google.com/'
else:
    address = 'https://www.google.com/'
