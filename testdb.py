from utils.db_handle import DB
# from action.get_rely import GetRely
# from utils.HttpClient import HttpClient
def main():
    # 连接数据库，获取连接实例对象
    db = DB()
    # 从数据库中获取需要执行的api执行集合
    api_list = db.get_api_list("tab_19_magn")
    print(api_list)
main()