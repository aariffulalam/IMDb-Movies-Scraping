import requests,json ,time
from pprint import pprint
f=open("task_12a.json","r")
x=json.load(f)
c=0
list1,list2 = [],[]
sett=set()
def movies_detials():
    for i in x:
        dict1={}
        for  j in i:
            list1.append(j["name"])
        for y in i:
            dict2={}
            dict2["name"]=y["name"]
            dict2["num_movies"]=list1.count(y["name"])
            dict1[y["imdb_id"]]=dict2
        list2.append(dict1)
    file=open("task_15a.json","w")
    json.dump(list2,file,indent=4)
    file.close()
    return list2

print(movies_detials())