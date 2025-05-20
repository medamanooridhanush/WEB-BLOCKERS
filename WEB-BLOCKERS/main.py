# Run this script as root
import os
import time
from datetime import datetime as dt

# Change hosts path according to your OS
hosts_path = r"C:/Windows/System32/drivers/etc"  # Use raw string to avoid escape issues
if not os.path.exists(hosts_path):
    print("Hosts file not found at:", hosts_path)
    exit()
# Localhost's IP
redirect = "127.0.0.1"

# Websites that you want to block
website_list = [
    "www.facebook.com", "facebook.com",
    "dub119.mail.live.com", "www.dub119.mail.live.com",
    "www.gmail.com", "gmail.com"
]

while True:
    # Time of your work (e.g., 8 AM to 4 PM)
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    # Mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
