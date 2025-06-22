import configparser
import os

config = configparser.ConfigParser()

config_path = "./config.ini"

class Configuration:
    def __init__(self):
        self._config_options = {
            "debug-mode": True
        }

        if not os.path.exists(config_path):
            config['config'] = {}
            self.__write_to_config(self._config_options)
        else:
            config.read(config_path)
            self.__missing_options = self.__check_config_for_completeness()
            if self.__missing_options:
                self.__write_to_config(self.__missing_options)

    def __check_config_for_completeness(self) -> dict:
        missing = {}
        if 'config' not in config:
            config['config'] = {}
            return self._config_options

        for key, value in self._config_options.items():
            if key not in config['config']:
                missing[key] = value
        
        return missing

    def __write_to_config(self, options) -> None:
        if 'config' not in config:
            config['config'] = {}

        for key, value in options.items():
            config['config'][key] = str(value)
        
        with open(config_path, "w") as configfile:
            config.write(configfile)

    def get_config_value(self, value) -> str:
        try:
            return config['config'][value]
        except Exception as e:
            return None