from selenium.webdriver.common.by import By


class SearchCustomers:
    search_email_xpath="//input[@id='SearchEmail']"
    search_fname_xpath="//input[@id='SearchFirstName']"
    search_lname_xpath="//input[@id='SearchLastName']"
    search_button_xpath="//button[@id='search-customers']"
    table_xpath="//table[@id='customers-grid']"
    table_row_xpath="//table[@id='customers-grid']//tbody/tr"
    table_col_xpath="//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.search_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.search_email_xpath).send_keys(email)

    def setFname(self,fname):
        self.driver.find_element(By.XPATH,self.search_fname_xpath).clear()
        self.driver.find_element(By.XPATH,self.search_fname_xpath).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element(By.XPATH,self.search_lname_xpath).clear()
        self.driver.find_element(By.XPATH,self.search_lname_xpath).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_row_xpath))


    def getNoOfcolumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_col_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            Name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[3]").text
            if Name==name:
                flag=True
                break
        return flag