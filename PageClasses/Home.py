from selenium.webdriver.common.by import By
from selenium import webdriver

class SwagLabHomePage:

    #1: declare web elements globally
    textBackpackProductXpath="//div[text()='Sauce Labs Backpack']"
    textBackpackProductPriceXpath="(//div[@class='inventory_item_price'])[1]"
    allProdictSizeXpath="//div[@class='inventory_item_name ']"
    textAllProductTotalPriceXpath = "//div[@class='inventory_item_price']"

    #2: initialization webdriver object globally
    def __init__(self,driver):
        self.driver=driver

    #3: perform actions
    def getBackpackProductName(self):
        productName=self.driver.find_element(By.XPATH,self.textBackpackProductXpath).text
        return productName

    def getBackpackProductPrice(self):  #added
        productPriceWithDoller = self.driver.find_element(By.XPATH, self.textBackpackProductPriceXpath).text
        productPrice = productPriceWithDoller.replace("$", "")
        return productPrice

    def getAllProductSize(self):
        size=self.driver.find_elements(By.XPATH, self.allProdictSizeXpath)
        # print(len(size))
        return size

    def getAllProductTotalPrice(self):
        allProductPrice = self.driver.find_elements(By.XPATH, self.textAllProductTotalPriceXpath)
        TotalPrice=0

        for i in allProductPrice:
            s1=i.text      #   $32.5  -> convert WebElement to Text.
            s1=s1[1:]      #    32.5 -> String   -> remove char from string
            s1=float(s1)   #    32.5 -> float    -> covert String to float

            TotalPrice=TotalPrice+s1

        return TotalPrice