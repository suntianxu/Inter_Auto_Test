from selenium import webdriver
from selenium.webdriver.common.by import By
import time
drive = webdriver.Chrome()
drive.get('http://www.baidu.com')
time.sleep(3)
#drive.find_element_by_xpath("//input[@id='kw' and @name='wd']").send_keys('baidu')
#drive.find_elements_by_css_selector('.s_ipt').send_keys('baidu')
#drive.find_element(By.ID,"kw").send_keys('1111')
drive.find_element("id","kw").send_keys('1111')
drive.implicitly_wait(2)
#定位编码
st = drive.current_window_handle
print(st)
#截图
drive.save_screenshot('page.png')
drive.quit()