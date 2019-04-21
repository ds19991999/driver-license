#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os,cv2
import tkinter as tk

from SQLHelper.MySQLHelper import MySQLHelp
from config import *
from Core import predict,find_license,Surface

conf = config()
mysql_ip = conf['mysql_ip']
mysql_database = conf['mysql_database']
mysql_user = conf['mysql_user']
mysql_passwd = conf['mysql_passwd']

def card_data(img):
    c = predict.CardPredictor()
    c.train_svm()
    r, roi, color = c.predict(img)
    province = r[0]
    card = ""
    for i in r[1:]:
        card += i
    return province,color,card

def check_card(card_temp):
	"""查询用户表"""
	sql='select province,color from card where card=%s'
	params=[card_temp]
	helper=MySQLHelp(mysql_ip,mysql_database,mysql_user,mysql_passwd)
	result=helper.all(sql,params)
	return result

def save_to_mysql(province_temp,color_temp,card_temp):
    sql = 'insert into card(province,color,card) values(%s,%s,%s)'
    params = [province_temp,color_temp,card_temp]
    helper = MySQLHelp(mysql_ip, mysql_database, mysql_user, mysql_passwd)
    helper.cud(sql, params)

def find_pos(img_temp):
	orgimg = cv2.imread(img_temp)
	rect, img = find_license.find_license(orgimg)
	cv2.rectangle(img, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
	cv2.imshow('img', img)
	print("输入0退出窗口！")
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def win_surface():
	def close_window():
	    print("destroy")
	    if surface.thread_run:
	        surface.thread_run = False
	        surface.thread.join(2.0)
	    win.destroy()	
	win = tk.Tk()
	surface = Surface.Surface(win)  # 新建一个自定义类Surface（在本文件内定义），作用有窗口的初始化和功能的定义
	win.protocol('WM_DELETE_WINDOW', close_window)  # 定义窗口关闭事件
	win.mainloop()  # 进入窗口消息循环

def print_license(img_temp):
    province,color,card = card_data(img_temp)
    result = check_card(card)
    if len(result) == 0:
        print("该车未注册！请先到网站注册！")
        save_to_mysql(province,color,card)
    else:
        print("存在该车，允许通行！")
        print("省份：%s"%(province))
        print("颜色：%s"%(color))
        print("车牌号：%s"%(card))

def print_menu():
	print("欢迎进入车牌识别系统v0.01")
	print("-"*25)
	print("0"+"-"*10+"显示菜单"+"-"*10)
	print("1"+"-"*10+"定位车牌"+"-"*10)
	print("2"+"-"*10+"打印车牌"+"-"*10)
	print("3"+"-"*10+"窗口程序"+"-"*10)
	print("4"+"-"*10+"退出系统")

def main():
	img = "Core/Test/car.jpg"
	print_menu()
	while True:
		try:
			i = int(input("请输入操作符："))
			if i == 0:
				os.system("clear")
				print_menu()
			elif i == 1:
				find_pos(img)
			elif i == 2:
				print_license(img)
			elif i == 3:
				win_surface()
			elif i == 4:
				os.system("clear")
				os.system(exit())
		except Exception:
			os.system("clear")
			print_menu()
			print("输入错误!")
	print("成功退出系统！")

if __name__ == '__main__':
	main()	
	