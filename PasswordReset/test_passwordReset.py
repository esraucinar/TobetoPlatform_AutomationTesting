from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gC
from selenium.common.exceptions import TimeoutException
import openpyxl
import pytest
import time

class Test_tobeto_sifreyenileme():
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get(gC.URL)
        self.driver.maximize_window()
    
    def teardown_method(self): 
        self.driver.quit()
    
    #kayıtlı olmayan email ile şifre yenileme
    def test_sifremi_unuttum(self):
        sifremiunuttum = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, gC.PASSWORD_RESET)))
        sifremiunuttum.click()
        sleep(3)

        epostaAlanı= WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH, gC.EMAİL_SECTION)))
        epostaAlanı.send_keys("deneme@hotmail.com")
        sleep(3)

        emailclick= WebDriverWait(self.driver,10).until(ec.element_to_be_clickable((By.XPATH, gC.EMAİL_CLİCK)))
        emailclick=emailclick.click()
        sleep(3)

        toast_message = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gC.PASSWORD_RESET_MESSAGE)))
        assert toast_message.text=="• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."

    #kayıtlı email ile şifre yenileme
    def test_sifremi_unuttum1(self):
        sifremiunuttum = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, gC.PASSWORD_RESET)))
        sifremiunuttum.click()
        sleep(3)

        epostaAlanı= WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,gC.EMAİL_SECTION)))
        epostaAlanı.send_keys("96wyssplag@rfcdrive.com")
        sleep(5)

        emailclick= WebDriverWait(self.driver,10).until(ec.element_to_be_clickable((By.XPATH, gC.EMAİL_CLİCK)))
        emailclick=emailclick.click()
        sleep(5)

        toast_message = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gC.PASSWORD_RESET_MESSAGE)))
        assert toast_message.text=="• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."

    #geçersiz e-posta ile şifre yenileme
    def test_sifremi_unuttum2(self):
        sifremiunuttum = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, gC.PASSWORD_RESET)))
        sifremiunuttum.click()
        sleep(3)

        epostaAlanı= WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH, gC.EMAİL_SECTION)))
        epostaAlanı.send_keys("a")
        sleep(3)

        emailclick= WebDriverWait(self.driver,10).until(ec.element_to_be_clickable((By.XPATH, gC.EMAİL_CLİCK)))
        emailclick=emailclick.click()
        sleep(3)

        toast_message = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,gC.INVALİD_EMAİL ))) 
        assert toast_message.text=="• Girdiğiniz e-posta geçersizdir."


        



    