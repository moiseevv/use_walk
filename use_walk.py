#! /usr/bin/env python3
path = r'D:\python all\bitrix_21\в работу  от 2022 11 12'
import os
def record_f(p,d,l):
	with open('log_use_walk.txt', 'a') as file:
		print(' *** Иследуем папку',file=file)
		print(p, file=file)
		print('       Найденые папки:  ',file=file)
		print(d, file=file)
		print('       Найденые файлы',file=file)
		print(l, file=file)

def walk(path):
	for p,d,l in os.walk(path):
		record_f(p,d,l)

walk(path)


