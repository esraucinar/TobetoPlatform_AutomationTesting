import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import elifLoginConstants as c
from time import sleep

class TestAsencronEducation:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown_method(self, method):
        self.driver.quit()

    def test_asencron_education(self):
        self.driver.get(c.LOGIN_URL)
        sleep(5)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()


       # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.LESSONS_TAB))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.EDUCATION))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.LESSONTITLE))).click()

        lock = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.LOCK)))
        actions = ActionChains(self.driver)
        actions.move_to_element(lock).perform()

        time_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.TIME)))
        assert time_text.text == "Eğitim bitiş tarihi geçmiştir."

    def test_asencron_education2(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.LESSONS_TAB))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.SHOWMOREBTN))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.APPLYBTN))).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.CIRCLE))).click()

        infoText = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.TOOLTIP)))
        assert infoText.is_displayed()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.SPAN))).click()
        aboutYouText = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.COLL)))
        assert aboutYouText.text == "Geçirdiğin Süre"

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.TABS))).click()

        playVideoButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.PLAY)))
        playVideoButton.click()
        
        #Eğitim Başlığı Hizasında Kullanıcı Bilgilerinin Gösterimi
    def test_user_info_display(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        self.driver.get("https://tobeto.com/platform")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Eğitimlerim"))).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.COURSE_TITLE_XPATH)))
        user_info = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.USER_INFO_XPATH)))

        assert user_info.find_element_by_xpath("./div[1]").get_attribute("class") == "points"
        assert user_info.find_element_by_xpath("./div[2]").get_attribute("class") == "like-icon"
        assert user_info.find_element_by_xpath("./div[3]").get_attribute("class") == "like-count"
        assert user_info.find_element_by_xpath("./div[4]").get_attribute("class") == "favorite-icon"

     #Beğeni ve Favori Butonlarının İşlevselliği
    def test_like_button(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        self.driver.get("https://tobeto.com/platform")
        egitimlerim_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.EGITIMLERIM_LINK)))
        egitimlerim_link.click()

        egitime_git_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.EGITIME_GIT_BUTTON)))
        egitime_git_button.click()

        begeni_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.BEGENI_BUTTON)))
        begeni_button.click()

        pop_up_title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.POP_UP_TITLE)))
        assert pop_up_title.text == "Beğenenler"

        users_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, c.USERS_LIST)))
        assert len(users_list) <= 10

        close_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.CLOSE_BUTTON)))
        close_button.click()


     #Kullanıcı Profilini Takip Etme ve Takibi Bırakma 
    def test_follow_unfollow_user(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        self.driver.get("https://tobeto.com/platform")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Eğitimlerim"))).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.USER_TO_FOLLOW_XPATH))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.FOLLOW_BUTTON_XPATH))).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, c.FOLLOW_BUTTON_XPATH)))

        self.driver.back()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.USER_TO_FOLLOW_XPATH))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.UNFOLLOW_BUTTON_XPATH))).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, c.UNFOLLOW_BUTTON_XPATH)))
        assert True

     #:Eğitimi Favorilere Ekleme Kontrolü
    def test_add_remove_favorite(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        self.driver.get("https://tobeto.com/platform")
        my_trainings_button = self.driver.find_element(By.XPATH, c.MY_TRAININGS_BUTTON)
        my_trainings_button.click()

        training_image = self.driver.find_element(By.XPATH, c.TRAINING_IMAGE)
        assert training_image.is_displayed()

        go_to_training_button = self.driver.find_element(By.XPATH, c.GO_TO_TRAINING_BUTTON)
        go_to_training_button.click()

        add_to_favorites_button = self.driver.find_element(By.XPATH, c.ADD_TO_FAVORITES_BUTTON)
        add_to_favorites_button.click()

        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.SUCCESS_MESSAGE)))
        assert success_message.text == "Favorilere ekleme işlemi başarılı bir şekilde gerçekleştirildi"
        time.sleep(2)

        add_to_favorites_button.click()

        remove_success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.SUCCESS_MESSAGE)))
        assert remove_success_message.text == "Favorilerinden çıkarma işlemi başarıyla gerçekleştirildi."

        close_button = self.driver.find_element(By.XPATH, c.CLOSE_BUTTON)
        close_button.click()

    def test_completion_of_training(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        self.driver.get("https://tobeto.com/platform")
        my_trainings_link = self.driver.find_element(By.XPATH, c.MY_TRAININGS_LINK)
        my_trainings_link.click()

        assert self.driver.find_element(By.XPATH, c.COURSE_INFO_XPATH).is_displayed()

        go_to_training_button = self.driver.find_element(By.XPATH, c.GO_TO_TRAINING_BUTTON)
        go_to_training_button.click()

        progress_bar = self.driver.find_element(By.XPATH, c.PROGRESS_BAR)
        assert progress_bar.is_displayed()

        completion_percentage = self.driver.find_element(By.XPATH, c.COMPLETION_PERCENTAGE)
        assert "%" in completion_percentage.text

        webdriver.ActionChains(self.driver).move_to_element(progress_bar).perform()
        assert "Training Completion Rate" in self.driver.page_source

    def test_detay_button_popup(self):
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()

        self.driver.get("https://tobeto.com/platform")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.LESSONS_TAB))).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, c.DETAIL_POP_UP))).click()

        time.sleep(2) 
