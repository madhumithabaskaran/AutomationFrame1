import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\61094914\\PycharmProjects\\AutomationFrame1\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getEmail():
        name=config.get('common info','username')
        return name
    @staticmethod
    def getPass():
        userpass=config.get('common info','password')
        return userpass
