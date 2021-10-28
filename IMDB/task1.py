import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(url.content,"html5lib")
def fun():
    title=soup.find_all(None,class_="titleColumn")
    ran=soup.find_all(None,class_="ratingColumn imdbRating")
    rt=[]
    for x,y in zip(title,ran):
        for u,v in zip(x.find("a"),x.select(".secondaryInfo")):
            # print(u,"\n",v)
            t={}
            r=str(x).split()
            k=(r[4].replace("href="+'"'+"/title",""))
            link="http://www.imdb.com/title"+k.replace('"',"")
            e=(x.get_text()).split()
            t["position"],t["name"],t["rating"],t["year"],t["link"]=e[0],u,(y.get_text()).strip("  \n "),v.get_text(),link
        rt.append(t)
        f=open("task_1a.json","w")
        json.dump(rt,f,indent=4)
        f.close()
    return rt
x=fun
pprint(x())