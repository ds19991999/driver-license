#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
mysql> desc card;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int(11)     | NO   | PRI | NULL    | auto_increment |
| province | varchar(10) | YES  |     | NULL    |                |
| color    | varchar(10) | YES  |     | NULL    |                |
| card     | varchar(10) | YES  |     | NULL    |                |
| isdelete | bit(1)      | YES  |     | b'0'    |                |
+----------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
"""

def config():
    config = {
        'mysql_ip': 'localhost',
        'mysql_database': 'python3',
        'mysql_user': 'root',
        'mysql_passwd': 'passwd'
    }
    return config
