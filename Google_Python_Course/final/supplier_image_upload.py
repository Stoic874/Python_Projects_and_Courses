#!/usr/bin/env python3

import requests
import sys
import os

dir = sys.argv[1]
url = 'http://34.28.219.79/upload/'
images  = os.listdir(dir)


for im in images:
  path = os.path.join(dir, im)
  ext = os.path.splitext(path)[1]
  if ext.lower() == '.jpeg':
    with open(path, 'rb') as opened:
      response = requests.post(url, files={'file': opened})

      #print(response.request.url)
      #print(response.request.body)

      code = response.status_code
      if code == 201:
        print("{} upload successful".format(im))
      else:
        print("Error Code: {}".format(code))

