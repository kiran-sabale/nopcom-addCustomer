import configparser

config = configparser.RawConfigParser()
config.read("D:\\Credence_17_Notes\\Automation Testing Part 2 by Tushar sir\\Class 10 Notest nopcomm project\\class 6 nopcom_pytest\\Configuration\\config.ini")

#config.read("..\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password

