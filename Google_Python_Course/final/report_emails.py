#!/usr/bin/env python3

import os
import sys
import reports
from datetime import date
import emails

today = date.today().strftime('%d/%m/%Y')

def process_data():
    dir = 'supplier-data/descriptions'
    files = os.listdir(dir)
    paragraph = ""

    for file in files:
      path = os.path.join(dir, file)
      with open(path) as opened:
          lines = opened.readlines()
          #make a list of dictionaries
          dict = ""
          name = lines[0].strip()
          weight = lines[1].strip()
          paragraph += ("name: {} <br/>".format(name) + "weight: {} lbs <br/><br/>".format(weight)) 
    return paragraph
    
   

def main(argv):
    title = "Processed Update on {}".format(today)
    paragraph = process_data()
    #generate a report
    reports.generate_report("/tmp/processed.pdf", title, paragraph)

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    message = emails.generate_email(sender, recipient, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)
