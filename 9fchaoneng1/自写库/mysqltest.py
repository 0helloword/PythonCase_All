# -*- coding: utf-8 -*-

import MySQLdb
import os,sys
from sshtunnel import SSHTunnelForwarder


def mysql_test(sql): 
    with SSHTunnelForwarder(
            ('123.57.56.45', 22),
            ssh_password="1Glij0i8",
            ssh_username="cntest",
            remote_bind_address=('rdsen555btj41b8e4iy3.mysql.rds.aliyuncs.com', 3306)) as server:
         
        conn = MySQLdb.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user='jf_cn',
                               passwd='Xe4P7PJb1a',
                               db='uat_jf_cn',
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