#!/usr/bin/env python3


from pprint import pprint

import requests


endpoint = "http://data.nba.net/"
r = requests.get(endpoint)
pprint(r.json())
