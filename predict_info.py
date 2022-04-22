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
# 左右连接，连接两个表，staioninfo 与predict_t连接做经纬度查询

app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/predict/Location_search',methods=["POST"])
def get_alikeWord():


    try:
        '''
        通过经纬度查询地理位置
        :return:
        '''
        Latitude = request.args.get("Latitude")
        Longitude = request.args.get("Longitude")
        # 需要做连表查询

        search_result=db.contactLocation_search(Longitude,Latitude)
        search_List=["Latitude","Longitude"]
        # search_ListStr="Latitude=%d&&Longitude=%d"%(Latitude,Longitude)
        # search_result =db.get_youDefine_fondata("Location","staioninfo",search_ListStr)
        search_result = jsfy.jsonfy(search_List, search_result)
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
@app.route('/predict/get_predictTable_alldata',methods=["GET"])
def get_predictTable_alldata():
    # 地震表头
    predictTable_title=["id","class_name","magn_level","Longitude","Latitude"]
    '''
    获取预测表所有信息
    :return:
    '''
    # searchStr=','.join(predictTable_data)
    targ_keyStr = ','.join(predictTable_title)
    predictTable_data = db.get_tragColumn_data_list(targ_keyStr,"predict_t")
    predictTable_data = jsfy.jsonfy(predictTable_title,predictTable_data)
    print("preallT", predictTable_data)
    return predictTable_data
    # try:

    # except:
    #     db.close_connect()
    #     return "fail"


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




