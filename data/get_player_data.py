#!/usr/bin/env python3


from pprint import pprint

import requests


endpoint = "http://data.nba.net/10s/prod/v1/2018/players.json"
r = requests.get(endpoint)
pprint(r.json())
