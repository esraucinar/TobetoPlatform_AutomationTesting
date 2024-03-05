import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import certificateConstants as c

class TestCertificates:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(c.LOGIN_URL)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.parametrize("dosya_boyutu", [5, 6])
    def test_certificate_upload(self, dosya_boyutu):
        profilim_link = self.driver.find_element(By.XPATH, c.PROFILIM_LINK_XPATH)
        profilim_link.click()
        sertifikalarim_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, c.SERTIFIKALARIM_LINK_XPATH)))
        sertifikalarim_link.click()

        popup_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, c.POPUP_BUTTON_XPATH)))
        popup_button.click()
        
        if dosya_boyutu <= c.MAX_FILE_SIZE_MB:
            yukle_button = self.driver.find_element(By.XPATH, c.CERTIFICATE_BOX_XPATH)
            yukle_button.click()
        else:
            uyarı_mesajı = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "/div/p")))
            assert uyarı_mesajı.text == "Dosya boyutu 5 MB'dan büyük. Lütfen daha küçük bir dosya seçin."

    def test_certificate_page_navigation(self):
        profilim_link = self.driver.find_element(By.XPATH, c.PROFILIM_LINK_XPATH)
        profilim_link.click()
        time.sleep(2)
        yetkinliklerim_bolumu = self.driver.find_element(By.XPATH, c.SERTIFIKALARIM_LINK_XPATH)
        yetkinliklerim_bolumu.click()
        time.sleep(2)
        sertifika_kutusu = self.driver.find_element(By.XPATH, c.CERTIFICATE_BOX_XPATH)
        assert sertifika_kutusu.is_displayed()
        sertifika_listesi = self.driver.find_elements(By.XPATH, c.CERTIFICATE_LIST_XPATH)
        assert len(sertifika_listesi) <= 7
        if len(sertifika_listesi) > 7:
            sag_ok = self.driver.find_element(By.XPATH, c.SAG_OK_XPATH)
            sag_ok.click()
            time.sleep(2)
            assert sag_ok.value_of_css_property("background-color") == "rgba(0, 0, 0, 1)"
            sol_ok = self.driver.find_element(By.XPATH, c.SOL_OK_XPATH)
            sol_ok.click()
            time.sleep(2)
            assert sol_ok.value_of_css_property("background-color") == "rgba(0, 0, 0, 1)"

    def test_menu_items(self):
        wait = WebDriverWait(self.driver, 10)
        menu_item_xpaths = [
            "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[2]/ul/li[1]/button",
            "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[2]/ul/li[2]/button",
            "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[2]/ul/li[3]/button",
            "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[2]/ul/li[4]/button"
        ]

        for xpath in menu_item_xpaths:
            menu_item = wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            menu_item.click()
            assert "selected" in menu_item.get_attribute("class"), f"{xpath} öğesi seçili değil!"

    def test_certificate_page(self):
        self.driver.get("https://tobeto.com/platform")
        wait = WebDriverWait(self.driver, 10)
        eğitimlerim_link = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="lessons-tab"]')))
        eğitimlerim_link.click()
        eğitim_kutuları = wait.until(ec.visibility_of_all_elements_located((By.XPATH, '//*[@id="all-lessons-tab-pane"]/div/div/div/div[2]/a')))
        assert len(eğitim_kutuları) <= 4, "Dörtten fazla eğitim kutusu bulunmaktadır."
        for kutu in eğitim_kutuları:
            ActionChains(self.driver).move_to_element(kutu).perform()
            time.sleep(1)
            mor_çerçeve = kutu.find_element(By.CLASS_NAME, 'mor-cerceve')
            assert mor_çerçeve.is_displayed(), "Eğitim kutusunun etrafında mor çerçeve görüntülenmemiştir."
            eğitime_git_butonu = kutu.find_element(By.XPATH, './/button[text()="Eğitime Git"]')
            assert eğitime_git_butonu.value_of_css_property('background-color') == 'rgba(128, 0, 128, 1)', "Eğitime Git butonunun rengi mor değildir."
            assert eğitime_git_butonu.value_of_css_property('color') == 'rgba(255, 255, 255, 1)', "Eğitime Git butonunun yazı rengi beyaz değildir."
