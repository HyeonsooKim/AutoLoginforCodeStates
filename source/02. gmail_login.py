#02. gmail login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = 'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&scope=profile%20email&redirect_uri=https%3A%2F%2Furclass.codestates.com%2Fauth%3Fsocial_provider%3Dgoogle&propmt=consent&client_id=430860350629-p0iei83mun2uhg4ma0be52qbv8p97k8e.apps.googleusercontent.com&flowName=GeneralOAuthFlow'

driver.get(url)

id = 'sbkhs274@gmail.com'
pw = 'skyy994!274'

driver.find_element_by_id('identifierId').send_keys(id)
driver.find_element_by_id('identifierNext').click()
# driver.find_element_by_name('password').send_keys(pw)
# driver.find_element_by_class_name('btn_confirm').click()