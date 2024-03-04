
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
from selenium.webdriver.support.ui import Select
from constants import educationCalendarConstants as e

class Test_educationCalendar():

  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(e.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_educationCalendarAccess(self):
   
    calendar=self.driver.find_element(By.CSS_SELECTOR, e.CALENDAR_CSS)
    calendar.click()
    calendarText=self.driver.find_element(By.XPATH,e.CALENDAR_TEXT_XPATH)
    sleep(3)
    calendarText.is_displayed

  def test_searchEducation(self) :

    Test_educationCalendar.test_educationCalendarAccess(self) 
    searchEducationText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.SEARCH_EDUCATION_XPATH)))
    searchEducationText.send_keys(e.SEARCH_EDUCATION_TEXT)
    qualityAndTest=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.QUALITY_TEST_XPATH)))
    sleep(3)
    allText=qualityAndTest.text
    searchtext=e.SEARCH_EDUCATION_TEXT
    if searchtext in allText:
           print(f"'{searchtext}' kelimesi metinde bulunuyor.")
    else:
        print(f"'{searchtext}' kelimesi metinde bulunmuyor.")

  
  def test_searchInstructor(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    searchInstructorText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,e.INSTRUCTOR_CLASS)))
    searchInstructorText.click()
    textArea=self.driver.find_element(By.CLASS_NAME,"css-1jqq78o-placeholder")
    sleep(3)
    textArea.click()
    textArea.send_keys("irem balcı")
    sleep(4)
    searchInstructorText.send_keys(e.SEARCH_INSTRUCTOR_TEXT)


   
  def test_searchEndLessons(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    searchEducationText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.SEARCH_EDUCATION_XPATH)))
    searchEducationText.send_keys(e.SEARCH_EDUCATION_TEXT)
    endLessons=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.END_LESSONS_XPATH)))
    endLessons.click()
    sleep(3)
    qualityAndTest=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.QUALITY_TEST_XPATH)))
    allText=qualityAndTest.text
    searchtext=e.SEARCH_EDUCATION_TEXT
    if searchtext in allText:
           print(f"'{searchtext}' kelimesi metinde bulunuyor.")
    else:
        print(f"'{searchtext}' kelimesi metinde bulunmuyor.")

  def test_searchContinueLessons(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    searchEducationText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.SEARCH_EDUCATION_XPATH)))
    searchEducationText.send_keys(e.SEARCH_EDUCATION_TEXT)
    continueLessons=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.CONTINUE_LESSONS_XPATH)))
    continueLessons.click()
    sleep(3)
    qualityAndTest=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.QUALITY_TEST_XPATH)))
    allText=qualityAndTest.text
    searchtext=e.SEARCH_EDUCATION_TEXT
    if searchtext in allText:
           print(f"'{searchtext}' kelimesi metinde bulunuyor.")
    else:
        print(f"'{searchtext}' kelimesi metinde bulunmuyor.")

  
  def test_searchBuyLessons(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    searchEducationText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.SEARCH_EDUCATION_XPATH)))
    searchEducationText.send_keys(e.SEARCH_EDUCATION_TEXT)
    buyLessons=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.BUY_LESSONS_XPATH)))
    buyLessons.click()
    sleep(3)
    
  def test_searchNotStartedLessons(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    searchEducationText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.SEARCH_EDUCATION_XPATH)))
    searchEducationText.send_keys(e.SEARCH_EDUCATION_TEXT)
    notStartedLessons=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.NOT_STARTED_LESSONS_XPATH)))
    notStartedLessons.click()
    sleep(3)
    qualityAndTest=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.QUALITY_TEST_XPATH)))
    allText=qualityAndTest.text
    searchtext=e.SEARCH_EDUCATION_TEXT
    if searchtext in allText:
           print(f"'{searchtext}' kelimesi metinde bulunuyor.")
    else:
        print(f"'{searchtext}' kelimesi metinde bulunmuyor.")

  def test_dayWeekMonthLessons(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    searchEducationText= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, e.SEARCH_EDUCATION_XPATH)))
    searchEducationText.send_keys(e.SEARCH_EDUCATION_TEXT)
    month=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.MONTH_XPATH)))
    month.click()
    sleep(3)
    week=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.WEEK_XPATH)))
    week.click()
    sleep(3)
    day=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.DAY_XPATH)))
    day.click()
    sleep(3)

  def test_rightLeftKeys(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    month=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.MONTH_XPATH)))
    month.click()
    sleep(4)
    leftKeys=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.LEFT_KEYS_CLASS)))
    leftKeys.click()
    sleep(4)
    rightKeys=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.RIGHT_KEYS_CLASS)))
    rightKeys.click()
    sleep(4)
    week=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.WEEK_XPATH)))
    week.click()
    sleep(4)
    leftKeys.click()
    sleep(4)
    rightKeys.click()
    sleep(4)
    day=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.DAY_XPATH)))
    day.click()
    sleep(4)
    leftKeys.click()
    sleep(4)
    rightKeys.click()
    sleep(2)

  def test_closeCalendarPage(self) :

    Test_educationCalendar.test_educationCalendarAccess(self)
    closeButton=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,e.CLOSE_BUTTON_XPATH)))
    closeButton.click()
    sleep(5)
    codeAcademy=self.driver.find_element(By.XPATH,e.CODE_ACADEMY_XPATH)
    codeAcademy.is_displayed