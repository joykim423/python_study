# 셀레니움 및 크롬 드라이버 사전 설치가 필요합니다. 

# 자동화 테스트를 위해 셀레니움을 불러옵니다. 
from selenium import webdriver
from time import sleep

# 크롬 웹 드라이버의 경로를 설정합니다.
# 예시) driver = webdriver.Chrome('/Users/kimgunwoo/Downloads/chromedriver')
driver = webdriver.Chrome('/Users/kimgunwoo/Downloads/chromedriver')

# 크롬을 통해 이카운트이알피 로그인 화면에 접속합니다.
driver.get('https://login.ecount.com/Login/?shortcut=Y')

# 코드, 아이디와 비밀번호를 입력합니다. (0.5초씩 기다리기)
sleep(0.5)
driver.find_element_by_name('com_code').send_keys('87762')
sleep(0.5)
driver.find_element_by_name('id').send_keys('dskim')
sleep(0.5)
driver.find_element_by_name('passwd').send_keys('jltech1234')

# XPath를 이용해 로그인을 시도합니다. (2.0초 기다리기)
driver.find_element_by_xpath('//*[@id="save"]').click()
sleep(2.0)

# XPath를 이용해 MyPage -> ERP확인 -> (구매현황) -> 금주(~오늘) -> 엑셀 순으로 클릭합니다.
driver.find_element_by_xpath('//*[@id="ma6"]').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="ma9008"]').click()
sleep(5.0)
driver.find_element_by_xpath('/html/body/div[8]/div/div[4]/div[1]/div[2]/div[2]/div[1]/div/div[4]/button').click()
sleep(3.0)
driver.find_element_by_xpath('//*[@id="outputExcel"]').click()
sleep(1.0)

# XPath를 이용해 발주서현황 -> 금주(~오늘) -> 엑셀 순으로 클릭합니다.
driver.find_element_by_xpath('//*[@id="ma9010"]').click()
sleep(5.0)
driver.find_element_by_xpath('/html/body/div[8]/div/div[4]/div[1]/div[2]/div[2]/div[1]/div/div[4]/button').click()
sleep(3.0)
driver.find_element_by_xpath('//*[@id="outputExcel"]').click()
sleep(1.0)

# XPath를 이용해 미입고현황 -> 검색 -> 엑셀 순으로 클릭합니다.
driver.find_element_by_xpath('//*[@id="ma9011"]').click()
sleep(5.0)
driver.find_element_by_xpath('//*[@id="searchGroup"]').click()
sleep(3.0)
driver.find_element_by_xpath('//*[@id="outputExcel"]').click()