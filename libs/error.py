# -*- coding: utf-8 -*-
# @Time : 2021/9/8 23:44
# @Author : KK
# @File : school_news.py
# @Software: PyCharm
import time
import traceback
from functools import wraps
from flask import Flask, make_response, jsonify, request
from loguru import logger

logger.add("logs/loguru.log", rotation="100KB", compression="zip", encoding="utf-8")

app = Flask(__name__)

exception_dict = {
    "AssertionError": "断言语句（assert）失败",
    "AttributeError": "尝试访问未知的对象属性",
    "EOFError": "用户输入文件末尾标志EOF（Ctrl+d）",
    "FloatingPointError": "浮点计算错误",
    "GeneratorExit": "generator.close()方法被调用的时候",
    "ImportError": "导入模块失败的时候",
    "IndexError": "索引超出序列的范围",
    "KeyError": "字典中查找一个不存在的关键字",
    "KeyboardInterrupt": "用户输入中断键（Ctrl+c",
    "MemoryError": "内存溢出（可通过删除对象释放内存）",
    "NameError": "尝试访问一个不存在的变量",
    "NotImplementedError": "尚未实现的方法",
    "OSError": "操作系统产生的异常（例如打开一个不存在的文件）",
    "OverflowError": "数值运算超出最大限制",
    "ReferenceError": "弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象",
    "RuntimeError": "一般的运行时错误",
    "StopIteration": "迭代器没有更多的值",
    "SyntaxError": "Python的语法错误",
    "IndentationError": "缩进错误",
    "TabError": "Tab和空格混合使用",
    "SystemError": "Python编译器系统错误",
    "SystemExit": "Python编译器进程被关闭",
    "TypeError": "不同类型间的无效操作",
    "UnboundLocalError": "访问一个未初始化的本地变量（NameError的子类）",
    "UnicodeError": "Unicode相关的错误（ValueError的子类）",
    "UnicodeEncodeError": "Unicode编码时的错误（UnicodeError的子类）",
    "UnicodeDecodeError": "Unicode解码时的错误（UnicodeError的子类）",
    "UnicodeTranslateError": "Unicode转换时的错误（UnicodeError的子类）",
    "ValueError": "传入无效的参数",
    "ZeroDivisionError": "除数为零",
}


def get_res_message(message, status_code, content=None):
    # 异常处理信息函数，默认content为空
    res_data = {
        "code": status_code,
        "datas": content,
        "msg": message,

    }
    res = jsonify(res_data)
    res.headers['date'] = time.strftime("%Y-%m-%d %H:%M:%S %a UTF", time.localtime())
    return res


# 异常检测和程序运行时间记录
def check_exception_time(f):
    @wraps(f)
    def check(*args, **kwargs):
        try:
            # return f(*args, **kwargs)
            timestamp_start = float(time.time())
            res = f(*args, **kwargs)
            timestamp_end = float(time.time())
            cost_timestamp = timestamp_end - timestamp_start
            # cost_time = get_duration(cost_timestamp)
            logger.info("[%s]运行时间:[%s]秒" % (f.__name__, round(cost_timestamp, 2)))
            return res
        except Exception as e:
            # 以下是异常简要
            logger.info("未知异常简要：" + str(e))
            # 此处需要用到traceback模块捕获具体异常，以便展示具体的错误位置。以下是格式化后的具体异常
            exception_desc = "未知异常"
            for i in exception_dict:
                # print(i, exception_dict[i])
                if i in str(traceback.format_exc()):
                    exception_desc = "参考异常：" + exception_dict[i]
            logger.info("未知异常具体：" + str(traceback.format_exc()))
            # 以下字典格式不能http返回，所以需要转换成str,提前将traceback.format_exc()也转换成str，否则返回字符串没有引号
            res_data = {
                "code": 400,
                "msg": exception_desc,
                "datas": 'null',           # str(traceback.format_exc())   显示错误日志
            }
            return make_response(jsonify(res_data))

    return check

