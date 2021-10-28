
import requests,json
from pprint import pprint
from bs4 import BeautifulSoup
f=open("task_1a.json","r")
x=json.load(f)
d=[]
def scrape_movie_details():
    for i in x:
        for j in i:
            if j =="link":
                d.append(i[j])
    list1=[]
    c=1
    dict1={}
    for j in d:
        url=requests.get(j)
        soup=BeautifulSoup(url.text,"html.parser")
        ul=soup.find_all("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        tit=soup.find("div",class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
        title=soup.find("h1",class_="TitleHeader__TitleText-sc-1wu6n3d-0")
        a=tit.find_all("li",class_="ipc-inline-list__item")
        s=0
        for i in a:
            if s==2:
                dict1["runtime"]=i.text

            s+=1
        a=tit.find("li",class_="ipc-inline-list__item")
        for j in ul:
            gg=[]
            if "Language" in j.text:
                li = j.find_all("li")
                for i in li:
                    if "Language" in i.text:
                        div = i.find("div")
                        a= div.find_all("a")
                        for lan in a:
                            gg.append(lan.get_text())
                        dict1["language"]=gg
                    if "Country" in i.text:
                        a=i.find("a")
                        dict1["Country"]=a.get_text()
                        # print(a.text)
                    if "Release" in i.text:
                        a=i.find("li")
                        # b=(a.text).split()[2]
                        dict1["year"]=a.text
        dict1["movie_name"]=soup.find('h1').text
        dict1["genre"]=soup.find("span",class_="ipc-chip__text").text
        dict1["director"]=soup.find("div",class_="ipc-metadata-list-item__content-container").text
        dict1["img_url"]='https://www.imdb.com/'+(soup.find("a",class_="ipc-lockup-overlay ipc-focusable")["href"][:-14])
        dict1["bio_title"]=soup.find("div",class_="GenresAndPlot__TextContainerBreakpointM-cum89p-2 iJnWgZ").text
        list1.append(dict1.copy())
        # pprint(dict1)
        # print(c)
        # if c==1:
        #     break
        # c+=1
    pprint(list1[0])
    file=open("task_4a.json","w")
    json.dump(list1,file,indent=4)
    file.close()
    return list1
print(scrape_movie_details())     


# #     lang=soup.findAll("div",class_="ipc-metadata-list-item__content-container")