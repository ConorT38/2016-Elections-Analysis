import json

with open('tweets_load.json','r') as f:
    y = json.loads(json.dumps(f.read()))
    data = {'empty':0}
    e = open('location.json','a')
    for x in y:
        for key in data.keys():
                #print x['location']
                if x['location'] in key:
                    data[key] +=1
                    print data
                else:
                    data[x['location']] = 1
                    print data
    e.write(data)
