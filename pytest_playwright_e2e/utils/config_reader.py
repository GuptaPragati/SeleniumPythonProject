import configparser
import os

class ConfigReader:
    def __init__(self, env="DEFAULT"):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.env = env

    def get_base_url(self):
        return self.config[self.env]['base_url']

    def get_browser_name(self):
        return self.config[self.env].get('browser_name', 'chrome')

    def get_username(self):
        return self.config[self.env].get('username', 'admin')

    def get_password(self):
        return self.config[self.env].get('Password','admin')

    def get_browser_slow(self):
        return  self.config[self.env]['slow']
