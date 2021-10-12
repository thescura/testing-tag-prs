import requests

wa_resp = requests.get('https://data.cdc.gov/')
print(wa_resp)
# json = dict(wa_resp.json())
# print(json)
# state = json['state']
# print(wa_resp.json())
# id_resp = requests.get('https://api.covidtracking.com/v1/states/id/current.json')
# print(id_resp.json())