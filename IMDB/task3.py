import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json
f=open("task_1a.json","r")
rt=json.load(f)
years,d=[],set()
def group_by_decade():
    for i in rt:
        for j in i:
            if j=="year":
                years.append(i[j])
                d.add(i[j])
    movie_dict={j:[] for j in years}
    for i in rt:
        for k in i:
            for x in d:
                if str(x)==str(i[k]):
                    movie_dict[x].append(i) 
    moviedec,list1={},[]
    for j in movie_dict:
        x=j.replace("(","")
        y=x.replace(")","")
        mod=int(y)%10
        decode=int(y)-mod
        if decode not in list1:
            list1.append(decode)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movie_dict:
            k=x.replace("(","")
            l=k.replace(")","")
            for m in movie_dict[x]:
                if int(l)<=dec10 and int(l)>int(i):
                    moviedec[i].append(m)
    file=open("task_3a.json","w")
    json.dump(moviedec,file,indent=4)
    file.close()
    return moviedec
pprint(group_by_decade())