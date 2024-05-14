# Домашнее задание к занятию «Язык Python. Основы.»

## Задание 1

Напишите два скрипта, каждый из которых принимает один параметр и:

- первый - прибавляет к параметру единицу как строку.

  **Например:**

  **./python3 test_1.py 5**

  **51**

- второй - прибавляет к параметру единицу как число.

  **Например:**

  **./python3 test_2.py 5**

  **6**

[exercise1.py](./files/exercise1.py)
```
import sys
print("1) "+sys.argv[1]+"1")
a=int(sys.argv[1])+1
print("2) ",a)

ivanlitovka@MacBook-Pro-Ivan files % python3 exercise1.py 5
1) 51
2)  6
ivanlitovka@MacBook-Pro-Ivan files % 
```

## Задание 2

Напишите скрипт, который выводит содержимое каталога и подсчитывает в нём количество файлов.

**Например:**

**./test_dir.py**  
**admin_scripts**  
**...**  
**Videos**  
**Total: 22**  

[exercise2.py](./files/exercise2.py)
```
import sys
import os

dirs = next(os.walk(sys.argv[1]))[1]
count = 0
for i in dirs:
    print(i)
    count+=1
print(count," Files in folder")

ivanlitovka@MacBook-Pro-Ivan files % python3 exercise2.py /etc/
periodic
sudoers.d
ssl
racoon
snmp
paths.d
asl
security
manpaths.d
ppp
newsyslog.d
pam.d
defaults
apache2
ssh
postfix
pf.anchors
openldap
wfs
cups
uucp
21  Files in folder
ivanlitovka@MacBook-Pro-Ivan files % 
```



## Задание 3

Напишите скрипт, который принимает один параметр и определяет, какой объект передан этим параметром (файл, каталог или не существующий). 

**Например:**

**./test.py \windows**  
**c:\windows - dir**  
**./test.py c:\pagefile.sys**  
**c:\pagefile.sys - file**  
**user@user:~$ c:\windows1**  
**c:\windows1 - not exist**  

[exercise3.py](./files/exercise3.py)

```
import sys
import os

if os.path.isdir(sys.argv[1]):
    print("this directory")
elif os.path.isfile(sys.argv[1]):
    print("this file")
else:
    print("Object not exist")

ivanlitovka@MacBook-Pro-Ivan files % python3 exercise3.py /etc 
this directory
ivanlitovka@MacBook-Pro-Ivan files % python3 exercise3.py /etc/passwd 
this file
ivanlitovka@MacBook-Pro-Ivan files % python3 exercise3.py /etc/passwd111
Object not exist
```

## Задание 4* (необязательное)

### Легенда

Пользователи в нашей компании начали пересылать друг другу некие "секретные" сообщения. Т.к. доступа к средствам криптографии у них нет, для "шифрования" они используют преобразование строк в формат [Base64](https://ru.wikipedia.org/wiki/Base64).

### Задача

Написать скрипт, который:

1. принимает на входе два аргумента. Первый - режим преобразования, второй - строка;
2. если первый параметр равен `crypt` - преобразует второй параметр в строку Base64;
3. если первый параметр равен `decrypt` - преобразует второй параметр в текст;
4. если первый параметр равен любой другой строке - выйти из скрипта с ненулевым кодом возврата и сообщить об этом пользователю;
5. если количество параметров скрипта не равно двум - выйти из скрипта с ненулевым кодом возврата выдать сообщение пользователю и завершить работу.

Пример работы:

```
$ ./script.py crypt test
Encrypting...
dGVzdAo=
$ ./script.py decrypt dGVzdAo=
Decrypting...
test
```
[exercise4.py](./files/exercise4.py)
```
import sys
import os
import base64

if len(sys.argv) != 3:
    print("Use next syntax: python3 exercise4.py encode|decode text")
elif sys.argv[1] == "encode":
    print(base64.b64encode(sys.argv[2].encode('ascii')).decode('ascii'))
elif sys.argv[1] == "decode":
    print(base64.b64decode(sys.argv[2].encode('ascii')).decode('ascii'))
else:
    print("Use next syntax: python3 exercise4.py encode|decode text")

ivanlitovka@MacBook-Pro-Ivan files % python3 exercise4.py encode Hello   
SGVsbG8=
ivanlitovka@MacBook-Pro-Ivan files % python3 exercise4.py decode SGVsbG8=
Hello
ivanlitovka@MacBook-Pro-Ivan files % python3 exercise4.py decode         
Use next syntax: python3 exercise4.py encode|decode text
ivanlitovka@MacBook-Pro-Ivan files % python3 exercise4.py dfdfd SGVsbG8=
Use next syntax: python3 exercise4.py encode|decode text
ivanlitovka@MacBook-Pro-Ivan files % 
```