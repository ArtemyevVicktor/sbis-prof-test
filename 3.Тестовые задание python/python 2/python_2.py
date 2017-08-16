#python 3.5.2
# -*- encoding: utf-8 -*-
#author: Artemyev Viktor
#date:05.08.2017

import os
import sys
import shutil

#Получение списка файлов
files = os.listdir(sys.argv[1])
path = sys.argv[1]
#получаем путь до директории
deletetypelist = []

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # от отсюда https://gist.github.com/vladignatyev/06860ec2040cb497f0f3

def FileOrDirectory(path):
#Если папка 0, если файл 1, иначе -1
	if os.path.exists(path):
		if os.path.isfile(path):
			res = 1
		elif os.path.isdir(path):
			res = 0
	else:
		res = -1
	return res
	
def RemoveDirectory(path):
#Проверка существует ли папка
    if os.path.exists(path):
#Удалить, если существует
         shutil.rmtree(path)

def uniq(data):
    res = []
    for i in data:
        if i not in res:
            res.append(i)
    return res
     
for filenumber in range(len(files)):

	if (FileOrDirectory(path+"/"+files[filenumber]) == 1):
		if (files[filenumber].find(".") != -1):
			file_name_extension = files[filenumber].split(".")
			deletetypelist.append ("файл типа " + file_name_extension[1])
			os.remove( path+"/"+files[filenumber] )
		else:
			deletetypelist.append ("файл без типа")
			os.remove( path+"/"+files[filenumber] )
	elif (FileOrDirectory(path+"/"+files[filenumber]) == 0):
		deletetypelist.append ("папка        ")
		RemoveDirectory(path+"/"+files[filenumber])
#удалить всё содержимое директории кроме корневой папки
	progress(filenumber+1,len(files))	
#при удалении показывать прогресс-бар	

u_deletetypelist = uniq(deletetypelist)
#получаем список уникальных значений
print ( "" )
for i in range(len(u_deletetypelist)):
	 print (u_deletetypelist[i]," ", deletetypelist.count(u_deletetypelist[i]), "раз удалено" )
#вывести информацию о том, сколько было удалено файлов того или иного типа (папки считаем одним из типов файлов)
deletetypelist.clear()
