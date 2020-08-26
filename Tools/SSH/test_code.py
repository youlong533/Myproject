from selenium import webdriver
import time,os
def test_login1():
    chrome_driver = './chromedriver'
    driver = webdriver.Chrome(executable_path= chrome_driver)
    driver.get("https://talent.lenovo.com.cn/")
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_class_name("close-qrcode").click()
    time.sleep(2)
    driver.find_element_by_class_name("recruitment_user").click()
    time.sleep(2)
    driver.switch_to.frame(0)
    driver.find_element_by_xpath('//*[@id="tuser"]').send_keys('18232202828')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tpass"]').send_keys("zhaoqian1989")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ldILoginForm"]/div[3]/input').click()
    time.sleep(2)
    # cookie = driver.get_cookie()
    # print(cookies)
    input('Press Enter to exit...')

test_login1()