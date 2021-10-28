import json 
from pprint import pprint
f=open("task_1a.json","r")
x=json.load(f)
def find_year_wise(movies):
    years=[]
    for i in movies:
        for j in i:
            if j=="year":
                years.append(i[j])
    d=[]
    for i in years:
        if i not in d:
            d.append(i)
    movie_dict={j:[] for j in years}
    for i in movies:
        for k in i:
            for x in d:
                if str(x)==str(i[k]):
                    movie_dict[x].append(i)
    f=open("task_2a.json","w")
    json.dump(movie_dict,f,indent=4)
    f.close()    
    return movie_dict
task2 = find_year_wise(x)
pprint(task2)