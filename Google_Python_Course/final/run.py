#!/usr/bin/env python3

import os
import requests

dir = 'supplier-data/descriptions'
url = 'http://34.28.219.79/fruits/'
files = os.listdir(dir)

for file in files:
  path = os.path.join(dir, file)
  description = {}
  with open(path) as opened:
    lines = opened.readlines()
    description['name'] = lines[0].strip()
    description['weight'] = [int(lbs) for lbs in str.split(lines[1]) if lbs.isdigit()][0]
    description['description'] = lines[2].strip()
    description['image_name'] = '{}.jpeg'.format(file[:3])

  response = requests.post(url, json=description)
  print(response.request.url)
  print(response.request.body)
  code = response.status_code

  if code == 201:
    print("Upload successful")
  else:
    print("Error code {}".format(code))