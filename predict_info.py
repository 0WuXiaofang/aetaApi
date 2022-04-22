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
@app.route('/predict/get_locationKeywordSearch',methods=["GET"])
def get_keywordSearch():
    '''地区关键字查询
    '''
    # try:
    #
    # except:
    #     db.close_connect()
    #     return "fail"
    columnValue = request.args.get("Location")
    search_result=db.contactLocation_alikeSearch("Title",columnValue)
    search_List=["Title","id","class_name","StationID","magn_level","Longitude","Latitude"]
    kSearch_result = jsfy.jsonfy(search_List,search_result)
    print(kSearch_result)
    return kSearch_result
@app.route('/predict/StationID_search',methods=["GET"])
def get_StationID_search_data():
    '''
通过站台查询地理位置
:return:
'''
    # Latitude = request.args.get("Latitude")
    # Longitude = request.args.get("Longitude")

    try:
        StationID=int(request.args.get("StationID"))
    # 需要做连表查询
        search_result=db.contactLocation_search("stationinfo","StationID",StationID)
        search_List=["Title","id","class_name","StationID","magn_level","Longitude","Latitude"]
        # search_ListStr="Latitude=%d&&Longitude=%d"%(Latitude,Longitude)
        # search_result =db.get_youDefine_fondata("Location","staioninfo",search_ListStr)
        search_result = jsfy.jsonfy(search_List, search_result)
        print(search_result)
        return search_result
    except:
        db.close_connect()
        return "fail"
#     通过地震震级查询
@app.route('/predict/magnLevel_search',methods=["GET"])
def get_magnLevel_search_data():
    '''
通过站台查询地理位置
:return:
'''
    # Latitude = request.args.get("Latitude")
    # Longitude = request.args.get("Longitude")
    #
    try:
        magn_level=request.args.get("magn_level")
    # 需要做连表查询
        search_result=db.contactLocation_search("predict_t","magn_level",magn_level)
        search_List=["Title","id","class_name","StationID","magn_level","Longitude","Latitude"]
        # search_ListStr="Latitude=%d&&Longitude=%d"%(Latitude,Longitude)
        # search_result =db.get_youDefine_fondata("Location","staioninfo",search_ListStr)
        search_result = jsfy.jsonfy(search_List, search_result)
        print(search_result)
        return search_result

    except:
        db.close_connect()
        return "fail"

# 根据经纬度范围片区划分
#     通过地震震级查询
@app.route('/predict/className_search',methods=["GET"])
def get_className_search_data():
    '''
通过站台查询地理位置
:return:
'''
    # Latitude = request.args.get("Latitude")
    # Longitude = request.args.get("Longitude")
    #
    try:
        class_name=request.args.get("class_name")
        # 需要做连表查询
        search_result=db.contactLocation_search("predict_t","class_name",class_name)
        search_List=["Title","id","class_name","StationID","magn_level","Longitude","Latitude"]
        # search_ListStr="Latitude=%d&&Longitude=%d"%(Latitude,Longitude)
        # search_result =db.get_youDefine_fondata("Location","staioninfo",search_ListStr)
        search_result = jsfy.jsonfy(search_List, search_result)
        print(search_result)
        return search_result

    except:
        db.close_connect()
        return "fail"



@app.route('/predict/get_predictTable_alldata',methods=["GET"])
def get_predictTable_alldata():
    # 地震表头
    predictTable_title=["id","class_name","StationID","magn_level","Longitude","Latitude"]
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




