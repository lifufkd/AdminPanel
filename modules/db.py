#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import MySQLdb
import datetime
############static variables#####################

#################################################


class DB:
    def __init__(self, config):
        super(DB, self).__init__()
        self.__db = None
        self.__cursor = None
        self.__config = config
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.__db = MySQLdb.connect(host=self.__config['db_host'], passwd=self.__config['db_passwd'], user=self.__config['db_user'], db=self.__config['db_name'])
        self.__cursor = self.__db.cursor()

    def create_table(self):
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            login TEXT,
            password TEXT,
            role INT, # внешний ключ
            full_name TEXT, # JSON massive (имя, фамилия, отчество)
            photo MEDIUMBLOB,
            date_create DATE,
            email VARCHAR(255),
            phone_number INT,
            region INT, # внешний ключ
            area INT, # внешний ключ
            agent BOOL,
            blocked BOOL
        );
        CREATE TABLE IF NOT EXISTS application(
            id INT AUTO_INCREMENT PRIMARY KEY,
            number TEXT, # Номер (в оригинале)
            application_type INT, # внешний ключ
            payment_type INT, # внешний ключ
            application_status INT, # внешний ключ
            close_author INT, # внешний ключ
            patient INT, # внешний ключ
            mkb INT, # внешний ключ
            service INT, # внешний ключ
            сhronic_diseases TEXT,
            comment_designer TEXT,
            comment_tutor TEXT,
            file LONGTEXT, # JSON massive with blobs
            price INT,
            application_author INT, # внешний ключ
            hospitalized BOOL,
            hospital INT, # внешний ключ
            ratio DECIMAL(7,2),
            status INT, # внешний ключ
            date_create DATE,
            date_notice DATE,
            date_hospitalized DATE,
            date_close DATE
        );
        CREATE TABLE IF NOT EXISTS role(
            id INT AUTO_INCREMENT PRIMARY KEY,
            role VARCHAR(255)
        );
        CREATE TABLE IF NOT EXISTS hospital(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT,
            med_profiles TEXT, # внешние ключи в JSON
            moderator INT, # внешний ключ
            ratio INT, # Из ratio_settings
            base_rate INT,
            site TEXT,
            phone_number INT,
            email VARCHAR(255),
            other_contact TEXT, # JSON 2d massive
            region INT, # внешний ключ
            area INT, # внешний ключ
            city TEXT,
            addres TEXT,
            photo LONGTEXT, # JSON massive with blobs
            requisites TEXT # JSON dict with (Номер договора, Управляющий клиники, Должность управляющего, ФИО управляющего, ИНН, КПП, ОГРН, Почтовый индекс, Расчетный счет, Название банка, Корреспондентский счет, БИК)
        );
        CREATE TABLE IF NOT EXISTS med_profile(
            id INT AUTO_INCREMENT PRIMARY KEY,
            med_profile TEXT
        );
        CREATE TABLE IF NOT EXISTS ksg(
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(255),
            title TEXT,
            price INT,
            ratio TEXT, # JSON massive with (Коэффициент затрат, Коэффициенты специфики, Коэффициент уровня, Доля ЗП и прочих расходов, switch (Коэффициент уровня мед учреждения))
            mkb TEXT # внешние ключи в JSON
        );
        CREATE TABLE IF NOT EXISTS mkb(
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(255),
            title TEXT,
            ksg TEXT, # внешние ключи в JSON
            service TEXT, # внешние ключи в JSON
            clinical_minimum TEXT # JSON 2d massive (КАТЕГОРИИ, НАЗВАНИЕ, ВРЕМЯ ДЕЙСТВИЯ (ДНЕЙ))
        );
        CREATE TABLE IF NOT EXISTS service(
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(255),
            title TEXT,
            mkb TEXT, # внешние ключи в JSON
            ksg TEXT, # внешние ключи в JSON
            clinical_minimum TEXT # JSON 2d massive (КАТЕГОРИИ, НАЗВАНИЕ, ВРЕМЯ ДЕЙСТВИЯ (ДНЕЙ))
        );
        CREATE TABLE IF NOT EXISTS ratio_settings(
            id INT AUTO_INCREMENT PRIMARY KEY,
            parameter DECIMAL(12,2)
        );
        CREATE TABLE IF NOT EXISTS benefit_status(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT
        );
        CREATE TABLE IF NOT EXISTS region(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            area TEXT # внешние ключи в JSON
        );
        CREATE TABLE IF NOT EXISTS area(
            id INT AUTO_INCREMENT PRIMARY KEY,
            area TEXT,
            region INT #внешний ключ
        );
        CREATE TABLE IF NOT EXISTS application_status(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT
        );
        CREATE TABLE IF NOT EXISTS payment_type(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT
        );
        CREATE TABLE IF NOT EXISTS application_type(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT
        );
        ''')

    def add_db_entry(self, query):
        self.__cursor.execute(query)
        self.__db.commit()

    def authorization(self, login, password):
        self.__cursor.execute(f'SELECT id FROM users WHERE login = "{login}" AND password = "{password}"')
        if len(self.__cursor.fetchall()) != 0:
            access = True
        else:
            access = False
        return access



