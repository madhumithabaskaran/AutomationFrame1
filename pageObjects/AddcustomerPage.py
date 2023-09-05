import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomers:
    customer_menu_xpath=" //a[ @ href ='#'] // p[contains(text(), 'Customers')]"
    subcustomer_menu_option="//a[ @ href ='/Admin/Customer/List'] // p[contains(text(), 'Customers')]"
    add_new_customer_xpath="//a[ @ href = '/Admin/Customer/Create']"
    toggle_xpath="//i[ @class ='fa toggle-icon fa-plus']"
    mail_xpath="// input[@ id='Email']"
    password_xpath="//input[@ id='Password']"
    firstname_xpath="//input[@ id='FirstName']"
    lastname_xpath="//input[@ id='LastName']"
    male_gender_xpath="//input[@ id='Gender_Male']"
    female_gender_xpath="//input[@ id='Gender_Female']"
    date0fbirth_input_xpath="//input[@id='DateOfBirth']"
    calender_icon_xpath="//span[@class ='k-icon k-i-calendar']"
    date_xpath="//div[@ id='f905054d-c585-4c77-8cbd-a28dc3fc4118']//div[2]//table//tbody//tr//td//a[@ title='Wednesday, July 26, 2023']"
    comapny_xpath="// input[@ id='Company']"
    customer_roles_xpath="//div[@ class ='card-body']//div[10]//div[2]//div//div//div//div[@class='k-multiselect-wrap k-floatwrap']"
    adminstrator_xpath="//ul[@ id='SelectedCustomerRoleIds_listbox']//li[contains(text(),'Administrators')]"
    forum_moderators_xpath="//li[contains(text(), 'Forum Moderators')]"
    guests_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']//li[contains(text(), 'Guests')]"
    registered_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']//li[contains(text(), 'Registered')]"
    vendors_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']//li[contains(text(),'Vendors')]"
    vendor_xpath="//select[@id='VendorId']"
    vendor_option1_xpath="//select[@id='VendorId']//option[@ value='0']"
    vendor_option2_xpath="//select[@id='VendorId']//option[@ value='1']"
    vendor_option3_xpath="//select[@id='VendorId'] // option[@ value='2']"
    admin_comment_xpath="//textarea[@id='AdminComment']"
    save_button_xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.customer_menu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH,self.subcustomer_menu_option).click()

    def clickAddNewCustomer(self):
        self.driver.find_element(By.XPATH,self.add_new_customer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.mail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def setFname(self,Fname):
        self.driver.find_element(By.XPATH,self.firstname_xpath).send_keys(Fname)

    def setLname(self,Lname):
        self.driver.find_element(By.XPATH,self.lastname_xpath).send_keys(Lname)

    def selectGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.male_gender_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.female_gender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.male_gender_xpath).click()

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.date0fbirth_input_xpath).send_keys(dob)

    def setCompanyname(self,cname):
        self.driver.find_element(By.XPATH,self.comapny_xpath).send_keys(cname)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.customer_roles_xpath).click()
        time.sleep(4)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.registered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.adminstrator_xpath)
        elif role=='Guests':
            time.sleep(4)
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem=self.driver.find_element(By.XPATH,self.guests_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.vendors_xpath)
        elif role=='Forum Moderators':
            self.listitem=self.driver.find_element(By.XPATH,self.forum_moderators_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.guests_xpath)
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setVendors(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.vendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self,content):
        self.driver.find_element(By.XPATH,self.admin_comment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()



    




