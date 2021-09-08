#01. Auto_string_input.py
#자동 검색어 입력

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

# Chrome
# driver = webdriver.Chrome(r"C:\\Users\\sbkhs\\PycharmProjects\\Auto-login\\selenium")
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Furclass.codestates.com%252Fauth%253Fsocial_provider%253Dkakao%26client_id%3D43984033602adcda52af84344f1daa74'
# url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(url)
# Firefox
# driver = webdriver.Firefox()
# Intenet explorer
# driver = webdriver.Ie()

id = 'gustn9442@naver.com'
pw = 'qweasdzxc1/'

# copy_input('//*[@id="email"]', id)
# time.sleep(1)
# copy_input('//*[@id="password"]', pw)
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="btn_g btn_confirm submit').click()

driver.find_element_by_name('email').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_class_name('btn_confirm').click()