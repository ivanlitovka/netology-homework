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
result = nmap.nmap_version_detection("192.168.31.135")
for i in result["192.168.31.135"]["ports"]:
	print(i["protocol"], i["portid"], i["state"], i["service"]["name"], i["service"]["version"])
	
┌──(ivan㉿kali)-[~]
└─$ sudo python3 nmap.py
tcp 21 open ftp 2.3.4
tcp 22 open ssh 4.7p1 Debian 8ubuntu1
Traceback (most recent call last):
  File "/home/ivan/nmap.py", line 6, in <module>
    print(i["protocol"], i["portid"], i["state"], i["service"]["name"], i["service"]["version"])
                                                                        ~~~~~~~~~~~~^^^^^^^^^^^



```