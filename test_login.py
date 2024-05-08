#Capstone Project 2
#importing pytest
import pytest


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Data import data
from Locators import locator


class Test_Project2:
    @pytest.fixture
    #Booting Method
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url)  # this code is used to get the url from the data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # this code is used to for explicit wait
        yield
        self.driver.quit()
    #this method will fill the text to the input box
    def fillText(self, locator, textvalue):
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        # this will clear the values
        element.clear()
        element.send_keys(textvalue)
#method to click
    def clickButton(self, locator):
        self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()
#method to get Xpath
    def getTextBYXpath(self, locator):
        return self.driver.find_elements(by=By.XPATH, value=locator)
    def getTextBYID(self, locator):
        return self.driver.find_elements(by=By.ID, value=locator)

    def getTextBYCLASSNAME(self, locator):
        return self.driver.find_elements(by=By.CLASS_NAME, value=locator)

    def getTextBYTAGNAME(self, locator):
        return self.driver.find_elements(by=By.TAG_NAME, value=locator)

#TC_PIM_01
    def test_forgotPassword(self,boot):
        try:
            # This code is used to find the path and fill the username
            self.fillText(locator.WebLocators().usernameLocator, data.WebData().username)
            # This code is used to click Forgot your Password
            self.clickButton(locator.WebLocators().forgotLocator)
            # This code is used to enter the username
            self.fillText(locator.WebLocators().resetusernameLocator, data.WebData().username)
            # This code is used to click the reset password button

            self.clickButton(locator.WebLocators().resetLocator)
        except NoSuchElementException as e:
                print(e)
            # This code is used to check whether the link is sent for reset
        print("Reset Password link sent Successfully")

    # TC_PIM_02

    def test_header(self,boot):
        try:
            # THis will fill the username
            self.fillText(locator.WebLocators().usernameLocator, data.WebData().username)
            # This  fill the password
            self.fillText(locator.WebLocators().passLocator, data.WebData().password)
            # This code is used to find the path and click the login button
            self.clickButton(locator.WebLocators().subLocator)
            # This code is used to click the Admin
            self.clickButton(locator.WebLocators().adminLocator)
            # This will fetch the tittle
            tittle = self.driver.title
            print(tittle)
            #for loop for looping in
            a = self.getTextBYXpath(locator.WebLocators().optionsLocator)
            for j in a:
                print(j.text)
            print("headers on Admin Page are displayed")
        except NoSuchElementException as e:
            print(e)

    # TC_PIM_03
    def test_menu(self,boot):
        try:
            # THis code is used to find and fill the username
            self.fillText(locator.WebLocators().usernameLocator, data.WebData().username)
            # This code is used to find and fill the password
            self.fillText(locator.WebLocators().passLocator, data.WebData().password)
            # This code is used to find the path and click the login button
            self.clickButton(locator.WebLocators().subLocator)
            # This code is used to click the Admin
            self.clickButton(locator.WebLocators().adminLocator)
            self.driver.execute_script('window.scrollBy(0, 1000)')

            a = self.getTextBYXpath(locator.WebLocators().optionsLocator)

            for j in a:
                print(j.text)
            sleep(5)
            print("MainMenu on Admin Page are displayed")
        except NoSuchElementException as e:
            print(e)
