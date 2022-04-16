# 关于地震部分数据查询，从地震目录查询
from flask import Flask, request
from werkzeug.utils import redirect
from flask_cors import  CORS
#自己封装了一个，这个确实没啥用 from dbConnect import *
import pymysql
from utils.jsonfyDbtable import *
from utils.db_handle import *
import json
# 实例化数据库对象
db=DB()
jsfy=jsonfyDbtable()
# 去封装一个模糊查询
#调用模糊查询的方法
app = Flask(__name__)
@app.route('/searchinfo',methods=["POST"])
def searchEqlisInfo():

    print("开始执行模糊查询")
    tablename=request.form.get("tablename")
    key_word=request.form.get("key_word")
    alike_data=request.form.get("alike_data")
    result=db.alike_get_data(tablename, key_word,alike_data)

    print(result)
    if result==0:
        return json.dumps({"statment":"未找到信息"})
    key=list(range(0,len(result)))

    res=dict(zip(key,list(result)))
    res=json.dumps(res)
    return res
def land_location():
    """
    对地震通过经纬度进行划分，划分为8个地震带
    :param longtitude:
    :param latitude:
    :return:
    """
    # 经纬度划分地带
    # 区域分类，id为观测站id，range为经纬度范围，分别是左上角和右下角经纬度
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
    try:
        for area in (0, 1, 2, 3, 4, 5, 6, 7):
            sid = area_groups[area]['id']
            em_list = []
            for id_num in sid:
                try:
                    table_list = db.get_all_tablename("gasound")
                    # print("读取数据库所有的表名成功",table_list)
                    # 读取相应的表的信息并且关键字为StationID
                    locm_tablename = "tab_%s_magn" % id_num
                    print("loc——tablename", locm_tablename)
                    em_list.append(db.get_api_list(locm_tablename))
                    print("\n")
                    # print("这个是站点信息magn:",em_list)
                except:
                    print("站点没在这个范围内部\n", )
                    continue
            # em_data = pd.concat(em_list)
            # 对python的变量内存进行回收
            # del em_list
            ga_list = []
            for id_num in sid:
                try:
                    table_list = db.get_all_tablename("gasound")
                    # print("读取数据库所有的表名成功", table_list)
                    # 读取相应的表的信息并且关键字为StationID
                    locs_tablename = "tab_%s_sound" % id_num
                    ga_list.append(db.get_api_list(locs_tablename))

                    # print("获取到的划分数据sound",ga_list)
                except:
                    print("站点没在这个范围内部\n", )
                    continue
        # print("galist\n",ga_list)
        print("数据类型", type(ga_list))
        print("emlist\n", em_list)
        # return (em_list,ga_list)

        # return ("okk")
    except:
        db.close_connect()
        return "fail"


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
        if magnitude >= 3.4 and magnitude <= 4.5:
            print("3.4~4.5")
            result = db.get_scope_data("eqlst", "*", "Magnitude", "<=4.5")
            return result
        if magnitude >= 4.6 and magnitude <= 5.5:
            print("4.6~5.5")
            result = db.get_scope_data("eqlst", "*", "Magnitude", "<=5.5")
            return result
        if magnitude >= 5.6 and magnitude < 8.0:
            print("5.6~8.0")
            result = db.get_scope_data("eqlst", "*", "Magnitude", "<=8.0")
            return result
    except:
        db.close_connect()
        return "fail"


# searchEqlisInfo()
@app.route("/classify_magnitude", methods=["POST"])
def classify_magnitude():
    try:
        magnitude = request.form.get("magnitude")
        print("地震级别", magnitude)
        #     调用函数对数据进行分类
        magnitude = float(magnitude)
        result = seismicL_classify(magnitude)
        key = list(range(0, len(result)))
        print("地震等级分类，处理完毕", result)
        if result == 0:
            return json.dumps({"statment": "未找到第%s地震相关信息" % magnitude})

        res = dict(zip(key, list(result)))
        res = json.dumps(res)
        return res
    except:
        db.close_connect()
        return "fail"


#
# def gettablename():
#     print("hhhhhhhhhhh")
#     return "agagag"
@app.route("/location_classify",methods=["POST"])
def location_classify():
    '''
    进行经纬度地域划分
    使用模糊查询
    :return:
    '''

    # max_mag = -1
    # eq_area = -1
    # 不好写
    pass



    print("你正在查看地区划分预测所有影响因子")
    return land_location()
def ealst_locClassify():
    '''
    地震目录，地区分化
    :return:
    '''



    # sqlStr="Select count(week), max(Magnitude) from eqlst ,Group by Location"
    pass
if __name__=='__main__':
    app.run(debug=True, port=5000, host="localhost")
    CORS(app)





