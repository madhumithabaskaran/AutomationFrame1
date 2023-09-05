import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomers

class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPass()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByMailID(self,setup):
        self.logger.info("*********Test_004_SearchCustomerByMail***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Succesful*******")

        self.adc = AddCustomers(self.driver)
        self.adc.clickOnCustomerMenu()
        time.sleep(4)
        self.adc.clickOnCustomerSubMenu()

        self.logger.info("*********providing email for searching customer*******")
        self.sc=SearchCustomers(self.driver)
        self.sc.setEmail("victoria_victoria@nopCommerce.com")
        self.sc.clicksearch()
        time.sleep(5)
        status=self.sc.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("*********successfully searched customers by email*******")
        self.logger.info("*******Test_004_SearchCustomerByMail_Finished*********")
        self.driver.close();

