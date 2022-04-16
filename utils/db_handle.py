import datetime

import pymysql
from utils.config_handler import ConfigParse


class DB(object):
    def __init__(self):
        # 获取mysqldb名字
        # self.dbname=self.db_conf["db"]
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
        dbname=self.db_conf["db"]
        print("数据库名",dbname)

    def close_connect(self):

        # 关闭数据连接
        # 提交，物理存储
        self.conn.commit()
        # 游标关闭
        self.cur.close()
        # 连接对象关闭
        self.conn.close()

    def get_api_list(self,dbtablename):
        """获取一个表所有的对象数据"""
        sqlStr = "select * from %s"%dbtablename
        self.cur.execute(sqlStr)
        data = self.cur.fetchall()
        # 转成一个list
        apiList = list(data)
        return apiList

    # def get_api_case(self,dbtablename, targ):
    #     """获取某一条数据"""
    #     sqlStr = "select * from %s where id=%s" % (dbtablename,targ)
    #     self.cur.execute(sqlStr)
    #     api_case_list = list(self.cur.fetchall())
    #     return api_case_list

    def get_rely_data(self, col_data, dbtablename,limit_item,limit_data):
        """获取所有数据库中的某一条限定相关数据"""
        sqlStr = "select %s from %s where %s=%s " % (col_data,dbtablename,limit_item,limit_data)
        self.cur.execute(sqlStr)
        rely_data = eval(self.cur.fetchall()[0][0])
        return rely_data

    def write_check_result(self,error_item,errorInfo,resitem, res_data, case_id):
        """更新数据库表"""
        # sqlStr = "update  set error_info=\"%s\", res_data=\"%s\" where id=%s" % (
        # errorInfo, res_data, case_id)
        sqlStr = "update  set %s=\"%s\", %s=\"%s\" where id=%s" % (
        error_item,errorInfo,resitem, res_data, case_id)
        self.cur.execute(sqlStr)
        self.conn.commit()

    def insert_dab(self,dbtablename,insert_values):
        sqlStr = "INSERT INTO %s VALUES %s"%(dbtablename,insert_values)
        print("数据库管理员正在插入数据\n",sqlStr)
        self.cur.execute(sqlStr)
        print("插入完成")
        self.conn.commit()
        # self.close_connect()
    def get_titleTarg_search(self,dbtablename,select_data):
        '''
        寻找指定表头数据的值
        :param dbtablename:
        :param select_data:
        :return:
        '''
        sqlStr="select id, isdeny, islogin, password, user_name from eta_user where user_name='aFang'"
        print("数据库管理员正在查找数据\n",sqlStr)
        self.cur.execute(sqlStr)
        if self.cur.execute(sqlStr)==0:
            return 0
        else:
            print(self.cur.execute(sqlStr))
            res = list(self.cur.fetchall())
            print("模糊查询完毕")
            print("res",res)
            return res



        return search_res
    def get_api_id(self, dbtablename,id):
        """获取表中id"""
        sqlStr = "select * from %s where id=%s" %(dbtablename,id)
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

    def get_api_case(self,targ,dbtablename,column_title,column_value):
        """获取表中指定数据"""
        sqlStr = "select %s from %s where %s='%s'" % (targ,dbtablename,column_title,column_value)
        print("found",sqlStr)
        self.cur.execute(sqlStr)
        if self.cur.execute(sqlStr)==0:
            return 0
        else:

            print(self.cur.execute(sqlStr))
            res=list(self.cur.fetchone())
            print("res",res)
            return res
    def get_api_idNum(self,dbtablename,id_value):
        """获取表中id"""
        sqlStr = "select * from %s where id='%d'" % (dbtablename,id_value)
        print("found\n",sqlStr)
        self.cur.execute(sqlStr)
        api_id = self.cur.fetchall()[0][0]
        return api_id
    def alike_get_data(self,dbtablename,keyword,alike_data):
        print("开始模糊查询")
        # 对某一数据进行关键字段模糊查询
        sqlStr = "select * from "+dbtablename+" WHERE " + keyword + " LIKE '%"+alike_data+"%'"
        print("模糊",sqlStr)
        self.cur.execute(sqlStr)
        if self.cur.execute(sqlStr)==0:
            return 0
        else:
            print(self.cur.execute(sqlStr))
            res = list(self.cur.fetchall())
            print("模糊查询完毕")
            print("res",res)
            return res

    # 进行某个范围的值查询
    def get_scope_data(self,dbtablename,targ_data,column_title,lim_scope):
        print("开始对%s范围进行数据的查询"%lim_scope)
        sqlStr = "select "+targ_data+" from "+dbtablename+" WHERE " + column_title + lim_scope
        # print("范围查询语句",sqlStr)
        self.cur.execute(sqlStr)
        if self.cur.execute(sqlStr)==0:
            return 0
        else:
            print(self.cur.execute(sqlStr))
            res = list(self.cur.fetchall())
            print("范围查询完毕")
            print("res",res)
            return res


    # 获取单个数据库指定表表头
    def get_tbColTitle_data(self,dbname,dbtablename):
        # self.cur.close()

        print("开始对%s表进行表头的查询"%dbtablename)
        sqlStr = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '%s' AND TABLE_NAME = '%s'"%(dbname,dbtablename)
        print("范围查询语句",sqlStr)
        self.cur.execute(sqlStr)
        get_tbColTitle_data=list(self.cur.fetchall())
        print("表头查询完毕")
        print("biaotou1",get_tbColTitle_data)
        res=[]
        for i in get_tbColTitle_data:
            # print(i)
            res.append(i[0])
        print("打印数据",res)

        return res


    def get_all_tablename(self,dbname):
        print("开始查询所有数据库的表名")
        sqlStr="SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '%s'"%dbname
        # print("查询表名语句",sqlStr)
        self.cur.execute(sqlStr)
        get_all_tablename=list(self.cur.fetchone())
        # get_all_tablename[0] for get_all_tablename in self.cursor.fetchall()
        print("查询数据表完毕")
        return get_all_tablename

    def update_store_data(self,dbtablename,column_title,set_value ,id):
        # 修改某个指定数据的值

        sqlStr = "select %s from %s where id=%s" % (column_title, dbtablename,id)
        self.cur.execute(sqlStr)
        if self.cur.fetchall():
            sqlStr = "update %s set %s=\"%s\" where id=%s" % (dbtablename,column_title,set_value ,id)
            print(sqlStr)
            self.cur.execute(sqlStr)
            self.conn.commit()
        else:
            # 可能写的有错误
            sqlStr = "insert into %s values(%s, %s)" % (dbtablename, datetime.now())
            self.cur.execute(sqlStr)
            self.conn.commit()
    def error_rollback(self):
        '''
        发生错误时候回滚并且关闭连接及游标
        :return:
        '''
        self.conn.rollback()
        self.close_connect()
    # def create_table(self,tablename):
    #     '''
    #     创建一个表
    #     :param tablename:
    #     :return:
    #     '''
    #     table_sql = 'CREATE TABLE IF NOT EXISTS ' + filename + '(' + 'id int not null auto_increment primary key,' + tables + ')' + 'ENGINE=MyISAM DEFAULT CHARSET=utf8;'
    #     print(table_sql)
    #     # 开始创建
    #     print("开始创建表")
    #     # 创建游标
    #     # cursor = conn.cursor()
    #     print(table_sql)
    #     cur.execute(table_sql)
    #     # 执行创建表
    #     conn.commit()
    #     print("创建完成")



if __name__ == '__main__':
    db = DB()
    print("测试一下")
    # 获取全部的数据
    # print(db.get_api_list("tab_19_magn"))
    # 获取某一个部分的数据
    # print(db.get_api_case("tab_19_magn",6))
    # print(db.alike_get_data("eqlst","Location","四川"))
    # print(db.get_scope_data("eqlst", "*", "Magnitude", "<8.0"))
    # print(db.get_all_tablename("gasound"))
    print("修改数据")
    print(db.update_store_data("eta_user",("user_id","user_name","password","islogin","isdeny"),(2,"xiaozhang","1234",0,1),2))

