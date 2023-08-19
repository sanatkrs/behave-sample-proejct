import configparser
from pathlib import Path

config = configparser.ConfigParser()
basePath = Path(__file__).parent.parent
config.read(basePath  / "Config/Config.ini")


class ReadConfig():
    @staticmethod
    def getWebUrl():
        #url = config.get('common info', 'baseUrl')
        url = config['common info']['baseUrl']
        return url

    @staticmethod
    def getUserName():
        # url = config.get('common info', 'baseUrl')
        userName = config['common info']['username']
        return userName

    @staticmethod
    def getPassword():
        # url = config.get('common info', 'baseUrl')
        password = config['common info']['password']
        return password
