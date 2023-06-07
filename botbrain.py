from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os

CHROME_DRIVER_PATH = "C:\Developement\chromedriver.exe"
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]


class InternetSpeedTwitterBot:

    def __init__(self):
        self.download = 0
        self.upload = 0
        service = Service(executable_path=CHROME_DRIVER_PATH)
        options = webdriver.ChromeOptions()  # to keep the screen not closed
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.driver.maximize_window()

    def get_internet_speed(self):
        """Fetch Internet Speed, result download is [0] and upload is [1]"""
        self.driver.get(url="https://www.speedtest.net/")
        go = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go.click()
        time.sleep(50)
        self.download = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.upload = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        return float(self.download), float(self.upload)

    def tweet_at_provider(self):
        """Sending auto tweet to the ISP"""
        self.driver.get(url='https://twitter.com/')
        time.sleep(5)
        google_login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a')
        google_login.click()
        time.sleep(3)
        try:
            input_email = self.driver.find_element(By.NAME, "text")
            input_email.send_keys(EMAIL)
            next_button_1 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            next_button_1.click()
            time.sleep(3)
            input_pass = self.driver.find_element(By.NAME, "password")
            input_pass.send_keys(PASSWORD)
            login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            login_button.click()
        except NoSuchElementException:
            # If tweet detect the unusual login activity
            name = self.driver.find_element(By.NAME, "text")
            name.send_keys(USERNAME)
            time.sleep(3)
            next_1 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            next_1.click()
            time.sleep(3)
            password = self.driver.find_element(By.NAME, 'password')
            password.send_keys(PASSWORD)
            time.sleep(3)
            login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            login.click()
        finally:
            time.sleep(5)
            twit = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            twit.send_keys(
                f"The internet is really slow, download: {self.download} and upload: {self.upload}. This is for testing python automation only, don't take serous dude - Ricky"
            )
            time.sleep(2)
            send_twit = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            send_twit.click()
        time.sleep(20)
        self.driver.quit()
