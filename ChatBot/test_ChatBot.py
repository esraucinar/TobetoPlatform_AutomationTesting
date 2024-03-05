from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains

from constants import chatBotConstants as c

class Test_ChatBot:
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()
        sleep(3)  
    
    def teardown_method(self): 
           self.driver.quit()  


    def  test_chatBotOpenAndClose(self):
           iframe_element = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,c.ANASAYFA_IFRAME)))
           WebDriverWait(self.driver,10).until(ec.frame_to_be_available_and_switch_to_it(iframe_element)) 
           openChatBot = self.driver.find_element(By.XPATH,c.CHATBOT_IFRAME)
           openChatBot.click()
           sleep(5)
           self.driver.switch_to.default_content()
           second_frame =WebDriverWait(self.driver,30).until(ec.visibility_of_element_located((By.XPATH,c.CHATBOT_SECOND_IFRAME )))
           WebDriverWait(self.driver,15).until(ec.frame_to_be_available_and_switch_to_it(second_frame)) 
           simge_durumu_frame =self.driver.find_element(By.CSS_SELECTOR,c.SIMGE_DURUMU_FRAME)
           simge_durumu_frame.click()
           sleep(3)
           
    def test_chatBotOpenAndEnd(self):

           iframe_element = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH, c.ANASAYFA_IFRAME)))
           WebDriverWait(self.driver,10).until(ec.frame_to_be_available_and_switch_to_it(iframe_element)) 
           openChatBot = self.driver.find_element(By.XPATH,c.CHATBOT_IFRAME)
           openChatBot.click()
           sleep(5)
           self.driver.switch_to.default_content()
           second_frame =WebDriverWait(self.driver,30).until(ec.visibility_of_element_located((By.XPATH,c.CHATBOT_SECOND_IFRAME)))
           WebDriverWait(self.driver,15).until(ec.frame_to_be_available_and_switch_to_it(second_frame))    
           konusmaBitirme=self.driver.find_element(By.CSS_SELECTOR,c.KONUSMA_BITIRME_CSSSELECTOR)
           konusmaBitirme.click()
           simgeDurumuGetirme=self.driver.find_element(By.CSS_SELECTOR,c.SIMGE_DURUMU_CSSSELECTOR)
           simgeDurumuGetirme.click()
           sleep(3)

    def test_chatBotGeriBildirim(self):
         
           iframe_element = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,c.ANASAYFA_IFRAME)))
           WebDriverWait(self.driver,10).until(ec.frame_to_be_available_and_switch_to_it(iframe_element)) 
           openChatBot = self.driver.find_element(By.XPATH,c.CHATBOT_IFRAME)
           openChatBot.click()
           sleep(5)
           self.driver.switch_to.default_content()
           second_frame =WebDriverWait(self.driver,30).until(ec.visibility_of_element_located((By.XPATH,c.CHATBOT_SECOND_IFRAME)))
           WebDriverWait(self.driver,15).until(ec.frame_to_be_available_and_switch_to_it(second_frame))    
           konusmaBitirme=self.driver.find_element(By.CSS_SELECTOR,c.KONUSMA_BITIRME_CSSSELECTOR)
           konusmaBitirme.click()
           simgeDurumuGetirme=self.driver.find_element(By.CSS_SELECTOR,c.SIMGE_DURUMU_CSSSELECTOR)
           simgeDurumuGetirme.click()
           sleep(5)
           self.driver.find_element(By.ID, "emoji5").click()
           sleep(5)
           self.driver.find_element(By.ID, "surveyTextArea").click()
           sleep(3)
           self.driver.find_element(By.ID, "surveyTextArea").send_keys("teşekkürler")
           sleep(5)
           self.driver.find_element(By.ID, "surveyBtn").click() 
           sleep(3)
           self.driver.switch_to.default_content()
           self.driver.close()

    def test_chatBotKontrol(self):
          iframe_element = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,c.ANASAYFA_IFRAME)))
          WebDriverWait(self.driver,10).until(ec.frame_to_be_available_and_switch_to_it(iframe_element)) 
          openChatBot = self.driver.find_element(By.XPATH, c.CHATBOT_IFRAME)
          openChatBot.click()
          sleep(5)
          self.driver.switch_to.default_content()
          second_frame =WebDriverWait(self.driver,20).until(ec.visibility_of_element_located((By.XPATH, c.CHATBOT_SECOND_IFRAME)))
          WebDriverWait(self.driver,15).until(ec.frame_to_be_available_and_switch_to_it(second_frame)) 
          sleep(5)
          messageKey=self.driver.find_element(By.NAME, c.MESSAGE_KEY)
          messageKey.click()
          sleep(3)
          messageName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.MESSAGE_NAME)))
          messageName.send_keys("Elif Acet")
          sleep(3)
          sendKey=self.driver.find_element(By.XPATH,c.SEND_KEY)
          sendKey.click()
          sleep(7)
          tobetoHakkinda=self.driver.find_element(By.CSS_SELECTOR,c.TOBETO_HAKKINDA)
          tobetoHakkinda.click()
          sleep(10)
          egitimlerimiz=self.driver.find_element(By.CSS_SELECTOR,c.EGITIMLERIMIZ)
          egitimlerimiz.click()
          sleep(5)
          hangiEgitimler=self.driver.find_element(By.CSS_SELECTOR,c.HANGI_EGITIMLER)
          hangiEgitimler.click()
          sleep(6)
          self.driver.switch_to.default_content()
          second_frame =WebDriverWait(self.driver,30).until(ec.visibility_of_element_located((By.XPATH,c.CHATBOT_SECOND_IFRAME )))
          WebDriverWait(self.driver,15).until(ec.frame_to_be_available_and_switch_to_it(second_frame)) 
          simge_durumu_frame =self.driver.find_element(By.CSS_SELECTOR,c.SIMGE_DURUMU_FRAME)
          simge_durumu_frame.click()
          sleep(3)
          #self.driver.find_element(By.CSS_SELECTOR, ".exw-reply:nth-child(2)").click()
          #sleep(6)
          #self.driver.find_element(By.CSS_SELECTOR, "#emoji5 > #color > circle").click()
          #sleep(5)
          #self.driver.find_element(By.ID, "surveyBtn").click()
          self.driver.switch_to.default_content()
          self.driver.close()

               
          
          
         
         

       



