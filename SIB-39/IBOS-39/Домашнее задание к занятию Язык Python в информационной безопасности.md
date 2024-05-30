# Домашнее задание к занятию «Язык Python в информационной безопасности»

##Студент: Литовка Иван

В качестве результата пришлите ответы на вопросы в личном кабинете студента на сайте [netology.ru](https://netology.ru/).

**Важно**: перед отправкой переименуйте ваш скрипт в `script.txt` (система отправки файлов Netology блокирует файлы с расширением `.py`).


## Задание 1

Просканируйте с помошью Python ВМ Metasploitable. Определите установленные службы (нужно вывести название и версию службы, номер порта.)

[nmap.py](./files/nmap.py)

```
import nmap3

nmap = nmap3.Nmap()
result = nmap.nmap_version_detection("192.168.3.110")
for i in result["192.168.3.110"]["ports"]:
	print(i["protocol"], i["portid"], i["state"], i["service"]["name"], i["service"].get("version"))
	
/usr/local/bin/python3.9 /Users/ivanlitovka/Documents/netology-homework/SIB-39/IBOS-39/files/nmap.py 
tcp 22 open ssh 8.9p1 Ubuntu 3ubuntu0.4
tcp 80 open http 2.4.52

Process finished with exit code 0
                                                                        ~~~~~~~~~~~~^^^^^^^^^^^



```