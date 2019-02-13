# -*- coding: utf-8 -*-

import MySQLdb
import os,sys
from sshtunnel import SSHTunnelForwarder


def mysql_operate(sql): 
	with SSHTunnelForwarder(
            ('123.57.234.78', 22),
            ssh_password = "&pb$XhqPdrqA",
            ssh_username = "checklog",
            remote_bind_address=('rdsen555btj41b8e4iy3.mysql.rds.aliyuncs.com', 3306)) as server:
         
		conn = MySQLdb.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user = 'wk_db_rw',
                               passwd = 'cSdh1ahYqzE0',
                               db = 'wildfire_loan',
							   charset='utf8')
		# 使用cursor()方法获取操作游标
		cursor = conn.cursor()
		try:
		# 执行SQL语句
			cursor.execute(sql)
        # 提交到数据库执行
			conn.commit()
		except:
		# 发生错误时回滚
			conn.rollback()
		# 关闭数据库连接
		conn.close()
pass

if __name__ == "__main__":
	pass