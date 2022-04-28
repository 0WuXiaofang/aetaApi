from flask_cors import CORS

from utils.jsonfyDbtable import *

from flask_cors import CORS, cross_origin


import numpy
# 注册
from flask import Flask, request
# from werkzeug.utils import redirect
from utils.db_handle import *
from libs.redprint import Redprint

api = Redprint('earthquakePredict')
#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
import json
# 实例化数据库对象
db=DB()
jsfy=jsonfyDbtable()


def userName_ishaving(userName):
    try:
        print("用户名存在验证")
        #     查询该用户是否存在
        print(userName)
        dbuserName = db.get_api_case("*", "eta_user", "user_name", userName)
        print("数据库用户", dbuserName)
        if dbuserName != 0:
            print("该用户存在")
            return True
        else:
            print("未找到用户")
            return False
        # 关闭数据库连接
    except:
        db.close_connect()
        return "fail"

def oldUser_passwordisR(input_username,inputPassword):
    try:
        res = db.get_api_case("password", "eta_user", "user_name", input_username)
        if res[0] == inputPassword:
            print(res[0])
            print("密码对~~~")
            return 1
        return 0
    except:
        db.close_connect()
        return "fail"

def userPassword_isRight(userName,passWord):
    # 核对密码是否正确
    try:
        print("用户密码验证")
        if userName_ishaving(userName) and oldUser_passwordisR(userName, passWord):
            print("密码输入对~")
            return 1
        else:
            return 0
    except:
        db.close_connect()
        return "fail"

def newrName_check(newerUserName):
    '''
    新用户验证名字是否重复
    :param newerUserName:
    :return:
    '''
    try:
        if userName_ishaving(newerUserName):
            #         如果是已经存在
            print("51用户已经存在")
            return False
        return "用户名当前无人注册"
    except:
        db.close_connect()
        return "fail"


def newerPassword_check(newerPassWord,newerPassWord_repeat):
    try:
        print("检查新用户两次输入是否一致")
        if newerPassWord == newerPassWord_repeat:
            print("两次输入一直，正确")
            return "用户输入密码正确"
        return False
    except:
        db.close_connect()
        return "fail"


def newerInfo_check(newerUserName,newerPassWord,newerPassWord_repeat):
    '''
    做新用户注册消息验证
    :param newerUserName:
    :param newerPassWord:
    :param newerPassWord_repeat:
    :return:
    '''

    try:
        if newrName_check(newerUserName) and newerPassword_check(newerPassWord, newerPassWord_repeat):
            #         执行数据库新用户增加操作
            print("可以增加一个新用户")
            insert_userValues = (0, newerUserName, newerPassWord, 1, 0)
            print("10555",insert_userValues)
            db.insert_dab("eta_user", str(insert_userValues))
            # 插入完后关闭数据库

            # db.close_connect()
            print("插入成功")
            result = json.dumps({"200": "新用户增加成功"})
            return result

        else:
            result = (newrName_check(newerUserName), newerPassword_check(newerPassWord, newerPassWord_repeat))
            result = jsfy.l1_tol1(["statement（false就是注册了）", "两次密码输入情况(false为两次输入不一致)"], result)
            print("重新注册")
            return result
    except:
        db.close_connect()
        return "fail"

@api.route("/user/login",methods=["POST"])
def user_login():
    try:
        print("用户登录")
        #     查询该用户是否存在
        userName = request.form.get("userName")
        passWord = request.form.get("passWord")
        if userPassword_isRight(userName, passWord):
            print("userLogin", 200)
            return json.dumps({"userLogin": 200})
        return json.dumps({"fault,输入错误": 500})
    except:
        db.error_rollback()
        return "fail"


@api.route("/user/register",methods=["POST"])
def user_register():
    try:
        print("用户注册")
        newerUserName = request.form.get("userName")
        newerPassWord = request.form.get("passWord")
        newerPassWord_repeat = request.form.get("passWord_repeat")
        rgistResult = newerInfo_check(newerUserName, newerPassWord, newerPassWord_repeat)
        if rgistResult == "新用户增加成功":
            return json.dump({"200": "注册成功"})
        else:
            print(type(rgistResult))
            return rgistResult
    except:
        db.close_connect()
        return "fail"




@api.route("/user/foundUserInfo",methods=["POST"])
def found_userInfo():
    try:
        targ_userData = request.form.get("targ_userData")
        targ_title = request.form.get("targ_title")
        print("查询用户讯息")
        search_data = db.get_api_case("*", "eta_user", targ_title, targ_userData)
        print("查询的讯息", search_data)
        print(len(search_data))
        # print(search_data[0])
        # 格式化
        # search_data=jsfy.jsonfy(targ_userData,search_data)
        if len(search_data) == 0:
            return json.dumps({targ_userData: "找不到"})
        else:
            key = db.get_tbColTitle_data("gasound", "eta_user")
            keyStr = ','.join(key)
            print("122", keyStr)
            result = jsfy.l1_tol1(key, search_data)
            print("125", result)
            return result
    except:
        db.close_connect()
        return "fail"

def update_userInfo(old):
    #展示没有修改用户信息的部分
    # 修改test
    pass











