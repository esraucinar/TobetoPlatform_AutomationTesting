import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from competenciesConstans import c  


class TestMyCompetencies:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(c.LOGIN_URL)
        self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH).send_keys(c.VALID_EPOSTA)
        self.driver.find_element(By.XPATH, c.PASSWORD_TEXT_BOX_XPATH).send_keys(c.VALID_PASSWORD)
        self.driver.find_element(By.XPATH, c.LOGIN_BUTTON_XPATH).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.PROFILE_LINK_XPATH)))  

    def teardown_method(self, method):
        self.driver.quit()

    def test_competencies(self):
        self.driver.get("https://tobeto.com/platform")
        assert "Tobeto" in self.driver.title  
        
        egitimlerim_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.EGITIMLERIM_LINK_XPATH)))
        egitimlerim_link.click()
        
        lesson_title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.LESSONTITLE_XPATH)))
        assert lesson_title.text == "Seçiniz"
        
        arama_input = self.driver.find_element(By.XPATH, c.ARAMA_INPUT_XPATH)
        arama_input.send_keys("Python")
        arama_input.send_keys(Keys.ENTER)
        assert True

    def test_background_color_change(self):
        self.driver.get("https://tobeto.com/platform")
        profilim_button = self.driver.find_element(By.XPATH, c.PROFILIM_BUTTON_XPATH)
        profilim_button.click()
        
        yetkinlik_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.YETKINLIK_BUTTON_XPATH)))
        yetkinlik_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.ADDITIONAL_ELEMENT_XPATH)))
        self.driver.find_element(By.XPATH, c.BUTTON_XPATH).click()

    def test_add_skill(self):
        self.driver.get("https://tobeto.com/platform")
        profile_link = self.driver.find_element(By.XPATH, c.PROFILE_LINK_XPATH)
        profile_link.click()
        
        skill_heading = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.SKILL_HEADING_XPATH)))
        skill_heading.click()
        
        skill_input = self.driver.find_element(By.XPATH, c.SKILL_INPUT_XPATH)
        skill_input.send_keys("Yeni Yetkinlik")
        
        create_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.CREATE_OPTION_XPATH)))
        assert create_option.is_displayed(), "Create 'Yetkinlik Adı' seçeneği görüntülenemedi"

    def test_yetenek_ekle(self):
        self.test_add_skill()  # Reusing the logic from test_add_skill
        
        kaydet_button = self.driver.find_element(By.XPATH, c.KAYDET_BUTTON_XPATH)
        kaydet_button.click()
        
        close_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.CLOSE_ICON_XPATH)))
        close_icon.click()
        
        assert not WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.PROFILE_LINK_XPATH))).is_displayed()

    def test_remove_skill(self):
        self.test_add_skill()  # Reusing the logic from test_add_skill
        
        profile_link = self.driver.find_element(By.XPATH, c.PROFILE_LINK_XPATH)
        profile_link.click()
        
        skill_heading = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.SKILL_HEADING_XPATH)))
        skill_heading.click()
        
        trash_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.TRASH_ICON_XPATH)))
        trash_icon.click()
        
        confirmation_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.CONFIRMATION_MESSAGE_XPATH)))
        assert confirmation_message.text == "Seçilen yetkinliği silmek istediğinize emin misiniz?"
        
        assert WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.CONFIRMATION_MESSAGE_XPATH_2))).text == "Daha sonra tekrardan listeden istediğiniz yetkinliği ekleyebilirsiniz."
        
        yes_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, c.YES_BUTTON_XPATH)))
        assert yes_button.text == "Evet"
        assert yes_button.is_displayed()
        
        yes_button.click()
