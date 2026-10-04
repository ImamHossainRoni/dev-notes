import requests
from pprint import pprint
r = input()
p = "http://ip-api.com/json/" + r
r = requests.get(p)
r = r.json()
# pprint(r)
output = str(r['city']+', '+r['regionName']+' ('+r['country']+')')
pprint(output)

