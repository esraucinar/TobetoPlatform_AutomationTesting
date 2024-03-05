from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest
from buttonConstans import *


class TestButton:
   
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window()
        self.successful_login()

    def teardown_method(self):
        self.driver.quit()

    def successful_login(self):
        email_input = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, EMAIL_TEXT_BOX_XPATH)))
        email_input.send_keys(VALID_EMAIL)
        password_input = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, PASSWORD_TEXT_BOX_XPATH)))
        password_input.send_keys(VALID_PASSWORD)
        login_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, LOGIN_BUTTON_XPATH)))
        login_button.click()
        system_message = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, LOGIN_SUCCESS_MESSAGE_XPATH)))
        assert system_message.text == "• Giriş başarılı."

    def test_notification_panel(self):
       
        sleep(2)
        notification_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, NOTIFICATION_TAB_XPATH)))
        notification_button.click()
        show_more_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, SHOW_MORE_BUTTON_XPATH)))
        show_more_button.click()
        notification_panel = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, NOTIFICATION_PANEL_XPATH)))
        assert "Duyurularım" in notification_panel.text

