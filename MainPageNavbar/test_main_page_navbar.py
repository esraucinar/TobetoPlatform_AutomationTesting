
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
from constants import navbarConstants as n
from constants import loginConstants as l

class Test_mainPageNavbar():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(n.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  

  @pytest.mark.parametrize("location, url", [
        (n.MAIN_PAGE_LINKTEXT, n.MAIN_PAGE_URL),
        (n.PROFILE_LINK_TEXT, n.PROFILE_URL),(n.REVIEWS_LINK_TEXT,n.REVIEWS_URL),
        (n.CATALOG_LINK_TEXT,n.CATALOG_URL),(n.CALENDAR_LINK_TEXT,n.CALENDAR_URL),(n.ISTANBUL_CODING_LINK_TEXT,n.ISTANBUL_CODING_URL)])
  
  def test_navBar(self,location,url):

   emailTextBox= self.driver.find_element(By.XPATH,l.EPOSTA_TEXT_BOX_XPATH)
   emailTextBox.send_keys(l.VALID_EPOSTA)
   passwordTextBox=self.driver.find_element(By.XPATH, l.PASSWORD_TEXT_BOX_XPATH)
   passwordTextBox.send_keys(l.VALID_PASSWORD)
   loginButton=self.driver.find_element(By.XPATH, l.LOGIN_BUTTON_XPATH)
   loginButton.click()
   sleep(3)
   mainPage=self.driver.find_element(By.LINK_TEXT, location)
   mainPage.click()
   assert self.driver.current_url==url

  def test_profileSummary(self):

   emailTextBox= self.driver.find_element(By.XPATH,l.EPOSTA_TEXT_BOX_XPATH)
   emailTextBox.send_keys(l.VALID_EPOSTA)
   passwordTextBox=self.driver.find_element(By.XPATH, l.PASSWORD_TEXT_BOX_XPATH)
   passwordTextBox.send_keys(l.VALID_PASSWORD)
   loginButton=self.driver.find_element(By.XPATH, l.LOGIN_BUTTON_XPATH)
   loginButton.click()
   sleep(10)
   profileSummary=self.driver.find_element(By.CSS_SELECTOR, n.PROFILE_SUMMARY_CSS)
   profileSummary.click()
   profileInfo=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,n.PROFILE_INFO_XPATH)))
   sleep(3)
   profileInfo.is_displayed