import requests,json ,time
from pprint import pprint
from bs4 import BeautifulSoup
f=open("task_1a.json","r")
x=json.load(f)
d=[]
def scrape_movie_cast():
    for i in x:
        for j in i:
            if j =="link":
                d.append(i[j])
    list1=[]
    c=1
    for j in d:  
        url=requests.get(j)
        soup=BeautifulSoup(url.text,"html.parser")
        aa=soup.find_all("a",class_="ipc-lockup-overlay ipc-focusable")
        list2=[]
        for j in aa:
            dict1={}
            dict2={}
            m=j["href"][6:16]
            s=m.replace("?","")
            if "nm" in m:
                dict2["imdb_id"],dict2["name"] =s, j["aria-label"][:15]
                list2.append(dict2)
        print(c)
        c+=1
        list1.append(list2)
    file=open("task_12a.json","w")
    json.dump(list1,file,indent=4)
    file.close()
    return list1 
print(scrape_movie_cast())