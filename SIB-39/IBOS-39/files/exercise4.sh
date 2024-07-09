#!/bin/bash


if [ $# ==  2 ]
  then
	case $1 in
	  crypt)
	    echo $2 | base64;;
 	  decrypt)
	    echo $2 | base64 -d;;
	  *) echo "Не верно заданы параметры. Используйте скрипт следующим образом: exercise4.sh crypt|decrypt сообщение"
	esac
  else 
	echo "Не верно заданы параметры. Используйте скрипт следующим образом: exercise4.sh crypt|decrypt сообщение"
fi
