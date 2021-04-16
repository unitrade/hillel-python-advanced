import json
import datetime


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
        return log

    def _logging_handler(self, log: dict):
        pass

    @staticmethod
    def _convert_to_json(log: dict):
        return json.dumps(log)


class StdOutLogger(Logger):
    def __init__(self, name):
        super().__init__(name)

    def _logging_handler(self, log: dict):
        print(self._convert_to_json(log))


class FileLogger(Logger):
    def __init__(self, name, filename="my_log.log"):
        super().__init__(name)
        self._filename = filename

    def _logging_handler(self, buffer):
        with open(self._filename, 'a') as f:
            f.write(self._convert_to_json(buffer) + "\n")


if __name__ == '__main__':
    l1 = StdOutLogger("Success_logger")
    l2 = FileLogger("Fail_logger", "failed.log")

    l1.info("Creating new server in HG 1035 : 10.0.15.220:3306 , gtid_port=0, weight=1, status=0")
    l2.warning("Error during query on (1032,10.0.1.38,3306): 1062, Duplicate entry '6058-4006' for key 'interlocutors'")
    l2.error("Got error: mmsd 0x7f42537dbd80 , MYSQL 0x7f4277a01900 , FD 262 : timeout check")
    l2.error("Got error: mmsd 0x7f42537dbd80 , MYSQL 0x7f4277a01900 , FD 262 : timeout check")


