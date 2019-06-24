# -------------------------------------------------------------------------------
# 5118普 通 账 号 一 天只 能 搜 索 3 次
# -------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re


# hre 登 录 使用 ， 不 用 修 改
# user 用 户 名
# password 用户密码
# Key_word   要 搜 索 关 键 词

hre = 'https://account.5118.com/signin'
# user = '15831122938'
# user = '13068768472'
user = '13266915913'
password = 'zx850625'
key_word = '农业'
root = 'https://so.5118.com'
root_t = 'C:\\Users\\Administrator\\Desktop\\趣头条文本\\'


opt = Options()
opt.add_argument('"disable-infobars"')
prefs = {"profile.managed_default_content_settings.images": 2}
opt.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=opt)
driver.get(hre)


# 开 始 登 录 并 打 开 搜 索 页 面
driver.find_element_by_xpath('//*[@id="app"]/form/div[1]/div[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/form/div[2]/div/input[1]').send_keys(user)
driver.find_element_by_xpath('//*[@id="app"]/form/div[2]/div/input[2]').send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/form/div[2]/div/button').click()
time.sleep(2)



# 打开地址文本，开始获取文章

f = open('5118.txt','r')
img = open('img.txt','a')
while True:
    hre = f.readline()
    if not hre:
        break
    else:
        driver.get(hre)
        time.sleep(4)
        try:
            titile = driver.find_element_by_xpath('//*[@id="__layout"]/section/div[3]/div[1]/div/div[1]/div').text
            r_title = root_t + str(titile) + '.txt'
            w = open(r_title,'a')
            con_s = driver.find_elements_by_xpath('//*[@id="js_content"]/p')
            for i in con_s:
                con = i.text
                w.write(con)
                w.write('\n')
            w.close()
            img_s = driver.find_elements_by_xpath('//*[@id="js_content"]//img')
            imgs = open('img.txt','a')
            for mix_img in img_s:
                img_hre = mix_img.get_attribute('src')
                imgs.write(img_hre)
                imgs.write('\n')
            imgs.close()
        except:
            continue




