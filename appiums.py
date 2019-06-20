# encoding:utf-8
# -*-encoding:utf-8-*-
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = '192.168.76.101:5555'
desired_caps['appPackage'] = 'com.esbook.reader'
desired_caps['appActivity'] = '.activity.ActFragmentContent'

driver = webdriver.Remote('http://192.168.56.1:4723/wd/hub', desired_caps)



el1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ImageView[4]')
el1.click()
time.sleep(8)
el2=driver.find_element_by_xpath('//android.view.View[@content-desc="男生分类"]')

print (el2.get_attribute('name'))
time.sleep(8)
el3=driver.find_element_by_xpath('//android.view.View[@content-desc="武侠仙侠"]')

print (el3.get_attribute('name'))

el4=driver.find_element_by_xpath('')