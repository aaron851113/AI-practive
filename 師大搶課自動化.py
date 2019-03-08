# Python Selenium Practice 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


#疑難排解:
#https://medium.com/@Epicure1709/%E4%BD%BF%E7%94%A8python%E7%9A%84selenium%E6%99%82%E9%81%87%E5%88%B0%E7%9A%84%E4%B8%80%E4%BA%9B%E5%B0%8F%E5%95%8F%E9%A1%8C-7fb5de198ff7


student_id =  '...'
password = '......'

class_id = '1016'


#kind = int(input('(1)通識課程  (2)教育學程  (3)一般體育  (4)一般科目\n Please input class kind..> '))
kind = 1
print()
kind_id = 0
if kind == 1:
    kind_id = 'radioGeneral-inputEl' 
elif kind == 2:
    kind_id = 'radioEducation-bodyEl'
elif kind == 3:
    kind_id = 'radioEducation-bodyEl'
elif kind == 4:
    kind_id = 'radioOther-inputEl'





print('搶課學號:',student_id)
print('開課序號',class_id,'\n')

for j in range(1,10):
    #前往目標網頁
    check_code = 'nan'
    
    while check_code == 'nan' :
        print('第',j,'次開啟 : chromedriver')
        driver = webdriver.Chrome('./chromedriver')
        print('進入選課登入頁面')
        driver.get("http://cos4.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW")
        print('輸入帳號密碼')
        driver.find_element_by_id("userid-inputEl").clear()
        driver.find_element_by_id("userid-inputEl").send_keys(student_id)
        driver.find_element_by_id("password-inputEl").clear()
        driver.find_element_by_id("password-inputEl").send_keys(password)
        print('抓取無障礙輸入碼...',end=' ')
        driver.find_element_by_id("imageBoxTurnIntoTextButton-btnIconEl").click()
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
          
        first = soup.find(id="messagebox-1001-displayfield-inputEl")
        
        if first != None:
            for i in first:
                if i != None:
                    check_code = i.find('b').string
                    #按下ok鍵
                    driver.find_element_by_id("button-1005-btnIconEl").click()
                    
        else:
            print('重新Selenium')
            driver.close()
            
    print('無障礙輸入輔助碼為:',check_code)
    driver.find_element_by_id("validateCode-inputEl").click()
    driver.find_element_by_id("validateCode-inputEl").send_keys(check_code)
    #進入選課
    driver.find_element_by_id("button-1016").click()
    time.sleep(3.5)
    driver.find_element_by_id("button-1005").click()
    time.sleep(1.5)
    #進入我的選課
    driver.find_element_by_id("button-1017-btnIconEl").click()
    time.sleep(4)
    
    #登記(須先切換frame)
    driver.switch_to.frame(0)
    driver.find_element_by_id("add-btnInnerEl").click()
    time.sleep(2)
    
    #選擇通識領域
    print('選擇領域，輸入開課序號')
    driver.find_element_by_id("radioOther-inputEl").click()
    time.sleep(0.5)
    driver.find_element_by_id(kind_id).click()
    time.sleep(1.5)
    driver.find_element_by_id("serialNo-inputEl").clear()
    driver.find_element_by_id("serialNo-inputEl").click()
    driver.find_element_by_id("serialNo-inputEl").send_keys(class_id)
    driver.find_element_by_id("button-1059-btnIconEl").click()
    time.sleep(1.5)
    
    print('進行搶課:',end =' ')
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='資料科學與程式設計'])[1]/following::div[1]").click()
    driver.find_element_by_id("save-btnInnerEl").click()
    time.sleep(1)
    driver.find_element_by_id("button-1005-btnIconEl").click()
    time.sleep(1)
    for i in range(1,120):
        print(i,end=' ')
        driver.find_element_by_id("button-1059-btnIconEl").click()
        time.sleep(1)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='資料科學與程式設計'])[1]/following::div[1]").click()
        driver.find_element_by_id("save-btnInnerEl").click()
        time.sleep(2)
        driver.find_element_by_id("button-1005-btnIconEl").click()
        time.sleep(2)
    
    #登出(須先切換frame)
    print('\n登出\n')
    driver.switch_to.default_content()
    driver.find_element_by_id("button-1017-btnIconEl").click()
    time.sleep(4)
    driver.find_element_by_id("button-1005-btnIconEl").click()
    time.sleep(4)
    driver.exit()

