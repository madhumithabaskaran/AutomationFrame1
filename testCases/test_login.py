import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getEmail()
    password=ReadConfig.getPass()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("******************** Test_001_Login ****************")
        self.logger.info("****************** Verifying Home Page Title *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Title Verification Passed ************")
        else:
            self.driver.save_screenshot("C:\\Users\\61094914\\PycharmProjects\\AutomationFrame1\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************** Title Verification failed **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*********** Verifying Login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        #self.ad=Addcustomers(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login test is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\61094914\\PycharmProjects\\AutomationFrame1\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********* Login test is failed ***********")
            assert False

