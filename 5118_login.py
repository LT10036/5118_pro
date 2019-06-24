
# -------------------------------------------------------------------------------
# 5118普 通 账 号 一 天只 能 搜 索 3 次
# -------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


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


opt = Options()
opt.add_argument('"disable-infobars"')
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
driver.get('https://www.5118.com/')
time.sleep(2)


# 搜 索 方 法 一（点击搜索按钮）
driver.find_element_by_xpath('//*[@id="page-1"]/div[1]/div/div[3]/div[2]/input').send_keys(key_word)
driver.find_element_by_xpath('//*[@id="page-1"]/div[1]/div/div[3]/div[2]/a').click()
time.sleep(2)
handers = driver.window_handles
driver.switch_to.window(handers[-1])

# 搜 索 方 法 二 （直 接 打 开 网 址）
# driver.get('https://so.5118.com/all/%E5%86%9C%E4%B8%9A')
f = open("5118.txt",'a')
while True:
    try:
        time.sleep(3)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        max_lin =  driver.find_elements_by_xpath('//*[@id="__layout"]/section/div[3]/div[1]/div[2]/div[1]/ul[1]/li')
        for i in max_lin:
            mix_link = i.find_element_by_xpath('./a').get_attribute('href')
            print(mix_link)
            f.write(mix_link)
            f.write('\n')
        time.sleep(5)
        driver.find_element_by_link_text('下一页>').click()
    except:
        print('翻页结束')
        f.close()
        break


