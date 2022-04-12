import pymysql
def connectdb():
    print("正在准备连接数据库")
    db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='gasound')
    dbname = "gasound"
    print("连接成功")
    cursor = db.cursor()


import datetime

import pymysql
from utils.config_handler import ConfigParse


class DB(object):
    def __init__(self):
        # 获取mysql连接信息
        self.db_conf = ConfigParse.get_db_config()
        # 获取连接对象
        self.conn = pymysql.connect(
            host=self.db_conf["host"],
            port=int(self.db_conf["port"]),
            user=self.db_conf["user"],
            password=self.db_conf["password"],
            database=self.db_conf["db"],
            charset="utf8"
        )
        # 获取数据的游标
        self.cur = self.conn.cursor()

    def close_connect(self):
        # 关闭数据连接
        # 提交，物理存储
        self.conn.commit()
        # 游标关闭
        self.cur.close()
        # 连接对象关闭
        self.conn.close()

    def get_api_list(self):
        """获取所有的对象数据"""
        sqlStr = "select * from interface_api where status=1"
        self.cur.execute(sqlStr)
        data = self.cur.fetchall()
        # 转成一个list
        apiList = list(data)
        return apiList

    def get_api_case(self, api_id):
        """获取某一条数据"""
        sqlStr = "select * from interface_test_case where api_id=%s and status=1" % api_id
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

    def get_rely_data(self, api_id, case_id):
        """获取所有数据库中的某一条"""
        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" % (api_id, case_id)
        self.cur.execute(sqlStr)
        rely_data = eval(self.cur.fetchall()[0][0])
        return rely_data

    def alike_get_data(self,dbtablename,keyword,alike_data):
        # 对某一数据进行关键字段模糊查询
        sqlStr = "select * from "+dbtablename+" WHERE" + keyword + " LIKE '%"+alike_data+"%'"
        self.cur.execute(sqlStr)
        alike_get_data = list(self.cur.fetchall())
        return alike_get_data

    def write_check_result(self, case_id, errorInfo, res_data):
        """更新数据库表"""
        sqlStr = "update interface_test_case set error_info=\"%s\", res_data=\"%s\" where id=%s" % (
        errorInfo, res_data, case_id)
        self.cur.execute(sqlStr)
        self.conn.commit()

    def insert_dab(self):
        sqlStr = "INSERT INTO `interface_api` VALUES (4, '修改博文', 'http://39.106.41.11:8080/getBlogContent/', 'get', 'url','0', '2018-07-27 22:13:30')"
        self.cur.execute(sqlStr)

    def get_api_case(self, api_id):
        """获取表中id"""
        sqlStr = "select * from interface_test_case where api_id=%s and status=1" % api_id
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

    def get_api_id(self, api_name):
        """获取表中id"""
        sqlStr = "select api_id from interface_api where api_name='%s'" % api_name
        self.cur.execute(sqlStr)
        api_id = self.cur.fetchall()[0][0]
        return api_id

    def update_store_data(self, api_id, case_id, store_data):

        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" % (api_id, case_id)
        self.cur.execute(sqlStr)
        if self.cur.fetchall():
            sqlStr = "update interface_data_store set data_store=\"%s\" where api_id=%s and case_id=%s" % (
                store_data, api_id, case_id)
            print(sqlStr)
            self.cur.execute(sqlStr)
            self.conn.commit()
        else:
            sqlStr = "insert into interface_data_store values(%s, %s, \"%s\", '%s')" % (
                api_id, case_id, store_data, datetime.now())
            self.cur.execute(sqlStr)
            self.conn.commit()


if __name__ == '__main__':
    db = DB()
    print(db.get_api_list())
    print(db.get_api_case(1))
    # print(db.get_rely_data(1,1))
    # print(db.insert_dab())