import sys
from config import config_path

class Colors:
    RESET = "\033[0m"
    INFO = "\033[94m"
    WARN = "\033[93m"
    OK = "\033[92m"
    ERROR = "\033[91m"

class Logger:
    def __init__(self, stream=sys.sdtout) -> None:
        self.__stream = stream
        self.debug_mode = self.__get_debug_mode()

    def __get_debug_mode(self) -> bool:
        try:
            with open(config_path, "r") as config:
                content = config.read()
                if "debug-mode = False" in content:
                    return False
                return True
        except Exeption:
            return True

    def info(self, message:str) -> None:
        if self.debug_mode:
            self._print_colored("[INFO]", message, Colors.INFO)

    def warn(self, message:str) -> None:
        self._print_colored("[WARN]", message, Colors.WARN)

    def ok(self, message:str) -> None:
        if self.debug_mode:
            self._print_colored("[OK]", message, Colors.OK)

    def error(self, message:str) -> None:
        self._print_colored("[ERROR]", message, Colors.ERROR)

    def _print_colored(self, prefix:str, message:str, color:str):
        self.__stream.write(f"{color}{prefix}{Colors.RESET} {message}\n")
        self.__stream.flush()