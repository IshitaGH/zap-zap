#!/usr/bin/env python3
import requests

url = 'http://127.0.0.1:8000/endpoints/change-target-photo/4/'
files = {'file': open('../media/remy.jpg', 'rb')}

r = requests.post(url, files=files)
r.text
print(r.text)