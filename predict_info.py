# 预测数据分析导出
from flask import Flask, request
from werkzeug.utils import redirect
from flask_cors import  CORS
from utils.db_handle import *
from utils.jsonfyDbtable import *
#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
import json
# 实例化数据库对象
db=DB()
jsfy=jsonfyDbtable()
# 去封装一个模糊查询
#调用模糊查询的方法
app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/predict/alike_search',methods=["POST"])
def get_alikeWord():
    try:
        '''
        模糊查询，通过地理位置
        :return:
        '''
        alikeLocation = request.form.get("location_name")
        search_result = db.alike_get_data("predict_table", "Location", alikeLocation)
        search_result = jsfy.jsonfy(alikeLocation, search_result)
        print(search_result)
        return search_result
    except:
        db.close_connect()
        return "fail"

def get_keywordSearch():
    '''关键字查询
    '''
    try:
        columnTitle = request.form.get("columnTitle")
        columnValue = request.form.get("keyWord")
        kSearch_result = db.get_api_id("predict_table", columnTitle, columnValue)
        kSearch_result = jsfy.jsonfy(kSearch_result)
        print(kSearch_result)
        return kSearch_result
    except:
        db.close_connect()
        return "fail"

def get_predictTable_alldata():
    '''
    获取预测表所有信息
    :return:
    '''
    try:
        predictTable_data = db.get_api_list("predict_table")
        predictTable_data = jsfy.jsonfy(predictTable_data)
        print("preallT", predictTable_data)
        return predictTable_data
    except:
        db.close_connect()
        return "fail"


def magnScope_search():
    '''
    检索所有有关某个范围地震的消息
    :return:
    '''
    try:
        targData = request.form.get("scopeCommand")
        columnTitle = request.form.get("columnTitle")
        limit = request.form.get("limit")
        limScope_result = db.get_scope_data("predict_table", targData, columnTitle, limit)
        limScope_result = jsfy.jsonfy(limScope_result)
        return limScope_result
    except:
        db.close_connect()
        return "fail"

if __name__=='__main__':
    app.run(debug=True, port=5000, host="localhost")
    CORS(app)




