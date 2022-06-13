from urllib import request
from bs4 import BeautifulSoup

from urllib.request import Request,urlopen

url="https://www.instagram.com/"


def get_data(username):

    last_url=url+username
    #So that the site does not know that it is a bot!
    request=Request(last_url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"})

    html_data=urlopen(request).read()

    soup=BeautifulSoup(html_data,"html.parser")

    data=soup.find("meta",property="og:description").attrs["content"]

    data=data.split("-")[0]

    data=data.split(" ")

    name=soup.find("meta",property="og:title").attrs["content"]

    





    try:

        print("Infotmation : "+name)
        print("Follower : "+data[0])

        print("Followed : "+data[2])

        print("Number of posts : "+data[4])



    except:
        print("Someting went wrong...")

username=input("Enter a username : ")

get_data(username)





