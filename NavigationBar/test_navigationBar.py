from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gC
import openpyxl
import pytest

class Test_NavigationBar():
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get(gC.URL_BASIC)
        self.driver.maximize_window()
    
    def teardown_method(self): 
        self.driver.quit()
#TEST CASE 1: Reklam Panosundaki “Başvur” Butonunun İşlevselliği
    def test_apply_button_on_billboard(self):
        apply_button= WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,gC.APPLYBUTTON)))
        apply_button.click()
        sleep(2)
        istanbul_kodluyor = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,gC.ISTANBUL_KODLUYOR)))
        assert istanbul_kodluyor.text == "Ücretsiz eğitimlerle, geleceğin mesleklerinde sen de yerini al."
#TEST CASE 2: Gezinme Çubuğundaki “Giriş Yap” Butonunun İşlevselliği
    def test_loginButton_navigationBar(self):
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,gC.LOGINBUTTON)))
        loginButton.click()
        sleep(2)
        emailinput = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, gC.name)))
        emailinput.click()
        sleep(2)
#TEST CASE 3: Gezinme Çubuğundaki “Ücretsiz Üye Ol” Butonunun İşlevselliği
    def test_free_sign_in(self):
        free = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.LINK_TEXT,"Ücretsiz Üye Ol")))
        free.click()
        sleep(2)
        kayıt_ol = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, gC.SIGNBUTTON)))
        assert kayıt_ol.text == "Hemen Kayıt Ol"

