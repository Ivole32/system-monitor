import configparser
import os

config = configparser.ConfigParser()

config_path = "./config.ini"

class Configuration:
    def __init__(self):
        self._config_options = {
            "allow-commandline": True,
            "allow-system-commands": True
        }

        if not os.path.exists(config_path):
            config['config'] = {}
            config['custom-commands'] = {"commands": []}
            self.write_to_config(self._config_options)
        else:
            config.read(config_path)
            self.__missing_options = self.__check_config_for_completeness()
            if self.__missing_options:
                self.write_to_config(self.__missing_options)

    def __check_config_for_completeness(self) -> dict:
        missing = {}
        if 'config' not in config:
            config['config'] = {}
            return self._config_options

        for key, value in self._config_options.items():
            if key not in config['config']:
                missing[key] = value
        
        return missing

    def write_to_config(self, options, topic="config") -> None:
        if 'config' not in config:
            config['config'] = {}

        if 'custom-commands' not in config:
            config['custom-commands'] = {"commands": []}

        for key, value in options.items():
            config[topic][key] = str(value)
        
        with open(config_path, "w") as configfile:
            config.write(configfile)

    def get_config_value(self, value, topic="config") -> str:
        try:
            return config[topic][value]
        except Exception as e:
            return None