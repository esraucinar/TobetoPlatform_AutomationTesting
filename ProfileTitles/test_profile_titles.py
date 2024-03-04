import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import loginConstants as c
from selenium.webdriver.support.ui import Select
from constants import profileTitlesConstants  as p

class Test_profileTitles():

   def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(c.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
   def teardown_method(self, method):
    self.driver.quit()

    
   @pytest.mark.parametrize("location, url", [
        (p.MY_PERSONAL_INFO_XPATH, p.MY_PERSONAL_URL),
        (p.MY_EXPERIENCE_XPATH, p.MY_EXPERIENCE_URL),(p.MY_EDUCATIONLIFE_XPATH,p.MY_EDUCATIONLIFE_URL),
        (p.MY_COMPETENCIES_XPATH,p.MY_COMPETENCIES_URL),(p.MY_CERTIFICATEDS_XPATH,p.MY_CERTIFICATEDS_URL),
        (p.MY_MEDIA_ACCOUNT_XPATH,p.MY_MEDIA_ACCOUNT_URL),(p.MY_FOREIGN_LANG_XPATH,p.MY_FOREIGN_LANG_URL),
        (p.SETTINGS_XPATH,p.SETTINGS_URL)])
  
   def test_profileTitlesAccess(self,location,url):

    epostaTextBox=self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(c.VALID_EPOSTA)
    passwordTextBox= self.driver.find_element(By.XPATH,c.PASSWORD_TEXT_BOX_XPATH)
    passwordTextBox.send_keys(c.VALID_PASSWORD)
    loginButton=self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
    loginButton.click()
    sleep(8)
    profileSummary=self.driver.find_element(By.CSS_SELECTOR, p.PROFILE_SUMMARY_CSS)
    profileSummary.click()
    profileInfo=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,p.PROFILE_INFO_XPATH)))
    profileInfo.click()
    sleep(2)
    profileTitles=self.driver.find_element(By.XPATH , location)
    profileTitles.click()
    sleep(1)
    assert self.driver.current_url== url 