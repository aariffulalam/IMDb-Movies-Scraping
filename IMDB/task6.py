import json
from pprint import pprint
f=open("task_4a.json","r")
x=json.load(f)
dict2,d,se={},[],set()
def analyse_movies_language():
    for i in x:
        for j in i:
            if j=="language":
                for k in i[j]:
                    d.append(k)
                    se.add(k)
        for j in se:
            dict2[j] = d.count(j)
    file=open("task_6a.json","w")
    json.dump(dict2,file,indent=4)
    file.close()
    return dict2
print(analyse_movies_language())