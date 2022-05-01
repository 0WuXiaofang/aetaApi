# 预测数据分析导出
from flask import Flask, request
from werkzeug.utils import redirect
from flask_cors import  CORS
from utils.db_handle import *
from utils.jsonfyDbtable import *
from libs.redprint import Redprint

#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
import json
# 实例化数据库对象


api = Redprint('earthquakePredict')

db=DB()
jsfy=jsonfyDbtable()
# 去封装一个模糊查询
#调用模糊查询的方法
# 左右连接，连接两个表，staioninfo 与predict_t连接做经纬度查询
# 地震震级区别查询，范围查询
# def seismicL_classify(magnitude):
#     '''
#     地震级别分类
#     :return:
#     '''
#     try:
#
#         print("地震级别开始分类")
#         if magnitude > 0 and magnitude < 3.4:
#             print("0~3.4")
#             result = db.get_scope_data("eqlst", "*", "Magnitude", "<=3.4")
#             return result
#         elif magnitude >= 3.4 and magnitude <= 4.5:
#             print("3.4~4.5")
#             result = db.get_youDefine_fondata("eqlst", "*", "Magnitude>=3.6 && Magnitude<=4.5")
#             return result
#         elif magnitude >= 4.6 and magnitude <= 5.5:
#             print("4.6~5.5")
#             result = db.get_youDefine_fondata("eqlst", "*", "Magnitude>=4.6 && Magnitude<=5.5")
#             return result
#         elif magnitude >= 5.6 and magnitude < 8.0:
#             print("5.6~8.0")
#             result = db.get_youDefine_fondata("eqlst", "*", "Magnitude>=5.6 && Magnitude<=8.0")
#             return result
#     except:
#         db.close_connect()
#         return "fail"

# 联表做范围查询
@api.route("/predict/classify_magnitude", methods=["GET"])
def predict_classify_magnitude():

    try:
        magn_levelScopeMax = request.args.get("magn_levelScopeMax")
        magn_levelScopeMin = request.args.get("magn_levelScopeMin")
        magn_levelScopeStr="predict_t.magn_level>%s AND predict_t.magn_level<%s "%(magn_levelScopeMin,magn_levelScopeMax)
        # print("地震级别", magn_level)
        #     调用函数对数据进行分类

        # result = seismicL_classify(magn_level)

        search_List=["Title","id","class_name","StationID","magn_level","Longitude","Latitude"]
        result = db.contactLocation_magnClassifySearch(magn_levelScopeStr)


        if result == 0:
            return json.dumps({"statment": "未找到地震相关信息" })

        res = jsfy.jsonfy(search_List,result)
        return res

    except:
        db.close_connect()
        return json.dumps({"statment": "程序执行中断" })


@api.route('/predict/get_locationKeywordSearch',methods=["GET"])
def get_keywordSearch():
    '''地区关键字查询
    '''
    try:
        columnValue = request.args.get("Location")
        search_result=db.contactLocation_alikeSearch("Title",columnValue)
        search_List=["Title","id","class_name","StationID","magn_level","Longitude","Latitude"]
        kSearch_result = jsfy.jsonfy(search_List,search_result)
        # print(kSearch_result)
        return kSearch_result

    except:
        db.close_connect()
        return "fail"

@api.route('/predict/StationID_search',methods=["GET"])
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
        # print(search_result)
        return search_result
    except:
        db.close_connect()
        return "fail"
#     通过地震震级查询
@api.route('/predict/magnLevel_search',methods=["GET"])
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
        # print(search_result)
        return search_result

    except:
        db.close_connect()
        return "fail"

# 根据经纬度范围片区划分
#     通过地震震级查询
@api.route('/predict/className_search',methods=["GET"])
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
        # print(search_result)
        return search_result

    except:
        db.close_connect()
        return "fail"



@api.route('/predict/get_predictTable_alldata',methods=["GET"])
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
    # print("preallT", predictTable_data)
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





