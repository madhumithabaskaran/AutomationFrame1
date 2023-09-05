import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPass()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*********Test_003_AddCustomer***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Succesful*******")

        self.logger.info("********Adding new customers**********")

        self.adc=AddCustomers(self.driver)
        self.adc.clickOnCustomerMenu()
        self.adc.clickOnCustomerSubMenu()
        self.adc.clickAddNewCustomer()

        self.logger.info("****Providing details*******")
        self.email = random_generator() + "@gmail.com"
        self.adc.setEmail(self.email)
        self.adc.setPassword("test123")
        self.adc.setFname("Madhu")
        self.adc.setLname("Mitha")
        self.adc.selectGender("Male")
        self.adc.setDob("7/05/1985")
        self.adc.setCompanyname("LtiMindtree")
        self.adc.setCustomerRoles("Forum Moderators")
        self.adc.setVendors("Vendor 1")
        self.adc.setAdminComment("Hi nop Commerce..")
        self.adc.clickOnSave()

        self.logger.info("***saving customer info ********")

        self.logger.info("******add customer validation started*******")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("******add customer passed****")
        else:
            self.logger.error("******add customer failed****")
            assert True == False
        self.driver.close()
        self.logger.info("*****Add customer completed******")


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

