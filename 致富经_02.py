
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from lxml import etree
opt = Options()
opt.add_argument('"disable-infobars"')
driver = webdriver.Chrome(chrome_options=opt)
root = 'C:\\Users\\Administrator\\Desktop\\zhifujing\\'
f = open('123.txt','r')
# 打开主页

while True:
    hre = f.readline()
    if not hre:
        break
    else:

        try:
            driver.get(hre)
            tit = driver.find_element_by_xpath('//*[@id="main"]/h1').text
            print(hre)
            print(tit)

            con_s = driver.find_element_by_xpath('//*[@id="content"]').text
            title = root + tit + ".txt"
            w = open(title,'a',encoding='utf-8')
            w.write(con_s)
            w.write('\n')
        except:
            continue












