import json
from pprint import pprint
f=open("task_4a.json","r")
x=json.load(f)
dict2,d,se={},[],set()
def analyse_movies_genre():
    for i in x:
        for j in i:
            if j=="genre":
                d.append(i[j])
                se.add(i[j])
        for j in se:
            dict2[j] = d.count(j)
    file=open("task_11a.json","w")
    json.dump(dict2,file,indent=4)
    file.close()
    return dict2
print(analyse_movies_genre())