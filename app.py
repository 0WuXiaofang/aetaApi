from flask import Flask, request
from flask_cors import  CORS
from dbConnect import *
from utils.db_handle import *
from werkzeug.utils import redirect
import pymysql
import json
from utils.jsonfyDbtable import *
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='gasound')
# dbname = "gasound"
# print("连接成功")
#
# cursor = db.cursor()
# connectdb()
db=DB()
dbname="gasound"
jsfy=jsonfyDbtable()

def file(dbname,tablename):
    try:
        print(dbname)
        selecthead = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA =" + "'" + dbname + "'" + " AND TABLE_NAME = " + "'" + tablename + "'" + ";"
        print("selecthead",selecthead)
        head = db.cur.execute(selecthead)
        print("head",head)
        heads = db.cur.fetchall()
        print(heads)
        # 查询对应的值
        vItems = []
        for headtitle in heads:
            headtitle = str(headtitle[0])

            selectvalue = "select " + headtitle + " FROM " + tablename + ";"
            # print(selectvalue)
            db.cur.execute(selectvalue)
            selectvalues = db.cur.fetchall()

        # 遍历然后变为一个list
        #
        # print(selectvalues)
            vItem = []
            for v in selectvalues:
                vItem.append(v[0])
            vItems.append(vItem)
        # print("值列表",vItems)
        return (heads, vItems)
        #     查询语句，表头
        # pp=file(dbname,tablename)
        # print(pp[1])
    except:
        # 发生错误时回滚
        db.close_connect()
        return 'fail'




# dbselctAllt("tab_24_magn")
def get_allTable_data(tableClass):

    print(tableClass)
    print(type(tableClass))
    allTableName=db.get_all_tablename("gasound")
    print("allTableName",allTableName)
    sound_key=["StationID","sound_var","sound_abs_max","sound_abs_mean","sound_abs_max_top5p","sound_mean"]
    magn_key=["StationID","magn_var","magn_kurt","magn_abs_max","magn_abs_mean","magn_abs_max_top5p","magn_variance_frequency"]
    # 判断给的是那种数据
    dataList=[]
    emTable_dataList=[]
    gaTable_titleList=[]
    emTable_titleList=[]
    gaTable_dataList=[]
    if tableClass=="em":
        # em为地磁
        for i in allTableName:
            if "magn" in i:
                emTable_titleList.append(i)
                data=getTabe_data(i,magn_key)
                # print("data\n",data)
                for everData in data:
                    emTable_dataList.append(everData)
            else:
                continue
        print("len",len(emTable_dataList))
        result=jsfy.jsonfy(magn_key,emTable_dataList)
        print("result\n",result)

        return result

    elif tableClass=="ga":
        # ga为地声
        for i in allTableName:
            if "sound" in i:
                gaTable_titleList.append(i)
                data=getTabe_data(i,sound_key)
                # print("data\n",data)
                for everData in data:
                    gaTable_dataList.append(everData)
            #         化为一维
            else:
                continue
        print("len",len(gaTable_dataList))
        result=jsfy.jsonfy(sound_key,gaTable_dataList)
        print("\n,\n,",result)
        return result

    else:
        print("啥也不是")
        return (json.dumps({"message":"其他暂不提供"}))


app = Flask(__name__)

CORS(app, resources=r'/*')

@app.route("/get_allTable_name", methods=["GET"])
def get_allTable_name():
    # tablename = request.form.get("tableNames")
    result=db.get_all_tablename("gasound")
    return jsfy.l1_tol1(range(0,len(result)),result)
# @app.route("/get_allTable_data", methods=["GET"])
# def get_allTable_messageApi():
#         tableClass=request.args.get("tableClass")
#         return get_allTable_data(tableClass)


@app.route("/optData", methods=["POST"])
def optData():
    print("test")
    return "1111"
# 接口不通的时候跑一下
def getTabe_data(tablename,targ_key):
    '''
    :return:
    '''
    # 对targ key处理
    targ_keyStr = ','.join(targ_key)
    # print("116", targ_keyStr)
    data=db.get_tragColumn_data_list(targ_keyStr,tablename)

    # print("result",result)
    return data




@app.route("/tablename/get_table_data", methods=["GET"])

def get_table_data():
    resultList=[]
    tableNames = request.args.get("tableName")
    tableClass=request.args.get("tableClass")
    sound_key=["StationID","sound_var","sound_abs_max","sound_abs_mean","sound_abs_max_top5p","sound_mean"]
    magn_key=["StationID","magn_var","magn_kurt","magn_abs_max","magn_abs_mean","magn_abs_max_top5p","magn_variance_frequency"]
    # 判断给的是那种数据
    if tableClass=="em":
        # em为地磁
        data=getTabe_data(tableNames,magn_key)
        for i in data:
            result=jsfy.jsonfy(magn_key,i)
            resultList.append(result)

        return data
    elif tableClass=="ga":
        # ga为地声
        data=getTabe_data(tableNames,sound_key)
        print("151data",data)
        result=jsfy.jsonfy(sound_key,data)
        return result
    else:
        return "default tableclass error"

# try:
    #     tableNames = request.args.get("tableName")
    #     tableClass=request.args.get("tableClass")
    #     sound_key=["StationID","sound_var","sound_abs_max","sound_abs_mean","sound_abs_max_top5p","sound_mean"]
    #     magn_key=["StationID","magn_var","magn_kurt","magn_abs_max","magn_abs_mean","magn_abs_max_top5p","magn_variance_frequency"]
    #     # 判断给的是那种数据
    #     if tableClass=="em":
    #         # em为地磁
    #         data=getTabe_data(tableNames,magn_key)
    #         result=jsfy.jsonfy(magn_key,data)
    #         return result
    #     elif tableClass=="ga":
    #         # ga为地声
    #         data=getTabe_data(tableNames,sound_key)
    #         print("151data",data)
    #         result=jsfy.jsonfy(sound_key,data)
    #         return result
    #     else:
    #         return "default tableclass error"
    #
    #     # try:
    #
    #             # table_data = db.get_api_list(tableNames)
    #     # new一个格式化jason对象
    #     # jsfy = jsonfyDbtable()
    #     # tableNames = jsfy.jsonfy(range(0, len(table_data)), table_data)
    #     # print(range(0, len(tableNames)))
    #     # print(tableNames)
    #     # return tableNames
    # except:
    #     db.close_connect()
    #     return "fail"

if __name__=='__main__':
    app.run(debug=True, port=5555, host="localhost")
    CORS(app)
