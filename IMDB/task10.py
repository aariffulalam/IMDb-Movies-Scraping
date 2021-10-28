import json 
from pprint import pprint
x=open("task_4a.json","r")
y=json.load(x)
director_name={}
def analyse_language_and_directors():
    for i in y:
        for j in i:
            # k=
            director_name[i["director"]]={}
            break
    for i in range(len(y)):
        for k in director_name:
            if k==  y[i]["director"]:
                for j in y[i]["language"]:
                    director_name[k][j]=0
    for i in range(len(y)):
        for k in director_name:
            if k==  y[i]["director"]:
                for j in y[i]["language"]:
                    director_name[k][j]+=1
                    # print(director_name)
    file=open("task_10a.json","w")
    json.dump(director_name,file,indent=4)
    file.close()
    return director_name
print(analyse_language_and_directors())