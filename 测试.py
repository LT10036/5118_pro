

# page = requests.get(hre)
# page.encoding = 'gb2312'
# page_source = etree.HTML(page.text)
# time.sleep(2)
# tit = page_source.xpath('//*[@id="main"]/h1/text()')
# title = root + str(tit[:-1]) + '.txt'
# w = open(title, 'a', encoding='utf-8')
# con_s = page_source.xpath('//*[@id="content"]')
# for i in con_s:
#     w.write(i)
#     w.write('\n')
# w.close()



#
#
# #coding=utf-8
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# option = Options()
# option.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default')
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('https://www.baidu.com')




import re

f = open('5118.txt','r')
while True:
    hre = f.readline()
    if not hre:
        new = re.findall('https.*c81f66ed8109',hre)
        print(new[0])
