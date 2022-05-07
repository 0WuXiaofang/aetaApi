#正确性校验
#时间范围校验（自己选）
#震级
#地区
#经纬度
# 关于地震部分数据查询，从地震目录查询
from flask import Flask, request
from werkzeug.utils import redirect
from flask_cors import  CORS
#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
from utils.jsonfyDbtable import *
from utils.db_handle import *
from libs.error import get_res_message, check_exception_time

from libs.redprint import Redprint


import json
# 实例化数据库对象
db=DB()
jsfy=jsonfyDbtable()
# 去封装一个模糊查询
#调用模糊查询的方法
# app = Flask(__name__)
api = Redprint('earthquakePredict')
# CORS(app, resources=r'/*')
# 联表做范围查询
@check_exception_time
@api.route("/correctCheck/classify_magnitude", methods=["GET"])
def predict_classify_magnitude():
    search_List=["Time","id","Location","deep","Magnitude","Longtitude","Latitude"]

    data=request.args.get("data")
    # max_data=request.args.get("min_data")
    magn_levelScopeMax = request.args.get("magn_levelScopeMax")
    magn_levelScopeMin = request.args.get("magn_levelScopeMin")
    targData_str=','.join(search_List)
    magn_levelScopeStr="Magnitude>"+magn_levelScopeMin+" AND Magnitude<"+magn_levelScopeMax+" AND LOCATE("+"'"+data+" '"+",Time)"
    # magn_levelScopeStr="'Time' like "+"'"+data+"'"+'%'+" and Magnitude>%s AND Magnitude<%s "%(magn_levelScopeMin,magn_levelScopeMax)
    # print("地震级别", magn_level)
    #     调用函数对数据进行分类

    # result = seismicL_classify(magn_level)

    result = db.get_youDefine_fondata('tab_alleqlist',targData_str,magn_levelScopeStr)


    if result == 0:
        return json.dumps({"statment": "未找到地震相关信息" })

    res = jsfy.jsonfy(search_List,result)
    return res
    # try:


    # except:
    #     db.close_connect()
    #     return json.dumps({"statment": "程序执行中断" })

# if __name__ == '__main__':
#     app.run()
