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

def dbselctAllt(tablename):
    # 函数返回值取参数，不是返回
    try:
        heads = file(dbname, tablename)[0]
        list_heads = []
        for i in heads:
            list_heads.append(i[0])
        # print("/n")
        # print("key",list_heads)
        # 列表是不是转json方便一些
        # 表名当json键，然后列值做jason值

        tablename = str(tablename)
        sqlall = "SELECT * FROM " + tablename + ";"
        print(sqlall)
        db.cur.execute(sqlall)
        result = db.cur.fetchall()
        result = str(result)
        # 变为json ，直接获取表头
        allResult = []

        # 写一个二维列表
        # list_heads=list(heads)
        # 好像不对
        list_values = file(dbname, tablename)[1]
        print("value", list_values)
        dict1 = dict(zip(list_heads, list_values))
        print(len(dict1))
        # dict1=jsonify(allResult)
        dballData = json.dumps(dict1)

        # db.close_connect()
        # return (result)
        return dballData
    except:
        # 发生错误时回滚
        db.close_connect()
        return 'fail'


# dbselctAllt("tab_24_magn")

app = Flask(__name__)

CORS(app, resources=r'/*')

@app.route("/get_allTable_data", methods=["POST"])
def allnum():
    tablename = request.form.get("tableNames")
    print("tablename",tablename)
    return dbselctAllt(tablename)
@app.route("/optData", methods=["POST"])
def optData():
    print("test")
    return "1111"
# 接口不通的时候跑一下

@app.route("/tablename/get_table_data", methods=["POST"])
def gettablename():
    try:
        tableNames = request.form.get("tablename")
        table_data = db.get_api_list(tableNames)
        # new一个格式化jason对象
        jsfy = jsonfyDbtable()
        tableNames = jsfy.jsonfy(range(0, len(table_data)), table_data)
        print(range(0, len(tableNames)))
        print(tableNames)
        return tableNames
    except:
        db.close_connect()
        return "fail"

if __name__=='__main__':
    app.run(debug=True, port=5555, host="localhost")
    CORS(app)
