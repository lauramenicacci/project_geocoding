from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget


driver = webdriver.Firefox(executable_path = r'C:\Program Files (x86)\geckodriver-v0.30.0-win64\geckodriver.exe')


driver.get('https://appsso.eurostat.ec.europa.eu/nui/show.do?query=BOOKMARK_DS-645593_QID_4FECA14_UID_-3F171EB0&layout=PERIOD,L,X,0;REPORTER,L,Y,0;PARTNER,C,Z,0;PRODUCT,L,Z,1;FLOW,L,Z,2;INDICATORS,C,Z,3;&zSelection=DS-645593INDICATORS,VALUE_IN_EUROS;DS-645593PARTNER,EU27_2020_EXTRA;DS-645593PRODUCT,TOTAL;DS-645593FLOW,1;&rankName1=PARTNER_1_2_-1_2&rankName2=INDICATORS_1_2_-1_2&rankName3=FLOW_1_2_-1_2&rankName4=PRODUCT_1_2_-1_2&rankName5=PERIOD_1_0_0_0&rankName6=REPORTER_1_2_0_1&sortC=ASC_-1_FIRST&rStp=&cStp=&rDCh=&cDCh=&rDM=true&cDM=true&footnes=false&empty=true&wai=false&time_mode=NONE&time_most_recent=false&lang=EN&cfo=%23%23%23%2C%23%23%23.%23%23%23&cxt_bm=1&lang=en')
original_window = driver.current_window_handle

time.sleep(5)

select_partner= driver.find_element_by_xpath('//*[@id="PARTNER"]/button')
select_partner.click()

wait = WebDriverWait(driver, 10)

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

wait.until(EC.title_is("SeleniumHQ Browser Automation"))


deselect1= driver.find_element_by_xpath('//*[@id="ck_EU27_2020_EXTRA"]')
deselect2= driver.find_element_by_xpath('//*[@id="ck_EU27_2020_INTRA"]')

time.sleep(4)

deselect1.click()
deselect2.click()

x_countries=['//*[@id="ck_IN"]', '//*[@id="ck_BR"]', '//*[@id="ck_BR"]', '//*[@id="ck_RU"]', '//*[@id="ck_CN"]', '//*[@id="ck_ZA"]','//*[@id="ck_US"]']

x_countries[0].click()