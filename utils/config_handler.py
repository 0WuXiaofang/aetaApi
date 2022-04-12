from configparser import ConfigParser
from config.public_data import config_path


class ConfigParse(object):
    def __init__(self):
        pass

    @classmethod
    def get_db_config(cls):
        # cls使用的类方法,cls就是指定本身


        cls.cfp = ConfigParser()
        # print(cls.cfp)

        cls.cfp.read(config_path,encoding="utf_8")
        print(config_path)
        print("config1")
        host = cls.cfp.get("sec_a", "host")
        print("config3")
        port = cls.cfp.get("sec_a", "port")
        user = cls.cfp.get("sec_a", "user")
        password = cls.cfp.get("sec_a", "password")
        db = cls.cfp.get("sec_a", "db_name")
        print("config2")
        return {"host": host, "port": port, "user": user, "password": password, "db": db}
if __name__ == '__main__':
    print("执行config-handler")
    cp = ConfigParse()
    result = cp.get_db_config()
    print(result)