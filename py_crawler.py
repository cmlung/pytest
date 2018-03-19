import csv
import json

import requests

url_twse = 'http://www.tse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20180201&stockNo=2330'
res = requests.get(url_twse)
s = json.loads(res.text)
# print(json.dumps(s, indent=5, sort_keys=True))

# for data in (s['data']):
#    print(data)

of = open(r'c:\pyout\output.csv', 'w', newline='')
ow = csv.writer(of)
ow.writerow(s['title'])

ow.writerow(s['fields'])

for data in (s['data']):
    ow.writerow(data)

of.close()
