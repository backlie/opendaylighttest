import requests
import json

url = 'http://192.168.64.135:8181/restconf/operational/opendaylight-inventory:nodes/'
username = 'admin'
password = 'admin'
headers = {
    'Authorization' : 'Basic YWRtaW46YWRtaW4='
    }
result = requests.get(url, headers=headers)
print result
outcome = json.loads (result.text)
print outcome.keys()
