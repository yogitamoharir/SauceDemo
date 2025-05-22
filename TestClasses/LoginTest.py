import pytest

from PageClasses.Home import SwagLabHomePage
from PageClasses.Login import swagLoginPage
from UtilityFiles.ReadExcelData import ReadTD
from UtilityFiles.customLogger import LogGen
from UtilityFiles.readProperties import ReadConfig


class Test_swagLoginPage:
    logger = LogGen.loggen()

    def loginToApp(self,setup):
        driver=setup
        login = swagLoginPage(driver)
        login.enterUsername(ReadConfig.getAppUsername())
        login.enterPassword(ReadConfig.getAppPassword())
        login.clickButton()

    @pytest.mark.sanity
    def test_TC1_loginAndTitleValidation(self,setup):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")
        driver = setup
        self.loginToApp(driver)

        actTitle=driver.title
        expTilte=ReadTD.getTestData(1,1)

        if actTitle==expTilte:
            assert True
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\Screenshots\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False

    @pytest.mark.sanity
    def test_TC2_loginFailureValidation(self,setup):
        userName="SwapnilJoshi"
        passWord="abcABC@1234"
        driver=setup

        login=swagLoginPage(driver)
        login.enterUsername(userName)
        login.enterPassword(passWord)
        login.clickButton()
        act_msg=login.invalidLoginMessage()
        exp_msg="Epic sadface: Username and password do not match any user in this service"

        assert True if act_msg == exp_msg else False

    @pytest.mark.regression
    def test_TC3_Verify_ProductName(self,setup):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC2_Verify_ProductName-------")

        driver = setup
        self.loginToApp(driver)

        home=SwagLabHomePage(driver)
        actProdctName=home.getBackpackProductName()
        expProductName=ReadTD.getTestData(2,1)

        if actProdctName==expProductName:
            assert True
            self.logger.info("----Passed- Act & Exp product Name match----")
        else:
            driver.save_screenshot("..\\SS\\test_TC2_Verify_ProductName.png")
            self.logger.error("----Failed- Act & Exp product Name mist-match----")
            assert False

    @pytest.mark.regression
    def test_TC4_VerifyProductPrice(self,setup):
            driver=setup
            self.loginToApp(driver)

            price=SwagLabHomePage(driver)
            actPrice=price.getBackpackProductPrice()
            expPrice=ReadTD.getTestData(3,1)
            if float(actPrice)==float(expPrice):
                assert True
                self.logger.info("----Passed- Act & Exp product Price match----")
            else:
                driver.save_screenshot("..\\SS\\test_TC2_Verify_ProductPrice.png")
                self.logger.error("----Product Price Mismatch----")
                assert False

    @pytest.mark.smoke
    def test_TC5_verifyProductSize(self,setup):
            driver=setup
            self.loginToApp(driver)
            item=SwagLabHomePage(driver)
            listOfItem=item.getAllProductSize()
            expItem=ReadTD.getTestData(4,1)
            if len(listOfItem)==expItem:
                assert True
                self.logger.info("----Passed- Act & Exp product Size match----")
            else:
                driver.save_screenshot("..\\SS\\test_TC2_Verify_ProductPrice.png")
                self.logger.error("----No of product mismatch----")
                assert False

    @pytest.mark.smoke
    @pytest.mark.functional
    def test_TC6_verifyProductAllPrice(self, setup):
        self.logger.info("----test_TC5_verifyProductAllPrice-------")
        driver = setup
        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        actTotalPrice = home.getAllProductTotalPrice()
        expTotalPrice = float(ReadTD.getTestData(5, 1))

        if actTotalPrice == expTotalPrice:
            assert True
            self.logger.info("----Passed- Act & Exp Total Price match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC5_verifyProductAllPrice.png")
            self.logger.error("----Failed- Act & Exp Total price mist-match----")
            assert False