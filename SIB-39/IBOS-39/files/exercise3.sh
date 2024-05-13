#!/bin/bash


if [ -e $1 ]
  then
	case $(ls -ld -- "$1") in
	  -*)
	    echo "Файл $1 является файлом";;
 	  d*)
	    echo "Файл $1 является каталогом";;
	esac
  else 
	echo "Файл $1 не существует"
fi
