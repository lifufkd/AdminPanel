# **Admin panel for medical company**
## [EN] 
### This application can be used to administer hospital networks.
### Implemented functions:
#### 1. Authorization
* Entering a username and password
#### 2. Profile
* Editing your account information
* Changing the password
### Usage and setup:
#### 1. Installation
* Download from the source code: Clone the repository and install all dependencies (pip install -r req.txt ). Launch main.py
* Download the latest release for your architecture and run.
#### 2. First start
The first time you run the program, a configuration file is created (in the folder with the executable file). In it, you need to fill in the data for Mysql authorization, the path to the resources and the path for saving reports.
### Technical information:
* DB: MySql
* Security: User passwords are hashed using the sha-512 algorithm and stored in the database, SSL encryption (manualy) is used when exchanging data between the server and the client.
* UI interface: flet (web and desktop versions)
## [RU]
### Это приложение может использоваться для администрирования сетей больниц.
### Реализованные функции:
#### 1. Авторизация
* Ввод логина и пароля
#### 2. Профиль
* Редактирование информации о своём аккаунте
* Смена пароля
### Использование и настройка:
#### 1. Установка
* Загрузить из исходного кода: Клонируйте репозиторий и установите все зависимости (pip install -r req.txt ). Запустить main.py
* Загрузить последний релиз для своей архитектуры и запустить.
#### 2. Первый запуск
При первом запуске программы создаётся файл конфигурации (в папке с исполняемым файлом). В нем необходимо заполнить данные для авторизации Mysql, путь до ресурсов и путь для сохранения отчётов.
### Техническая информация:
* БД: MySql
* Безопасность: Пароли пользователей хэшируются с помощью алгоритма sha-512 и сохраняются в БД, при обмене данных между сервером и клиентом используется SSL шифрование (настраивается).
* UI interface: реализован с помощью библиотеки flet (веб и десктоп)
