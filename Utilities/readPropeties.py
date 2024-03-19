import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('basic info', 'baseURL')
        return url

    @staticmethod
    def userName():
        user_name = config.get('basic info', 'userName')
        return user_name

    @staticmethod
    def set_email():
        email = config.get('basic info', 'email')
        return email

    @staticmethod
    def set_password():
        password = config.get('basic info', 'password')
        return password
