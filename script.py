#!/usr/bin/python

import requests
import json

API_benton="https://data.cdc.gov/resource/8396-v7yb.json?state_name=Oregon&county_name=Benton County"
API_licoln="https://data.cdc.gov/resource/8396-v7yb.json?state_name=Oregon&county_name=Lincoln County"
API_linn="https://data.cdc.gov/resource/8396-v7yb.json?state_name=Oregon&county_name=Linn County"

payload = ""
headers = {
    'content-type': "application/json"
    }

REQ = requests.request("GET", API_benton, data=payload, headers=headers)
JSON = REQ.json()
latest_benton = JSON.pop()
print("Benton County:")
print(latest_benton)
print("\r")

REQ = requests.request("GET", API_licoln, data=payload, headers=headers)
JSON = REQ.json()
latest_licoln = JSON.pop()
print("Lincoln County:")
print(latest_licoln)
print("\r")

REQ = requests.request("GET", API_linn, data=payload, headers=headers)
JSON = REQ.json()
latest_linn = JSON.pop()
print("Linn County:")
print(latest_linn)
