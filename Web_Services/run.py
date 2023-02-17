#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback"
files = os.listdir(dir)
url = "http://35.232.241.254/feedback/"
for f in files:
    fullname = os.path.join(dir, f)
    feedback = {}
    with open(fullname) as file:
        lines = file.readlines()
        feedback["title"] = lines[0].strip()
        feedback["name"] = lines[1].strip()
        feedback["date"] = lines[2].strip()
        feedback["feedback"] = lines[3].strip()

    response = requests.post(url, json=feedback)
    print(response.request.url)
    print(response.request.body)

    code = response.status_code

    if code == "201":
        print("Upload successful")
    else:
        print("Error Code: {}".format(code))
