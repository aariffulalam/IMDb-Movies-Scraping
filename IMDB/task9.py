import time,random,requests,json
x=open("task_4a.json","r")
y=json.load(x)
random_sleep=random.randint(1,3)
def scrape_movie_details():
    for i in y:
        print(i)
        for j in range(10):
            print(str(i)+"\r",end="")
            time.sleep(random_sleep)
scrape_movie_details()