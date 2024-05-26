import json

class Config:
    def __init__(self, config_file='config.json') -> None:
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Config file {self.config_file} not found")
        except json.JSONDecodeError:
            raise Exception("Error decoding the config file")


    def get(self, key, default=None):
        return self.config.get(key, default)