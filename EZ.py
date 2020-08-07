# OpenOPS - Unity, Dell EMC Unity/Unity XT/UnityVSA Monitor
# Unity: Unity 480
# Unisphere Version: 5.1.0.1.3.200
# Programe: Python 3.8
# Stage: prototype
# Author: QD888
# Tested: 7th Aug. 2020

# Import libraries
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
from urllib.parse import urlencode
from urllib.parse import quote

# Set up endpoint and authentication credentials
endpoint = 'https://IP address'
username = 'username'
password = 'password'

# Get base system information, Not required authentication
api = '/api/types/basicSystemInfo/instances'
url = endpoint + api
res0 = requests.get(url,verify=False)
print(res0.text)

# Set up endpoint and authentication credentials
api = '/api/types/system/instances?fields=serialNumber'
url = endpoint + api
auth = HTTPBasicAuth(username, password)

# Retrieve header token
headers = {
    'X-EMC-REST-CLIENT': 'true',
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Accept-Language': 'en-US',
}
res = requests.get(url, headers=headers, auth=auth, verify=False)

token = dict(res.headers)['EMC-CSRF-TOKEN']
cookies = dict(res.headers)['Set-Cookie']
print(res.text)


# Get response, example: system capacity
api = '/api/types/systemCapacity/instances?fields=id,sizeTotal,sizeUsed,sizeFree'
url = endpoint + api
headers = {
    'X-EMC-REST-CLIENT': 'true',
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Accept-Language': 'en-US',
}
response = requests.get(url, headers=headers, auth=auth, verify=False)
print(response.text)



# Post Response, example: logout
api = '/api/types/loginSessionInfo/action/logout'
data = {
    'localCleanupOnly' : 'true'
}

headers = {
    'X-EMC-REST-CLIENT': 'true',
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Accept-Language': 'en-US'
}

url = endpoint + api
response2 = requests.post(url, headers=headers, json=data, cookies=res.cookies, verify=False)
print(response2.text)
