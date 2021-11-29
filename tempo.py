cookie = driver.find_element_by_css_selector('')
cookie.click()

time.sleep(10)

https://appsso.eurostat.ec.europa.eu/nui/show.do?query=BOOKMARK_DS-645593_QID_4FECA14_UID_-3F171EB0&layout=PERIOD,L,X,0;REPORTER,L,Y,0;PARTNER,C,Z,0;PRODUCT,L,Z,1;FLOW,L,Z,2;INDICATORS,C,Z,3;&zSelection=DS-645593INDICATORS,VALUE_IN_EUROS;DS-645593PARTNER,EU27_2020_EXTRA;DS-645593PRODUCT,TOTAL;DS-645593FLOW,1;&rankName1=PARTNER_1_2_-1_2&rankName2=INDICATORS_1_2_-1_2&rankName3=FLOW_1_2_-1_2&rankName4=PRODUCT_1_2_-1_2&rankName5=PERIOD_1_0_0_0&rankName6=REPORTER_1_2_0_1&sortC=ASC_-1_FIRST&rStp=&cStp=&rDCh=&cDCh=&rDM=true&cDM=true&footnes=false&empty=true&wai=false&time_mode=NONE&time_most_recent=false&lang=EN&cfo=%23%23%23%2C%23%23%23.%23%23%23&cxt_bm=1&lang=en


time.sleep(5)
search_bar2= driver.find_element_by_css_selector('input.ytd-searchbox')
search_bar2.click()
search_bar2.send_keys("Merkel last Speech")

time.sleep(3)

search_bar2.send_keys(Keys.ENTER)
search_bar2.send_keys(Keys.ENTER)


time.sleep(5)
driver.back()

time.sleep (7)
driver.forward()

time.sleep(5)
search_bar2.click()
search_bar2.clear()














search_bar2.send_keys("Thank you for listening freyr")
time.sleep(3)
search_bar2.click()
search_bar2.send_keys(Keys.ENTER)
search_bar2.send_keys(Keys.ENTER)


#search= driver.find_element_by_css_selector('#search-icon-legacy')

time.sleep(20)

video=driver.find_element_by_css_selector('ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2) > yt-formatted-string:nth-child(2)')
time.sleep(5)

video.click()

time.sleep(7)

skip= driver.find_element_by_css_selector('.ytp-ad-skip-button')
skip.click()

time.sleep(2)

salta= driver.find_element_by_css_selector('.ytp-ad-skip-button')
salta.click()

time.sleep(15)
driver.quit()
