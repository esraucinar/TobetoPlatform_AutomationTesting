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

class Test_personalInformations():

  
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(c.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  

  def enterPersonalInformation(self):

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
  
  
  def test_profilePictureIcon(self):

      
    Test_personalInformations.enterPersonalInformation(self)
    photoEditIcon=self.driver.find_element(By.CSS_SELECTOR,p.PHOTO_EDIT_ICON_CSS)
    photoEditIcon.click()
    sleep(3)
    searchButton=self.driver.find_element(By.CSS_SELECTOR,p.SEARCH_BUTTON_CSS)
    assert searchButton.text == p.SEARCH_BUTTON_TEXT
    searchButton.click()
    sleep(3)
    closeButton=self.driver.find_element(By.XPATH,p.CLOSE_BUTTON_XPATH)
    closeButton.click()

    
  def test_removeProfilePicture(self):

      
    Test_personalInformations.enterPersonalInformation(self)

    photoEditIcon=self.driver.find_element(By.CSS_SELECTOR,p.PHOTO_EDIT_ICON_CSS)
    photoEditIcon.click()
    sleep(3)
    upload=self.driver.find_element(By.XPATH,p.UPLOAD_XPATH)
    photoPath = r"C:/Users/tahir/OneDrive/Masaüstü/tahir resim/akll.png"
    upload.send_keys(photoPath)
    sleep(5)
    removeFile=self.driver.find_element(By.XPATH,p.REMOVE_FILE_XPATH)
    
    title_value = removeFile.get_attribute("title")

    expected_value = p.EXPECTED_VALUE

    if title_value == expected_value:
      print(p.TITLE_TEXT_POSITIVE)
    else:
        print(p.TITLE_TEXT_NEGATIVE)

    removeFile.click()

    sleep(2)

  

  def test_successUploadProfilePicture(self):

    Test_personalInformations.enterPersonalInformation(self)
    photoEditIcon=self.driver.find_element(By.CSS_SELECTOR,p.PHOTO_EDIT_ICON_CSS)
    photoEditIcon.click()
    sleep(3)
    upload=self.driver.find_element(By.XPATH,p.UPLOAD_XPATH)
    photoPath = r"C:/Users/tahir/OneDrive/Masaüstü/tahir resim/akll.png"
    upload.send_keys(photoPath)
    sleep(3)
    uploadFileButton=self.driver.find_element(By.XPATH,p.UPLOAD_FILE_BUTTON_XPATH)
    uploadFileButton.click()
    sleep(2)
    dustbin=self.driver.find_element(By.CSS_SELECTOR,p.DUSTBIN_CSS)
    dustbin.is_displayed
    sleep(3)


  def test_editProfilePicture(self):

    Test_personalInformations.test_successUploadProfilePicture(self)
    dustbin=self.driver.find_element(By.CSS_SELECTOR,p.DUSTBIN_CSS)
    dustbin.click()
    sleep(2)
    noButton=self.driver.find_element(By.XPATH,p.NO_BUTTON_XPATH)
    noButton.click()
    sleep(3)
    photoEditIcon=self.driver.find_element(By.CSS_SELECTOR,p.PHOTO_EDIT_ICON_CSS)
    photoEditIcon.is_displayed
    dustbin.click()
    sleep(2)
    yesButton=self.driver.find_element(By.XPATH,p.YES_BUTTON_XPATH)
    yesButton.click()
    sleep(3)
    warningMessage=self.driver.find_element(By.CSS_SELECTOR,p.WARNING_MESSAGE_CSS)
    assert warningMessage.text== p.WARNING_MESSAGE_TEXT
    sleep(3)
    
  

  def test_editNameSurname(self):
   
   Test_personalInformations.enterPersonalInformation(self)
   nameBox=self.driver.find_element(By.NAME, p.NAME_BOX_NAME)
   nameBox.clear()
   nameBox.send_keys(p.NAME)
   sleep(3)
   surnameBox=self.driver.find_element(By.XPATH, p.SURNAME_BOX_XPATH)
   surnameBox.clear
   surnameBox.send_keys(p.SURNAME)
   sleep(3)

  
  def test_editPhoneNumber(self):
   
   Test_personalInformations.enterPersonalInformation(self)

   countryIcon= self.driver.find_element(By.NAME,p.COUNTRY_ICON_NAME)
   select=Select(countryIcon)
   select.select_by_visible_text(p.COUNTRY_VISIBLE_TEXT)
   sleep(3)
   phoneNumber= self.driver.find_element(By.ID, p.PHONE_NUMBER_ID)
   phoneNumber.send_keys(p.PHONE_NUMBER)

  
  def test_editBirthDate(self):
   Test_personalInformations.enterPersonalInformation(self)

   birthdate=self.driver.find_element(By.NAME, p.BIRTHDATE_NAME)
   birthdate.clear()
   sleep(2)
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   sleep(5)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   sleep(2)
   requiredFile=self.driver.find_element(By.XPATH,p.REQUIRED_FILE_XPATH)
   assert requiredFile.text == p.REQUIRED_TEXT
   sleep(2)
   birthdate.send_keys(p.BIRTHDATE)
   sleep(2)
  
  
  def test_editIdentifier(self):
   
   Test_personalInformations.enterPersonalInformation(self)

   identifier=self.driver.find_element(By.NAME,p.IDENTIFIER_NAME)
   identifier.clear()
   identifier.send_keys(p.LESS_IDENTIFIER)
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   sleep(3)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   self.driver.execute_script(p.SCRIPT_LOCATION2) 
   requiredFields=self.driver.find_element(By.XPATH,p.REQUIRED_FIELDS_XPATH)
   assert requiredFields.text == p.LESS_IDENTIFIER_TEXT
   identifier.clear()
   sleep(2) 
   identifier.send_keys(p.MORE_IDENTIFIER)
   requiredFieldsMore=self.driver.find_element(By.XPATH,p.MORE_IDENTIFIER_REQUIRED)
   assert requiredFieldsMore.text == p.MORE_IDENTIFIER_TEXT  
   sleep(2)
   identifier.clear() 
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   sleep(3)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   self.driver.execute_script(p.SCRIPT_LOCATION2) 
   requiredFields=self.driver.find_element(By.XPATH,p.REQUIRED_FIELDS_XPATH)
   assert requiredFields.text == p.REQUIRED_FIELDS_TEXT
   identifier.send_keys(p.VALID_IDENTIFIER)
   sleep(5)
    


  def test_editCountry(self):
   
   Test_personalInformations.enterPersonalInformation(self)
   country= self.driver.find_element(By.NAME, p.COUNTRY_NAME)
   country.clear()
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   sleep(3)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   self.driver.execute_script(p.SCRIPT_LOCATION3) 
   sleep(2)
   requiredFile=self.driver.find_element(By.XPATH,p.REQUIRED_FILE_XPATH)
   assert requiredFile.text == p.REQUIRED_TEXT
   sleep(1)
   country.send_keys(p.LESS_COUNTRY_NAME)
   requiredFile=self.driver.find_element(By.CSS_SELECTOR,p.REQUIRED_FIELDS_COUNTRY_CSS)
   assert requiredFile.text == p.LESS_COUNTRY_TEXT
   sleep(3)
   country.clear()
   sleep(1)
   country.send_keys(p.MORE_COUNTRY_NAME)
   requiredFile=self.driver.find_element(By.CSS_SELECTOR,p.REQUIRED_FIELDS_COUNTRY_CSS)
   assert requiredFile.text == p.MORE_COUNTRY_TEXT
   sleep(2)
   country.clear()
   country.send_keys(p.VALID_COUNTRY)
   


  def test_editCityAndDistrict(self):
   
   Test_personalInformations.enterPersonalInformation(self)
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   city=self.driver.find_element(By.NAME,p.CITY_NAME)
   select=Select(city)
   select.select_by_visible_text(p.CHOOSE_CITY_TEXT)
   sleep(1)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   requiredFieldsCity=self.driver.find_element(By.CSS_SELECTOR,p.REQUIRED_FIELDS_CITY_CSS)
   assert requiredFieldsCity.text == p.REQUIRED_TEXT
   requiredFieldsDistrict=self.driver.find_element(By.CSS_SELECTOR,p.REQUIRED_FIELDS_DISTRICT_CSS)
   assert requiredFieldsDistrict.text == p.REQUIRED_TEXT
   sleep(2)
   select=Select(city)
   select.select_by_visible_text(p.VALID_CITY_TEXT)
   sleep(2)
   district=self.driver.find_element(By.NAME,p.DISTRICT_NAME)
   select=Select(district)
   select.select_by_visible_text(p.VALID_DISTRICT_TEXT)
   sleep(2)


  def test_editNeighbourhood(self):
   
   Test_personalInformations.enterPersonalInformation(self)
   self.driver.execute_script(p.SCRIPT_LOCATION)
   sleep(3) 
   neighbourhood=self.driver.find_element(By.NAME, p.NEIGHBOURHOOD_NAME)
   neighbourhood.clear()
   sleep(1)
   neighbourhood.send_keys(p.INVALID_NEIGHBOURHOOD)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   sleep(2)
   warningMessage=self.driver.find_element(By.CSS_SELECTOR, p.REQUIRED_FIELDS_NEIGHBOURHOOD_CSS)
   assert warningMessage.text == p.REQUIRED_FIELDS_NEIGHBOURHOOD_TEXT
   sleep(2)
   neighbourhood.clear()
   neighbourhood.send_keys(p.VALID_NEIGHBOURHOOD)
   sleep(1)


  def test_editAboutMe(self):
   
   Test_personalInformations.enterPersonalInformation(self)
   self.driver.execute_script(p.SCRIPT_LOCATION) 
   sleep(2)
   aboutMe=self.driver.find_element(By.CSS_SELECTOR,p.ABOUT_ME_CSS)
   aboutMe.clear()
   sleep(3)
   aboutMe.send_keys(p.INVALID_ABOUT_ME)
   sleep(1)
   recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
   recordButton.click()
   warningMessage=self.driver.find_element(By.CSS_SELECTOR, p.REQUIRED_FIELDS_ABOUT_CSS)
   assert warningMessage.text == p.REQUIRED_FIELDS_ABOUT_TEXT
   sleep(1)
   aboutMe.clear()
   sleep(1)
   aboutMe.send_keys(p.VALID_ABOUT_ME)
   sleep(2)



  def test_successUpdatePersonalInformations(self):
     
    Test_personalInformations.enterPersonalInformation(self)
    photoEditIcon=self.driver.find_element(By.CSS_SELECTOR,p.PHOTO_EDIT_ICON_CSS)
    photoEditIcon.click()
    sleep(2)
    upload=self.driver.find_element(By.XPATH,p.UPLOAD_XPATH)
    photoPath = r"C:/Users/tahir/OneDrive/Masaüstü/tahir resim/akll.png"
    upload.send_keys(photoPath)
    sleep(3)
    uploadFileButton=self.driver.find_element(By.XPATH,p.UPLOAD_FILE_BUTTON_XPATH)
    uploadFileButton.click()
    sleep(2)
    nameBox=self.driver.find_element(By.NAME, p.NAME_BOX_NAME)
    nameBox.clear()
    nameBox.send_keys(p.NAME)
    sleep(2)
    countryIcon= self.driver.find_element(By.NAME,p.COUNTRY_ICON_NAME)
    select=Select(countryIcon)
    select.select_by_visible_text(p.COUNTRY_VISIBLE_TEXT)
    sleep(2)
    phoneNumber= self.driver.find_element(By.ID, p.PHONE_NUMBER_ID)
    phoneNumber.send_keys(p.PHONE_NUMBER)
    sleep(2)
    birthdate=self.driver.find_element(By.NAME, p.BIRTHDATE_NAME)
    birthdate.clear()
    birthdate.send_keys(p.BIRTHDATE)
    sleep(2)
    identifier=self.driver.find_element(By.NAME,p.IDENTIFIER_NAME)
    identifier.clear()
    identifier.send_keys(p.VALID_IDENTIFIER)
    sleep(2)
    self.driver.execute_script(p.SCRIPT_LOCATION4) 
    city=self.driver.find_element(By.NAME,p.CITY_NAME)
    select=Select(city)
    select.select_by_visible_text(p.VALID_CITY_TEXT)
    sleep(2)
    district=self.driver.find_element(By.NAME,p.DISTRICT_NAME)
    select=Select(district)
    select.select_by_visible_text(p.VALID_DISTRICT_TEXT)
    sleep(2)
    neighbourhood=self.driver.find_element(By.NAME, p.NEIGHBOURHOOD_NAME)
    neighbourhood.clear()
    neighbourhood.send_keys(p.VALID_NEIGHBOURHOOD)
    sleep(2)
    aboutMe=self.driver.find_element(By.CSS_SELECTOR,p.ABOUT_ME_CSS)
    aboutMe.clear()
    aboutMe.send_keys(p.VALID_ABOUT_ME)
    recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
    recordButton.click()
    sleep(2)
    successWarningMessage=self.driver.find_element(By.CSS_SELECTOR,p.WARNING_MESSAGE_CSS)
    assert successWarningMessage.text == p.SUCCESS_WARNING_MESSAGE



  def test_unsuccessUpdatePersonalInformations(self):
     
    Test_personalInformations.enterPersonalInformation(self)
    photoEditIcon=self.driver.find_element(By.CSS_SELECTOR,p.PHOTO_EDIT_ICON_CSS)
    photoEditIcon.click()
    sleep(2)
    upload=self.driver.find_element(By.XPATH,p.UPLOAD_XPATH)
    photoPath = r"C:/Users/tahir/OneDrive/Masaüstü/tahir resim/akll.png"
    upload.send_keys(photoPath)
    sleep(2)
    uploadFileButton=self.driver.find_element(By.XPATH,p.UPLOAD_FILE_BUTTON_XPATH)
    uploadFileButton.click()
    sleep(2)
    nameBox=self.driver.find_element(By.NAME, p.NAME_BOX_NAME)
    nameBox.clear()
    nameBox.send_keys(p.VALID_NAME)
    sleep(2)
    countryIcon= self.driver.find_element(By.NAME,p.COUNTRY_ICON_NAME)
    select=Select(countryIcon)
    select.select_by_visible_text(p.COUNTRY_VISIBLE_TEXT)
    sleep(2)
    phoneNumber= self.driver.find_element(By.ID, p.PHONE_NUMBER_ID)
    phoneNumber.send_keys(p.PHONE_NUMBER)
    sleep(2)
    birthdate=self.driver.find_element(By.NAME, p.BIRTHDATE_NAME)
    birthdate.clear()
    birthdate.send_keys(p.BIRTHDATE)
    sleep(2)
    identifier=self.driver.find_element(By.NAME,p.IDENTIFIER_NAME)
    identifier.clear()
    identifier.send_keys(p.VALID_IDENTIFIER)
    sleep(2)
    self.driver.execute_script(p.SCRIPT_LOCATION4) 
    city=self.driver.find_element(By.NAME,p.CITY_NAME)
    select=Select(city)
    select.select_by_visible_text(p.VALID_CITY_TEXT)
    sleep(2)
    district=self.driver.find_element(By.NAME,p.DISTRICT_NAME)
    select=Select(district)
    select.select_by_visible_text(p.VALID_DISTRICT_TEXT)
    sleep(2)
    neighbourhood=self.driver.find_element(By.NAME, p.NEIGHBOURHOOD_NAME)
    neighbourhood.clear()
    neighbourhood.send_keys(p.VALID_NEIGHBOURHOOD)
    sleep(2)
    aboutMe=self.driver.find_element(By.CSS_SELECTOR,p.ABOUT_ME_CSS)
    aboutMe.clear()
    aboutMe.send_keys(p.VALID_ABOUT_ME)
    recordButton=self.driver.find_element(By.XPATH,p.RECORD_BUTTON_XPATH)
    recordButton.click()
    sleep(2)
    successWarningMessage=self.driver.find_element(By.CSS_SELECTOR,p.WARNING_MESSAGE_CSS)
    assert successWarningMessage.text == p.UNSUCCESS_WARNING_MESSAGE