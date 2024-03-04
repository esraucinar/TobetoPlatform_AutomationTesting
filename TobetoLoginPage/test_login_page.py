
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
from constants  import loginPageConstants as l

class Test_loginPage():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(l.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()


  @pytest.mark.parametrize("location, url", [
        (l.ABOUT_LINKTEXT, l.ABOUT_URL),
        (l.FOR_PERSONS_LINK_TEXT, l.FOR_PERSONS_URL),(l.FOR_CORPORATE_LINKTEXT,l.FOR_CORPORATE_URL),
        (l.CORPORATE_ID_LINKTEXT,l.CORPORATE_ID_URL),(l.SSS_LINK_TEXT,l.SSS_URL),(l.COMMUNICATION_LINK_TEXT,l.COMMUNICATION_URL)])
  
  def test_siteMap(self, location, url):
        
        self.driver.execute_script(l.LOCATION)
        aboutLink = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT, location)))
        aboutLink.click()
        sleep(3)
        assert self.driver.current_url == url

  
  @pytest.mark.parametrize("location, url", [
        (l.MEMBERSHIP_AGGREEMENT_LINK_TEXT, l.MEMBERSHIP_AGGREEMENT_URL),(l.KVKK_TEXT_LINK_TEXT,l.KVKK_TEXT_URL),
        (l.APP_FORM_LINK_TEXT,l.APP_FORM_URL),(l.COOKIE_POLICY_LINK_TEXT,l.COOKIE_POLICY_URL),(l.WITHDRAWAL_FORM_LINK_TEXT,l.WITHDRAWAL_FORM_URL)])

  def test_resources(self, location, url):
        
      self.driver.execute_script(l.LOCATION)

      aboutLink = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT, location)))
      aboutLink.click()
      sleep(3)
      window_handles = self.driver.window_handles
      current_window = self.driver.current_window_handle
      new_window = [window for window in window_handles if window != current_window][0]
      self.driver.switch_to.window(new_window)
      sleep(3)
      assert self.driver.current_url == url
   
  
  
  @pytest.mark.parametrize("index,url", [ (12,l.FRONT_END_URL),(13,l.FULL_STACK_URL),(14,l.WEB_MOBILE_URL),
                                         (15,l.DATA_SCIENCE_URL),(16,l.CYBER_SECURITY_URL),(17,l.UI_UX_URL)])

  def test_educational_journeys(self,index,url):

    self.driver.execute_script(l.LOCATION)
    xpath_expression = f"(//a[@class='small text-white text-decoration-none'])[{index}]"
    aboutLink = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_expression)))
    aboutLink.click()
    sleep(3)
    assert self.driver.current_url == url


  

 
  @pytest.mark.parametrize ("index,url", [( 18,l.WEB_API_URL),(19,l.ART_INTELLIGENCE_URL),(20,l.TEST_AUTOMATION_URL),
                                         (21,l.NODE_URL),(22,l.PROGRAMMING_URL)])

  def test_blog(self,index,url):

    self.driver.execute_script(l.LOCATION)
    xpath_expression = f"(//a[@class='small text-white text-decoration-none'])[{index}]"
    aboutLink = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_expression)))
    aboutLink.click()
    sleep(3)
    assert self.driver.current_url == url