from lib2to3.pgen2 import driver
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random

with open('messages.txt','r',encoding='utf-8') as messages:
    messagelist=list()
    text=messages.read()
    messagelist=text.split("\n")


print(messagelist)


def start():
    driver=webdriver.Chrome()
    driver.implicitly_wait(3)  #Selenyum choremu açtıgında yanıt alamazsa 3sn tolerans tanı!
    driver.get("https://web.whatsapp.com/")
    input("QR kodunu okuttuysanız bir tuşa basıp enterleyin..")

start()


