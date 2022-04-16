#站点信息接口
# 关于地震部分数据查询，从地震目录查询
from flask_cors import  CORS
from flask import Flask, request
from werkzeug.utils import redirect
from utils.db_handle import *
#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
from utils.jsonfyDbtable import *
import json
# 实例化数据库对象
db=DB()
jsfy=jsonfyDbtable
# 去封装一个模糊查询
#调用模糊查询的方法
app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/stationSearch_stationLoc',methods=["POST"])
def search_stationLoc():
    '''
    查询站台信息关键字模糊查询地理位置
    :return:
    '''
    try:
        print("开始执行模糊查询")
        tablename = "StationInfo"
        key_word = "Title"
        alike_data = request.form.get("alike_data")
        result = db.alike_get_data(tablename, key_word, alike_data)
        if result == 0:
            return json.dumps({"statment": "未找到"})
        result = list(result[0])
        key = ["地区", "站点", "longtitude", "latitude,", "magndata", "magnupdate", "sounddata", "soundupdate"]
        print("28", result)
        print("key", type(key))
        res = dict(zip(key, result))
        res = json.dumps(res)
        return res
    except:
        db.close_connect()
        return "fail"

@app.route("/stationSearch_byStationID",methods=["POST"])
def search_byStationID():
    '''
    通过ID查找
    :return:
    '''
    try:
        # 这个写的有一些冗余，但是应该没没啥大问题
        print("查询某个Id站台相应的信息")
        StationID = request.form.get("StationID")
        result = db.get_api_case("*", "StationInfo", "StationID", StationID)

        key = ["地区", "站点", "longtitude", "latitude,", "magndata", "magnupdate", "sounddata", "soundupdate"]
        if result == 0:
            return json.dumps({"statment": "未找到"})

        res = dict(zip(key, list(result)))
        res = json.dumps(res)
        return res
    except:
        db.close_connect()
        return "fail"

@app.route("/stationSearch_byLcoTitude",methods=["POST"])
def search_byLcoTitude():
    '''
    通过给定值返回数据
    :return:
    '''
    try:
        print("StationInfo，通过给予的部分信息返回一列")
        column_title = request.form.get("column_title")
        print(column_title)
        coulmn_value = request.form.get("column_value")

        result = db.get_api_case("*", "StationInfo", column_title, coulmn_value)
        if result == 0:
            return json.dumps({"statment": "未找到"})
        key = ["地区", "站点", "longtitude", "latitude,", "magndata", "magnupdate", "sounddata", "soundupdate"]
        print("67", result)
        res = dict(zip(key, list(result)))
        res = json.dumps(res)
        return res
    except:
        db.close_connect()
        return "fail"

@app.route("/stationSearch_byLimit",methods=["POST"])
def search_byLimit():
    '''给定值的范围查询'''
    try:
        targe = request.form.get("targe")
        column_title = request.form.get("column_title")
        lim_scope = request.form.get("lim_scope")
        print("已经获取到用户的数据")
        result = db.get_scope_data("StationInfo", targe, column_title, lim_scope)
        print("查询完毕56")
        if result == 0:
            return json.dumps({"statment": "未找到"})
        # key=["地区","站点","longtitude","latitude,","magndata","magnupdate","sounddata","soundupdate"]
        print("67", result)
        # result=list(result[0])
        resultlist = []
        for i in result:
            print(i)
            resultlist.append(i[0])

        key = list(range(0, len(resultlist)))
        # print(result)
        # print(len(result))
        res = dict(zip(key, resultlist))
        res = json.dumps(res)
        return res
    except:
        db.close_connect()
        return "fail"

if __name__=='__main__':
    app.run(debug=True, port=5000, host="localhost")
    CORS(app)






