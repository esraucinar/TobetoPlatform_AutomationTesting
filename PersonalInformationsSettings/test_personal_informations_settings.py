


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
from constants import personalInformationsConstants as p
from constants import personalInfoSettingsConstants as r



class Test_personalInformationsSettings():
 

 def setup_method(self, method):

  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.driver.get(c.LOGIN_URL)
  self.driver.maximize_window()
  self.vars = {}
  
 def teardown_method(self, method):
    self.driver.quit()
  
 def test_enterPersonalInformationsSettings(self):

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
    sleep(3)
    settingsButton=self.driver.find_element(By.XPATH,r.SETTINGS_BUTTON_XPATH)
    settingsButton.click()
    sleep(2)
    changePasswordText=self.driver.find_element(By.XPATH,r.CHANGE_PASSWORD_TEXT_XPATH)
    changePasswordText.is_displayed

 def test_requiredFields(self):
   
   Test_personalInformationsSettings.test_enterPersonalInformationsSettings(self)
   changePasswordButton=self.driver.find_element(By.CSS_SELECTOR, r.CHANGE_PASSWORD_BUTTON_CSS)
   changePasswordButton.click()
   sleep(2)
   requiredFile=self.driver.find_element(By.XPATH,r.REQUIRED_FILE_XPATH)
   assert  requiredFile.text == r.REQUIRED_FILE_TEXT
   oldPassword=self.driver.find_element(By.NAME,r.OLD_PASSWORD_NAME)
   oldPassword.send_keys(r.OLD_PASSWORD)
   changePasswordButton.click()
   sleep(2)
   newPassword=self.driver.find_element(By.NAME, r.NEW_PASSWORD_NAME)
   newPassword.send_keys(r.NEW_PASSWORD)
   sleep(2)
   changePasswordButton.click()
   confirmPassword=self.driver.find_element(By.NAME,r.CONFIRM_PASSWORD_NAME)
   confirmPassword.send_keys(r.CONFIRM_PASSWORD)
   sleep(2)

 def test_passwordInvalidWarning(self):
   
   Test_personalInformationsSettings.test_enterPersonalInformationsSettings(self)

   oldPassword=self.driver.find_element(By.NAME,r.OLD_PASSWORD_NAME)
   oldPassword.send_keys(r.INVALID_OLD_PASSWORD)
   sleep(1)
   newPassword=self.driver.find_element(By.NAME, r.NEW_PASSWORD_NAME)
   newPassword.send_keys(r.NEW_PASSWORD)
   sleep(1)
   confirmPassword=self.driver.find_element(By.NAME, r.CONFIRM_PASSWORD_NAME)
   confirmPassword.send_keys(r.CONFIRM_PASSWORD)
   sleep(2)
   changePasswordButton=self.driver.find_element(By.CSS_SELECTOR, r.CHANGE_PASSWORD_BUTTON_CSS)
   changePasswordButton.click()
   sleep(2)
   warningmessage=self.driver.find_element(By.XPATH,r.WARNING_MESSAGE_XPATH)

   assert warningmessage.text == r.INVALID_PASSWORD_WARNING


 def test_passwordCharacterWarning(self):
   
   Test_personalInformationsSettings.test_enterPersonalInformationsSettings(self)

   oldPassword=self.driver.find_element(By.NAME,r.OLD_PASSWORD_NAME)
   oldPassword.send_keys(r.OLD_PASSWORD)
   sleep(1)
   newPassword=self.driver.find_element(By.NAME, r.NEW_PASSWORD_NAME)
   newPassword.send_keys(r.CHARACTER_NEW_PASSWORD)
   sleep(1)
   confirmPassword=self.driver.find_element(By.NAME, r.CONFIRM_PASSWORD_NAME)
   confirmPassword.send_keys(r.CHARACTER_NEW_PASSWORD)
   sleep(2)
   changePasswordButton=self.driver.find_element(By.CSS_SELECTOR, r.CHANGE_PASSWORD_BUTTON_CSS)
   changePasswordButton.click()
   sleep(2)
   warningmessage=self.driver.find_element(By.XPATH,r.WARNING_MESSAGE_XPATH)

   assert warningmessage.text == r.CHARACTER_PASSWORD_WARNING

 def test_passwordSameWarning(self):
   
   Test_personalInformationsSettings.test_enterPersonalInformationsSettings(self)

   oldPassword=self.driver.find_element(By.NAME,r.OLD_PASSWORD_NAME)
   oldPassword.send_keys(r.OLD_PASSWORD)
   sleep(1)
   newPassword=self.driver.find_element(By.NAME, r.NEW_PASSWORD_NAME)
   newPassword.send_keys(r.OLD_PASSWORD)
   sleep(1)
   confirmPassword=self.driver.find_element(By.NAME, r.CONFIRM_PASSWORD_NAME)
   confirmPassword.send_keys(r.OLD_PASSWORD)
   sleep(2)
   changePasswordButton=self.driver.find_element(By.CSS_SELECTOR, r.CHANGE_PASSWORD_BUTTON_CSS)
   changePasswordButton.click()
   sleep(2)
   warningmessage=self.driver.find_element(By.XPATH,r.WARNING_MESSAGE_XPATH)

   assert warningmessage.text == r.SAME_PASSWORD_WARNING

 def test_passwordMismatchWarning(self):
   
   Test_personalInformationsSettings.test_enterPersonalInformationsSettings(self)
   
   oldPassword=self.driver.find_element(By.NAME,r.OLD_PASSWORD_NAME)
   oldPassword.send_keys(r.OLD_PASSWORD)
   sleep(1)
   newPassword=self.driver.find_element(By.NAME, r.NEW_PASSWORD_NAME)
   newPassword.send_keys(r.NEW_PASSWORD)
   sleep(1)
   confirmPassword=self.driver.find_element(By.NAME, r.CONFIRM_PASSWORD_NAME)
   confirmPassword.send_keys(r.DIF_NEW_PASSWORD)
   sleep(2)
   changePasswordButton=self.driver.find_element(By.CSS_SELECTOR, r.CHANGE_PASSWORD_BUTTON_CSS)
   changePasswordButton.click()
   sleep(2)
   warningmessage=self.driver.find_element(By.XPATH,r.WARNING_MESSAGE_XPATH)
   

   assert warningmessage.text == r.DIF_NEW_PASSWORD_WARNING

 def test_successChangePasword(self) :
   
   Test_personalInformationsSettings.test_enterPersonalInformationsSettings(self)
   sleep(2)
   oldPassword=self.driver.find_element(By.NAME,r.OLD_PASSWORD_NAME)
   oldPassword.send_keys(r.OLD_PASSWORD)
   sleep(1)
   newPassword=self.driver.find_element(By.NAME, r.NEW_PASSWORD_NAME)
   newPassword.send_keys(r.NEW_PASSWORD)
   sleep(1)
   confirmPassword=self.driver.find_element(By.NAME, r.CONFIRM_PASSWORD_NAME)
   confirmPassword.send_keys(r.NEW_PASSWORD)
   sleep(2)
   changePasswordButton=self.driver.find_element(By.CSS_SELECTOR, r.CHANGE_PASSWORD_BUTTON_CSS)
   changePasswordButton.click()
   sleep(2)
   warningmessage=self.driver.find_element(By.XPATH,r.WARNING_MESSAGE_XPATH)
   assert warningmessage.text == r.SUCCESS_PASSWORD_CHANGE_WARNING
