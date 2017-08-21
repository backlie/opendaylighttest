import requests
import json

def odl_check_nodes(controller_address, auth_head):
    url='http://'+controller_address+':8181/restconf/operational/opendaylight-inventory:nodes/'
    headers={ 'Authorization' : auth_head }
    return requests.get(url,headers=headers)

if __name__=='__main__':
    controller_address='10.69.35.85'
    auth_head='Basic YWRtaW46YWRtaW4='
    result=odl_check_nodes(controller_address=controller_address,auth_head=auth_head)
    print result
    outcome=json.loads(result.text)
    print outcome