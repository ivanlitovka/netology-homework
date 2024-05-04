### Задача
## Студент: Литовка Иван

Скачайте:
1. [Исполняемый файл сервера](assets/server.bin)
1. [Сертификат](assets/certificate.pem) и [приватный ключ](assets/key.pem)

Настройте запуск сервера (используйте виртуальную машину с ОС Ubuntu) при старте системы с рабочим каталогом `/opt/app` (сертификаты должны располагаться в нём же).

С помощью `journalctl` отследите, лог приложения (не менее 2х минут) и пришлите:
1. Скриншот, либо содержимое файла `app.service`
```
ivan@ubuntu:~$ cat /etc/systemd/system/app.service 
[Unit]
Description=app
After=network.target auditd.service

[Service]
WorkingDirectory=/opt/app
ExecStart=/opt/app/server.bin

[Install]
WantedBy=multi-user.target
```  

1. Ответы на впоросы:
    1. На каком IP и порту запускается сервис
    ```
    0.0.0.0:9999
    ```

    1. Кто (IP и порт) шлёт запросы на этот сервис и на какой путь
    шлет запросы localhost с рандомного порта на /api/token
    1. Какие ответы (формат) получает клиент из п.ii получает в ответ на свои запросы
    получает ответ Status:Ok