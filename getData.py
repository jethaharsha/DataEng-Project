import urllib.request, json
from datetime import date

shit=urllib.request.urlopen("http://rbi.ddns.net/getBreadCrumbData")
data = json.loads(shit.read())
#print(len(data))
dt= date.today()
today=dt.strftime("%Y-%m-%d")
filename="examples/clients/cloud/python/data/"+today+".json"
with open(filename, "w") as fn:
    json.dump(data, fn)
print(len(data))

