# 1. 连接 Mysql 数据库
import os
import pymysql
# import pandas as pd
import pandas as pd

# import numpy

# try:

# except:
#     print('数据库连接失败！')
conn = pymysql.connect(host='49.234.155.190',port=3306, user='root', password='123456', db='gasound', charset='utf8')
cur = conn.cursor()
print('数据库连接成功！')
print(' ')
path = os.getcwd()
files = os.listdir(path)
print(files)
for file in files:
  print("wenjian",file)
  if file.split('.')[-1] in ['csv']:
      print(file)
      filename = file.split('.')[0]
      filename = 'tab_' + filename
      print(filename)
      f = pd.read_csv(file, encoding='gbk')
      print(f)
      f.fillna(f.mean(),inplace=True)
      print(f)
      columns = f.columns.tolist()

      field = []  # 用来接收字段名称的列表
      table = []  # 用来接收字段名称和字段类型的列表
      types = f.dtypes
      print(types)
      for col in columns:
          if 'int' in str(f[col].dtype):
              char = col + ' INT'
          elif 'float' in str(f[col].dtype):
              char = col + ' FLOAT'
          elif 'object' in str(f[col].dtype):
              char = col + ' VARCHAR(255)'
          elif 'datetime' in str(f[col].dtype):
              char = col + ' DATETIME'
          else:
              char = col + ' VARCHAR(255)'

          table.append(char.replace("@","_"))
          col=col.replace("@","_")

          field.append(col)




      tables = ','.join(table)
      print("66",field)
      # field

      fields = ','.join(field)


      print("单个表头",tables)

      print("内容",fields)
      ##id0 int PRIMARY KEY NOT NULL auto_increment 是创建的一个自增主键，之所以取名为 id0 而不取名 id ，是为了避免与 CSV 文件本来就有的 id 字段而出现冲突。
      table_sql = 'CREATE TABLE IF NOT EXISTS ' + filename + '(' + 'id int not null auto_increment primary key,' + tables + ')' + 'ENGINE=MyISAM DEFAULT CHARSET=utf8;'
      print(table_sql)
    #开始创建
      print("开始创建表")
      #创建游标
      # cursor = conn.cursor()
      print(table_sql)
      cur.execute(table_sql)
      #执行创建表
      conn.commit()
      print("创建完成")
      s = ','.join(['%s' for _ in range(len(f.columns))])
      print(s)
      values = f.values.tolist()
      print("values",values)
      ##executemany()就是将列表中的元素一个个取出来，然后一条条的执行，也就是说它能同时执行多条语句。执行同样多的语句可比execute()快很多。
      insert_sql = 'insert into {}({}) values({})'.format(filename, fields, s)
      s=""
      print(insert_sql)
      # cur.executemany(insert_sql, values)
      p=0
      for i in values:
          p+=1
          cur.execute(insert_sql, i)

          print("第",p)

      print("表"+filename+"创建成功")
      conn.commit()
      # print('任务完成！共导入 {} 个CSV文件。'.format(i))


# import os
# print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
# print("PATH:", os.environ.get('PATH'))
