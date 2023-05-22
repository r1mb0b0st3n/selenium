from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path 
from datetime import date



class Test_DemoClass:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        #Günün tarihini al varsa günün ss ini al 
        
    def teardown_method(self):
        sleep(2)
        self.driver.quit()
    @pytest.mark.parametrize("username,password",[("standard_user",""),("","secret_sauce")])
    def test_invalid_login(self,username,password):
        self.waitForElmentVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        self.waitForElmentVisible((By.ID,"password"))
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.waitForElmentVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElmentVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessages = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-ivalid-login-{username}-{password}.png")
        print (f"Error Message : {errorMessages}")