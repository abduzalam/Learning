## install request package as shown below

#from setuptools import Command


#type command " pip requests " this does not work try below Command
#python -m pip install requests

import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('people currently in space are:\n')
for person in json['people']:
    print(person['name'])