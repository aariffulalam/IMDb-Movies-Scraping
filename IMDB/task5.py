import json
from pprint import pprint
f=open("task_4a.json","r")
x=json.load(f)
c,cc=0,[]
def scrape_movie_details():
    c=0
    for i in x:
        cc.append(i)
        if c==10:
            break
        c+=1
    file=open("task_5a.json","w")
    json.dump(cc,file,indent=4)
    file.close()
    return cc
pprint(scrape_movie_details())