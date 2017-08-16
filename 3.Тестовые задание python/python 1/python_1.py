#python 3.5.2
# -*- encoding: utf-8 -*-
#author: Artemyev Viktor
#date:04.08.2017

from datetime import datetime

def median(data):
    data.sort()
    res = 0.0
    if len(data) % 2:
        res = data[int(len(data) / 2)]
    else:
        res = (data[int(round(len(data) / 2 - .5))] + data[int(round(len(data) / 2))])/2
    return res
    
def max(data):
	timedelta.sort()
	res = timedelta[0]
	return res

def mix(data):
	timedelta.sort()
	res = timedelta[len(timedelta)-1]
	return res

def Average(data):
	res = sum(data) / len(data)
	return res

def uniq(data):
    res = []
    for i in data:
        if i not in res:
            res.append(i)
    return res

logfile = open("test_log.txt", "r")
strings = logfile.readlines()
#читаем файл лога
logfile.close()
#закрываем файл

timedelta = []
req_path = []
requests = []
#создаем списки для парсинга

for i in range(len(strings)):
 elements = strings[i].split('|')
 date1 = datetime.strptime(elements[0], "%d.%m.%Y %H:%M:%S ")
 date2 = datetime.strptime(elements[1], " %d.%m.%Y %H:%M:%S ")
#парсим начальное время и конечное

 result_date = date2 - date1
#вычисляем разницу
 timedelta.append ( result_date.total_seconds() )
#добавляем к списку разницу в секундах
 
 req_path.append ( elements[2] )
#добовляем к списку запрашиваемый адрес
 if (int(elements[3]) >= 400) or (elements[4].find("error") != -1):
	 requests.append ( "bad" )
 else:
	 requests.append ( "good" )
#если код вышее 400 или в теле присутствует подстрока “error”,то записваем в список bad в ином случае good
 
#
print ( "Cтатистические характеристики времени обработки сервером всех запросов (минимум, максимум, среднее арфиметическое, медиана) ):" )
print ( "Min", mix(timedelta), "сек" )
print ( "Max", max(timedelta), "сек"  )
print ( "Average", Average(timedelta), "сек")
print ( "Median", median(timedelta), "сек"  )
print ( "-------------------------------" )
print ( "Процент ошибочных и успешных запросов:" )
print ( "bad reqest",(requests.count("bad")/len(requests))*100, "%" )
print ( "good reqest",(requests.count("good")/len(requests))*100, "%" )
print ( "-------------------------------" )
#выводим результаты на экран
u_req_path = uniq(req_path)
#получаем список уникальных значений
u_req_path.sort()
print ( "Распределение числа вызовов по страницам:" )
for i in range(len(u_req_path)):
 print (u_req_path[i],"страницу ", req_path.count(u_req_path[i]), "раз вызывали" )
#какую страницу сколько раз вызывали
 
timedelta.clear()
req_path.clear()
requests.clear()
#отчищаем списки
