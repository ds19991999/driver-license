#!/usr/bin/python3
# -*- coding:utf-8 -*-
from MySQLdb import *

class MySQLHelp(object):
	"""docstring for MySQLHelp"""
	def __init__(self, host, db, user, passwd, port=3306, charset='utf8', unix_socket='/tmp/mysql.sock'):
		super(MySQLHelp, self).__init__()
		self.host=host
		self.port=port
		self.db=db
		self.user=user
		self.passwd=passwd
		self.charset=charset
		self.unix_socket=unix_socket
	def open(self):
		self.conn=connect(host=self.host,db=self.db,user=self.user,passwd=self.passwd,port=self.port,charset=self.charset,unix_socket=self.unix_socket)
		self.cursor=self.conn.cursor()
	def close(self):
		self.cursor.close()
		self.conn.close()

	def cud(self,sql,params):
		try:
			self.open()
			self.cursor.execute(sql,params)
			self.conn.commit()
			self.close()
			print("ok")
		except Exception as e:
			print(e)

	def all(self,sql,params=[]):
		try:
			self.open()
			self.cursor.execute(sql,params)
			result = self.cursor.fetchall()
			self.close()
			return result
		except Exception as e:
			print(e)
	def one(self,sql,params=[]):
		try:
			self.open()
			self.cursor.execute(sql,params)
			result=self.cursor.fetchone()
			self.close()
			return result
		except Exception as msg:
			print(msg)
