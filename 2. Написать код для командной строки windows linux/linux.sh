#!/bin/bash
#created 03.08.2017
#Auther:Viktor Artemyev 

current_date=`date "+%d/%M/%Y %H:%M"`
#Помещаем в пременную $current_date текущую дату
file_name=current_date.txt
#В переменную $file_name помещаем имя файла

echo $current_date >"$file_name"
#записываем в текстовый файл текущую дату и время 

current_time_saved_in_file=`cat $file_name | awk '{print $2}' | awk -F":" '{print $1}'`
#читаем время записаное в файле

run () {
if [[ $current_time_saved_in_file -lt 12 ]]; then
	cat $file_name | cut -b 1-10
fi
#Если время меньше 12 часов,то вывести на экран дату из файла.

if [[ $current_time_saved_in_file -ge 12 ]]; then
	cp $file_name $file_name.bak
	echo $current_date >"$file_name"
fi
#Если время больше или равно 12 часам, то скопировать существующий текстовый файл в файл с тем же именем, но с расширением bak, а в сам текстовый файл дописать текущее дату и время.
}
echo "Сколько раз выполнять пункт 2.2?:"
read k
for n in $(seq 1 $k); do run;done
