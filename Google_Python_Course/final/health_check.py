
#!/usr/bin/env python3

import psutil
import subprocess
import os
import emails

cpu_usage = psutil.cpu_percent()
disk_space = psutil.disk_usage('/')
mem = psutil.virtual_memory()
#lh = subprocess.run(['nslookup', '127.0.0.1'], capture_output=True)


sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."
if cpu_usage > 80.0:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)
    print("Alert sent")
if disk_space.percent > 80.0:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email(sender, recipient, subject, body, 'None')
    emails.send_email(message)

if mem.available < (500 * 1024 * 1024):
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email(sender, recipient, subject, body, 'None')
    emails.send_email(message)

#if 'localhost' not in lh:
   # subject = "Error - localhost cannot be resolved to 127.0.0.1"
   # message = emails.generate_email(sender, recipient, subject, body, 'None')
   # emails.send_email(message)

