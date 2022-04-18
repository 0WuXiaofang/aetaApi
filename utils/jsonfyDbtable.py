# 将我查询到的数据表数据类型转换拿为json
import json
import numpy as np
class jsonfyDbtable(object):
    # def __init__(self):

    def jsonfy(self,key_data,twoDim_array):
    # #获取已经处理好的数据

        '''将数据转为json
        '''
        try:
            list_json=[dict(zip(key_data,item)) for item in twoDim_array]
            # indent缩进量，ensure_ascii=False支持中文
            str_json=json.dumps(list_json,indent=2, ensure_ascii=False)
            print(str_json)
            return str_json
        except:
            return "jsonfy_error"

    def l1_tol1(self ,key_data ,value_data):
        '''
        一维key和一维list转化为json
        :param key_data:
        :param twoDim_array:
        :return:
        '''
        try:
            list_json = [dict(zip(key_data, value_data))]
            # indent缩进量，ensure_ascii=False支持中文
            str_json = json.dumps(list_json, indent=2, ensure_ascii=False)
            print(str_json)
            return str_json
        except:
            return "jsonfy_error"
    # def json_inArray(self,key_data,value_data):
    #     '''
    #     装着json数组的array
    #     :param key_data:
    #     :param value_data:
    #     :return:
    #     '''




if __name__ == '__main__':
    jsfy=jsonfyDbtable()
    print("测试")
    key=[1,2,3,4]
    testdata=[('101.39', '27.92', '3.9', '2016-12-25 07:26:06', '1482621966', '12', '四川凉山州木里县'),
              ('104.72', '28.16', '4.2', '2017-01-15 18:05:35', '1484474735', '15', '四川宜宾市珙县'),
              ('104.73', '28.14', '3.7', '2017-01-15 19:20:53', '1484479253', '15', '四川宜宾市筠连县')]
    jsfy.jsonfy(key,testdata)
    key1=["地区","站点","longtitude","latitude,","magndata","magnupdate","sounddata","soundupdate"]
    data=['四川冕宁漫水湾', '181', '102.167771', '28.208206', 'True', 'True', 'True', 'True']
    jsfy.l1_tol1(key1,data)














