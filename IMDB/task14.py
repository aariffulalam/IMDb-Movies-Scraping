import requests,json ,time
from pprint import pprint
f=open("task_12a.json","r")
x=json.load(f)
c=0
list1 = []
def analyse_co_actors():
    for i in x:
        dict1={}
        for j  in range(len(i)-1):
            dict2={}
            list2=[]
            dict2['imdb_id'] = i[j+1]["imdb_id"]
            dict2["name"] = i[j+1]["name"]
            c=0
            for k in x:
                if i[j] in k and i[j+1] in k:
                    c+=1
            dict2["num_movies"]=c
            list2.append(dict2)
            dict1[i[j]["imdb_id"]]={"name":i[j]["name"],"frequent_co_actors":list2}   
        list1.append(dict1)
    file=open("task_14a.json","w")
    json.dump(list1,file,indent=4)
    file.close()
    return list1
print(analyse_co_actors())