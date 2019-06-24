

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

w = open('123.txt','a')
# 打开主页
opt = Options()
opt.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User ')
opt.add_argument('"disable-infobars"')
driver = webdriver.Chrome(chrome_options=opt)
driver.get('https://www.zhifujing.org/sannong/')


for num in range(30):
    try:
        # 下滑到底部
        time.sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(3)
        max_lin = driver.find_elements_by_xpath('//*[@id="main"]/div/div/h3/a')
        for i in max_lin:
            hre = i.get_attribute('href')
            print(hre)
            w.write(hre)
            w.write('\n')

        driver.find_element_by_link_text('下一页').click()
    except:
        break

w.close()