from selenium import webdriver
from selenium.webdriver.common.by import By


class swagLoginPage:

    #declare webelement globally
    inpUsernameXpath="//*[@id='user-name']"
    inpaPsswordXpath="//*[@id='password']"
    butLoginXpath="//*[@id='login-button']"
    errorMsgXpath="//h3[@data-test='error']"

    #2: initialization webdriver object globally
    def __init__(self,driver):
        self.driver=driver

    def enterUsername(self,username):
        self.driver.find_element(By.XPATH, self.inpUsernameXpath).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(By.XPATH, self.inpaPsswordXpath).send_keys(password)

    def clickButton(self):
        self.driver.find_element(By.XPATH, self.butLoginXpath).click()

    def invalidLoginMessage(self):
        return self.driver.find_element(By.XPATH, self.errorMsgXpath).text
