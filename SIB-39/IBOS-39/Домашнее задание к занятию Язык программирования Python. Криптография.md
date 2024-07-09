# Домашнее задание к занятию «Язык программирования Python. Криптография.»

В качестве результата пришлите ответы на вопросы в личном кабинете студента на сайте [netology.ru](https://netology.ru/).

**Важно**: перед отправкой переименуйте ваш скрипт в `script.txt` (система отправки файлов Netology блокирует файлы с расширением `.py`).



## Задание 1

Реализуйте атаку грубой силой на текст, зашифрованный AES. В качестве пароля возьмите трёхзначное число.


Примечание: вместо **pip install *cryptodome*** сейчас лучше использовать **pip install *pycryptodome***, - это обновлённый пакет криптографии для Python. Более подробую информацию можно посмотреть вот здесь: [Installation pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/installation.html?highlight=Cryptodome#compiling-in-linux-ubuntu)

Использовал пример с сайта с описанием библиотеки   
```
from Crypto.Cipher import AES
from Crypto import Random
import hashlib

key = b'123'
key = hashlib.sha256(key).digest()
print(key)

cipher = AES.new(key, AES.MODE_EAX)

nonce = cipher.nonce
data = b'Secret text'
ciphertext, tag = cipher.encrypt_and_digest(data)
print("Ciphertext:", ciphertext)


for i in range(0,1000):
    t = bytes(str(i), encoding='utf-8')
    key_dec=hashlib.sha256(t).digest()
    cipher = AES.new(key_dec, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    print("\nSecret text:",i,":",plaintext)
```  

Результат: 
```commandline
C:\Users\ivanl\AppData\Local\Programs\Python\Python310\python.exe D:\netology-homework\netology-homework\SIB-39\IBOS-39\files\crypto.py 
b'\xa6e\xa4Y B/\x9dA~Hg\xef\xdcO\xb8\xa0J\x1f?\xff\x1f\xa0~\x99\x8e\x86\xf7\xf7\xa2z\xe3'
Ciphertext: b'\xa7N\xeb[\x17\xc2Q\xbc\xa7\xa8\xb9'
...
...
...
Secret text: 121 : b'\x9f\x0bQ+\x91\xc4[\x16\xb7k8'

Secret text: 122 : b'\xb2V\x0c\xb8r\x172W\x15\x07u'

Secret text: 123 : b'Secret text'

Secret text: 124 : b'\xb8\xc0\xeb{k\x00m\tJ\xa1q'

Secret text: 125 : b'\xf8\xe2\xc8\xec\xb1\xa4Y\xf5\xe3\xddS'


```