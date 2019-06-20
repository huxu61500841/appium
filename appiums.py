# encoding:utf-8
# -*-encoding:utf-8-*-
from appium import webdriver
import time
#创建一个字典
desired_caps = {}
#将配置信息放入字典里面
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = '192.168.76.101:5555'
desired_caps['appPackage'] = 'com.esbook.reader'
desired_caps['appActivity'] = '.activity.ActFragmentContent'
#发送请求
driver = webdriver.Remote('http://192.168.56.1:4723/wd/hub', desired_caps)


#定位xpath
el1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ImageView[4]')
el1.click()
#休眠8 S
time.sleep(8)
el2=driver.find_element_by_xpath('//android.view.View[@content-desc="男生分类"]')

#找到并打印关键字
print (el2.get_attribute('name'))
time.sleep(8)

el3=driver.find_element_by_xpath('//android.view.View[@content-desc="武侠仙侠"]')

print (el3.get_attribute('name'))