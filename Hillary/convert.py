import json
import csv

f = open("tweets_load.json",'r')
y = json.loads(f.read())
t = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
t.writerow(["tweet", "user"])

for x in y:
   t.writerow([x['tweet'].encode('utf-8').replace(',','\,'),x['user'].encode('utf-8')])

