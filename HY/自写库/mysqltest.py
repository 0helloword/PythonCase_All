# -*- coding: utf-8 -*-

import MySQLdb
import os,sys
from sshtunnel import SSHTunnelForwarder


def mysql_test(sql): 
    with SSHTunnelForwarder(
            ('123.57.234.78', 22),
            ssh_password = "&pb$XhqPdrqA",
            ssh_username = "checklog",
            remote_bind_address=('rdsen555btj41b8e4iy3.mysql.rds.aliyuncs.com', 3306)) as server:
         
        conn = MySQLdb.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user = 'wk_db_rw',
                               passwd = 'cSdh1ahYqzE0',
                               db = 'saas_loan',
							   charset='utf8')
        cursor = conn.cursor()
        select = sql
        cursor.execute(select)
        data=cursor.fetchall()
	return data
pass

if __name__ == "__main__":
     #print(mysql_test())
	 pass