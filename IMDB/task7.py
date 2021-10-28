import json
from pprint import pprint
f=open("task_4a.json","r")
x=json.load(f)
dict2,d,se={},[],set()
def get_movie_list_details():
    for i in x:
        for j in i:
            if j=="director":
                d.append(i[j])
                se.add(i[j])
        for j in se:
            dict2[j] = d.count(j)
    file=open("task_7a.json","w")
    json.dump(dict2,file,indent=4)
    file.close()
    return dict2
pprint(get_movie_list_details())