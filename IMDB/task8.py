
import json, os
x=open("task_4a.json","r")
y=json.load(x)
list1=[]
def scrape_movie_details():
    for i in y:
        url=i["img_url"][27:38]
        ss=url.replace("/","")
        list1.append(ss)
    a={}
    for i,j in zip(list1,y):
        tt="./web_8/"+i+".json"
        if os.path.exists(tt):
            print("already have")
        else:
            x=open(tt,'w')
            json.dump(j,x,indent=4)
            x.close()
            print(j) 
scrape_movie_details()