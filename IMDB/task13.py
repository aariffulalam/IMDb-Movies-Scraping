import json
from pprint import pprint
f=open("task_4a.json","r")
x=json.load(f)
g=open("task_12a.json","r")
y=json.load(g)
list1=[]
def scrape_movie_details():
    for i,j in zip(x,y):
        i["cost"]=j
        list1.append(i)
    file=open("task_13a.json","w")
    json.dump(list1,file,indent=4)
    file.close()
    return list1
pprint(scrape_movie_details())