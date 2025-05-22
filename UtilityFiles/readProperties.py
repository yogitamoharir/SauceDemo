import configparser

config=configparser.RawConfigParser()
# config.read("./Configuration/config.ini")
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getAppUrl():
        urlValue=config.get("credentials","URL")
        return urlValue

    @staticmethod
    def getAppUsername():
        UNValue = config.get("credentials","username")
        return UNValue

    @staticmethod
    def getAppPassword():
        PWDValue = config.get("credentials", "password")
        return PWDValue



