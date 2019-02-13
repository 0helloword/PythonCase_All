# -*- coding: UTF-8 -*-

import MySQLdb
import os,sys
from sshtunnel import SSHTunnelForwarder
	 
with SSHTunnelForwarder(
            ('123.57.234.78', 22),
            ssh_password = "&pb$XhqPdrqA",
            ssh_username = "checklog",
            remote_bind_address=('rdsen555btj41b8e4iy3.mysql.rds.aliyuncs.com', 3306)) as server:
         
    db = MySQLdb.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user = 'wk_db_rw',
                               passwd = 'cSdh1ahYqzE0',
                               db = 'saas_loan',
							   charset='utf8')	 
# 打开数据库连接
#db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM wk_customer_extend WHERE customerId = '%d'" % (114743722)

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()