# 关于地震部分数据查询，从地震目录查询
from flask import Flask, request
from werkzeug.utils import redirect
from flask_cors import  CORS
#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
from utils.jsonfyDbtable import *
from utils.db_handle import *
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

# 判断表的类型进行数据的读出，表名的读出：
def define_EmoGm_tableData(emorgm,tablenameList):
    pass
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

@api.route('/searchinfo',methods=["POST"])
def searchEqlisInfo():

    print("开始执行模糊查询")
    tablename=request.form.get("tablename")
    key_word=request.form.get("key_word")
    alike_data=request.form.get("alike_data")
    result=db.alike_get_data(tablename, key_word,alike_data)
    print("result",result)
    # 还需要表头的数据做key
    key=db.get_tbColTitle_data("gasound","eqlst")
    print("key",key)

    keyStr = ','.join(key)
    print("122", keyStr)
    result = jsfy.jsonfy(key, result)

    print(result)
    if result==0 or len(result)==0:
        return json.dumps({"statment":"未找到信息"})
    # key=list(range(0,len(result)))
    return result
# def emLand_location(area):
#
#
#
#     pass
# def gaLand_location(area):
#     pass
def land_location(area,class_gaOrem):
    """
    对地震通过经纬度进行划分，划分为8个地震带
    :param longtitude:
    :param latitude:
    :return:
    """
    # 经纬度划分地带
    # 区域分类，id为观测站id，range为经纬度范围，分别是左上角和右下角经纬度
    area=int(area)
    area_groups = [
        {'id': set([133, 246, 119, 122, 59, 127]), 'range': [30, 34, 98, 101]},
        {'id': set(
            [128, 129, 19, 26, 159, 167, 170, 182, 310, 184, 188, 189, 191, 197, 201, 204, 88, 90, 91, 93, 94, 221, 223,
             98,
             107, 235, 236, 252, 250, 124, 125]), 'range': [30, 34, 101, 104]},
        {'id': set([141, 150, 166, 169, 43, 172, 183, 198, 202, 60241, 212, 214, 99, 228, 238, 115, 116, 121, 251]),
         'range': [30, 34, 104, 107]},
        {'id': set([131, 36, 164, 165, 231, 60139, 174, 175, 206, 303, 82, 51, 243, 55, 308, 119, 313, 318]),
         'range': [26, 30, 98, 101]},
        {'id': set(
            [256, 130, 132, 147, 148, 149, 151, 153, 32, 33, 35, 60195, 38, 39, 41, 302, 304, 177, 305, 307, 181, 309,
             314,
             315, 316, 317, 319, 320, 193, 322, 200, 73, 329, 75, 333, 78, 334, 84, 87, 60251, 96, 225, 101, 229, 105,
             109,
             40047, 240, 247, 120, 254, 255]), 'range': [26, 30, 101, 104]},
        {'id': set([352, 321, 355, 324, 326, 328, 331, 77, 47, 48, 335, 339]), 'range': [26, 30, 104, 107]},
        {'id': set([161, 226, 137, 138, 171, 140, 113, 306, 152, 186, 220, 60157]), 'range': [22, 26, 98, 101]},
        {'id': set([50117, 327, 106, 332, 142, 146, 24, 155, 156, 29]), 'range': [22, 26, 101, 104]}
    ]

    #
    # max_mag = -1
    # eq_area = -1
    # 做地区分类
    # try:

    # except:
    #     db.close_connect()
    #     return "fail"
    LocationData=[]
    mapData_list=[]
    sid = area_groups[area]['id']
    print(sid)
    key_ga=["StationID","sound_var","sound_abs_max","sound_abs_mean","sound_abs_max_top5p","sound_mean"]
    key_em=["StationID","magn_var","magn_kurt","magn_abs_max","magn_abs_mean","magn_abs_max_top5p","magn_variance_frequency"]
    # em_list = []
    # ga_list = []
    for id_num in sid:
        # table_list = db.get_all_tablename("gasound")
        # print("读取数据库所有的表名成功",table_list)
        # 读取相应的表的信息并且关键字为StationID
        if class_gaOrem=="em":
            # print("len",len(emTable_dataList))
            locm_tablename = "tab_%s_magn" % id_num
            data=getTabe_data(locm_tablename,key_em)
            for everData in data:
                mapData_list.append(everData)

        # return result
        elif class_gaOrem=="ga":
            locs_tablename = "tab_%s_sound" % id_num
            data=getTabe_data(locs_tablename,key_ga)
            for everData in data:
                mapData_list.append(everData)
        else:
            print("不属于这个范围")

            continue
    # print("这个是站点信息magn:",em_list)
        # try:

        # except:
        #     print("站点没在这个范围内部\n", )
        #     continue
    # for mapData in mapData_list:
    #     LocationData.append(mapData)

    if class_gaOrem=="em":
        print(mapData_list)
        result=jsfy.jsonfy(key_em,mapData_list)
        return result
    elif class_gaOrem=="ga":
        result=jsfy.jsonfy(key_ga,mapData_list)
        return result
    else:
        return json.dumps({"statement":200})



def seismicL_classify(magnitude):
    '''
    地震级别分类
    :return:
    '''
    try:

        print("地震级别开始分类")
        if magnitude > 0 and magnitude < 3.4:
            print("0~3.4")
            result = db.get_scope_data("eqlst", "*", "Magnitude", "<=3.4")
            return result
        elif magnitude >= 3.4 and magnitude <= 4.5:
            print("3.4~4.5")
            result = db.get_youDefine_fondata("eqlst", "*", "Magnitude>=3.6 && Magnitude<=4.5")
            return result
        elif magnitude >= 4.6 and magnitude <= 5.5:
            print("4.6~5.5")
            result = db.get_youDefine_fondata("eqlst", "*", "Magnitude>=4.6 && Magnitude<=5.5")
            return result
        elif magnitude >= 5.6 and magnitude < 8.0:
            print("5.6~8.0")
            result = db.get_youDefine_fondata("eqlst", "*", "Magnitude>=5.6 && Magnitude<=8.0")
            return result
    except:
        db.close_connect()
        return "fail"


# searchEqlisInfo()
@api.route("/classify_magnitude", methods=["POST"])
def classify_magnitude():
    try:
        magnitude = request.form.get("magnitude")
        print("地震级别", magnitude)
        #     调用函数对数据进行分类
        magnitude = float(magnitude)
        result = seismicL_classify(magnitude)
        key = db.get_tbColTitle_data("gasound","eqlst")
        print("key",key)

        print("地震等级分类，处理完毕", result)
        if result == 0:
            return json.dumps({"statment": "未找到第%s地震相关信息" % magnitude})

        res = jsfy.jsonfy(key,result)
        return res
    except:
        db.close_connect()
        return json.dumps({"statment": "程序执行中断" })


#
# def gettablename():
#     print("hhhhhhhhhhh")
#     return "agagag"
@api.route("/location_classify",methods=["GET"])
def location_classify():
    '''
    进行经纬度地域划分
    使用模糊查询
    :return:
    '''
    print("开始执行地区影响因子查询")
    area=request.args.get("area")
    print(area,"area")
    # 获取是em还是gm
    class_gaOrem=request.args.get("em_or_gm")
    # 从表名塔台id，来决定地区经纬度
    result=land_location(area,class_gaOrem)
    # print(result)
    if result==0:
        return json.dumps({"statment":"未找到信息"})
    print("你正在查看指定塔台地区划分预测所有影响因子")
    return result
def ealst_locClassify():
    '''
    地震目录，地区分化
    :return:
    '''
    # 需要实现分页查询
    # 全部表

    # 需要对指定列进行返回
    #





    # sqlStr="Select count(week), max(Magnitude) from eqlst ,Group by Location"
    pass






