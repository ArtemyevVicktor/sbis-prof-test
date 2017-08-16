::------------------------------------------
::
::Created:04.08.2017
::Author:Viktor Artemyev
::
::------------------------------------------

echo %date% %TIME:~0,2%:%TIME:~3,2% > current_date_win.txt
::записываем в текстовый файл текущую дату и время
set /p str= <current_date_win.txt
::читаем время записаное в файле
set hour=%str:~11,2%

set /p k= enter k:
for /L %%i in (1,1,%k%) do (
echo Repeat number %%i

if %hour% LSS 12 GOTO LESS
if %hour% GEQ 12 GOTO MOREOREQUAL
)
@goto EXIT

:MOREOREQUAL
::Если время больше или равно 12 часам, то скопировать существующий текстовый файл в файл с тем же именем, но с расширением bak, а в сам текстовый файл дописать текущее дату и время.
copy current_date_win.txt current_date_win.txt.bak
echo %date% %TIME:~0,2%:%TIME:~3,2% > current_date_win.txt
@goto :EOF

:LESS
::Если время меньше 12 часов,то вывести на экран дату из файла.
echo %str:~0,10%
@goto :EOF

:EXIT
