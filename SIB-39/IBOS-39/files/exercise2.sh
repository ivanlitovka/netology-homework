#!/bin/bash

a=$(ls)

echo "Нерабочий вариант. Хотя должен показать правильно. Почему не работает?"
echo $a
echo ${#a[@]}

echo "Рабочий вариант"
for val in ${a[@]}
do
     echo $val
     ((counter++))
done
echo "Количество файлов в папке: $counter."
