# 生成config对象
from configparser import ConfigParser
conf = ConfigParser()

  # 用config对象读取配置文件

conf.read("intest.ini",encoding="utf_8")

 # 以列表形式返回所有的section



 # 指定section，option读取值

str_val = conf.get("sec_a", "a_key1")
print(str_val)

int_val = conf.getint("sec_a", "a_key2")

