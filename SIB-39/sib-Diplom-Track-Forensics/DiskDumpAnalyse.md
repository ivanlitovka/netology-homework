**Отчет сканирования дампа жеского диска**


Журналы событий
неизвестный хост 37L4247D28-05
подключения к хосту по rdp с адреса 192.168.1.71
```User: IEWIN7\Wilfred
Session ID: 1
Source Network Address: 192.168.1.71
Type :		Information
Date :		09.03.2019
Time :		19:36:57
Event :		25
Source :		Microsoft-Windows-TerminalServices-LocalSessionManager
Category :	None
User :		\СИСТЕМА
Computer :	IEWIN7
Description:
Remote Desktop Services: Session reconnection succeeded:

User: IEWIN7\Wilfred
Session ID: 1
Source Network Address: 192.168.1.71
```

```
Type :		Information
Date :		10.03.2019
Time :		9:47:09
Event :		1149
Source :		Microsoft-Windows-TerminalServices-RemoteConnectionManager
Category :	None
User :		NT AUTHORITY\NETWORK SERVICE
Computer :	IEWIN7
Description:
Remote Desktop Services: User authentication succeeded:

User: Support
Domain: 
Source Network Address: 192.168.1.76

```

Очистка журнала windows defender 
```
Type :		Information
Date :		09.03.2019
Time :		17:29:25
Event :		1013
Source :		Microsoft-Windows-Windows Defender
Category :	None
User :		\СИСТЕМА
Computer :	IEWIN7
Description:
Microsoft Defender Antivirus has removed history of malware and other potentially unwanted software.
 	Time: 2/7/2019 6:29:21 AM
 	User: NT AUTHORITY\SYSTEM

```


Пользователь Support Created On 2019-03-10 06:45:48

**Полученные файлы:**

OpenSavePidlMRU
LastWrite time: 2019-03-10 06:35:43Z
OpenSavePidlMRU\*
LastWrite Time: Sun Mar 10 06:40:02 2019
Note: All value names are listed in MRUListEx order.

  My Computer\C:\Windows\Temp\iepv.zip
  My Computer\C:\Windows\Temp\netscan_portable.zip
  My Computer\C:\Windows\Temp\1
  passwords.txt

OpenSavePidlMRU\txt
LastWrite Time: Sat Mar  9 15:35:28 2019
Note: All value names are listed in MRUListEx order.

  passwords.txt

OpenSavePidlMRU\zip
LastWrite Time: Sun Mar 10 06:40:02 2019
Note: All value names are listed in MRUListEx order.

  My Computer\C:\Windows\Temp\iepv.zip
  My Computer\C:\Windows\Temp\netscan_portable.zip

**Файл 1 содежит зашифрованный base64 скрипт, обнаруженный в дампе оперативной памяти.**

environment v.20200512
(System, NTUSER.DAT) Get environment vars from NTUSER.DAT & System hives

Environment
LastWrite Time: 2019-03-09 16:57:35Z

TEMP                      %USERPROFILE%\AppData\Local\Temp                  
TMP                       %USERPROFILE%\AppData\Local\Temp                  
UserInitMprLogonScript    C:\Users\Wilfred\AppData\Roaming\Identities\Updater.bat
**ALERT: UserInitMprLogonScript value found: C:\Users\Wilfred\AppData\Roaming\Identities\Updater.bat

**Updater.bat так же содержит скрипт и активируется при входе пользователя в систему**

