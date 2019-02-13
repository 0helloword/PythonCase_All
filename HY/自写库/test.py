# -*- coding: utf-8 -*-

import MySQLdb
import os,sys
from sshtunnel import SSHTunnelForwarder


def test(): 
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
        insert ="UPDATE wk_tradepwd_log set createTime='2018-01-03 11:00:14' where customerId='114743848' and status =0 and proId='ad51b7d5c65a7xjs89x97c3454545cad' and type=3"
        cursor.execute(insert)

	return 1
pass

if __name__ == "__main__":
	 pass