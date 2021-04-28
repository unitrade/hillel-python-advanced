import json
import datetime
from os import linesep


class Logger:

    def __init__(self, name: str = "default_logger"):
        self.name = name

    def info(self, msg: str):
        self._logging_handler(self._logging_formatter(msg, "INFO"))

    def warning(self, msg: str):
        self._logging_handler(self._logging_formatter(msg, "WARNING"))

    def error(self, msg: str):
        self._logging_handler(self._logging_formatter(msg, "ERROR"))

    def _logging_formatter(self, msg, level):
        log = {
            'time': datetime.datetime.now().isoformat(),
            "logger": "(%s)" % self.name,
            'level': "[%s]" % level,
            'msg': msg
        }
        return self.__convert_to_json(log)

    def _logging_handler(self, log: dict):
        pass

    @staticmethod
    def __convert_to_json(log: dict):
        return json.dumps(log)


class StdOutLogger(Logger):
    def __init__(self, name):
        super().__init__(name)

    def _logging_handler(self, log: dict):
        print(log)


class FileLogger(Logger):
    def __init__(self, name, filename="my_log.log"):
        super().__init__(name)
        self._filename = filename

    def _logging_handler(self, buffer):
        with open(self._filename, 'a') as f:
            f.write(buffer + linesep)


class LogDecorator(Logger):
    def __init__(self, name: str, list_loggers: list):
        super().__init__(name)
        self._list_loggers = list_loggers

    def info(self, msg: str):
        for logger in self._list_loggers:
            logger.info(msg)

    def warning(self, msg: str):
        for logger in self._list_loggers:
            logger.warning(msg)

    def error(self, msg: str):
        for logger in self._list_loggers:
            logger.error(msg)


if __name__ == '__main__':
    l1 = StdOutLogger("Success_logger")
    l2 = FileLogger("Fail_logger", "failed.log")

    l1.info("Creating new server in HG 1035 : 10.0.15.220:3306 , gtid_port=0, weight=1, status=0")
    l2.warning("Error during query on (1032,10.0.1.38,3306): 1062, Duplicate entry '6058-4006' for key 'interlocutors'")
    l2.error("Got error: mmsd 0x7f42537dbd80 , MYSQL 0x7f4277a01900 , FD 262 : timeout check")
    l2.error("Got error: mmsd 0x7f42537dbd80 , MYSQL 0x7f4277a01900 , FD 262 : timeout check")

    l3 = LogDecorator('Log Decorator', list_loggers=[
        StdOutLogger('stout_decor'), FileLogger('file_decor', filename='decor.log')
    ])
    l3.info("Decor info")
    l3.error("Decor error")

    # {"time": "2021-04-18T07:24:27.950428", "logger": "(Success_logger)", "level": "[INFO]", "msg": "Creating new
    # server in HG 1035 : 10.0.15.220:3306 , gtid_port=0, weight=1, status=0"}
    # {"time": "2021-04-18T07:24:27.951165","logger": "(stout_decor)", "level": "[INFO]", "msg": "Decor info"}
    # {"time": "2021-04-18T07:24:27.951359","logger": "(stout_decor)", "level": "[ERROR]", "msg": "Decor error"}
