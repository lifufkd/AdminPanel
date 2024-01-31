#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import MySQLdb
############static variables#####################

#################################################


class DB:
    def __init__(self, db_name, creds):
        super(DB, self).__init__()
        self.__db = None
        self.__cursor = None
        self.__db_name = db_name
        self.__creds = creds

    def connect_db(self):
        self.__db = MySQLdb.connect(host=self.__creds[0], passwd=self.__creds[2], user=self.__creds[1], db=self.__db_name)
        self.__cursor = self.__db.cursor()

    def create_table(self):
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            login TEXT,
            pasword TEXT,
            role INT, # внешний ключ
            full_name TEXT, JSON massive (имя, фамилия, отчество)
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
            file LONGTEXT,
            price INT,
            application_author INT, # внешний ключ
            hospitalized BOOL,
            hospital INT, # внешний ключ
            ratio DECIMAL(7,2),
            status INT # внешний ключ
            date_create DATE,
            date_notice DATE,
            date_hospitalized DATE,
            date_close DATE
        );
        CREATE TABLE IF NOT EXISTS role(
            role VARCHAR(255)
        );
        CREATE TABLE IF NOT EXISTS hospital(
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
            requisites TEXT, # JSON dict with (Номер договора, Управляющий клиники, Должность управляющего, ФИО управляющего, ИНН, КПП, ОГРН, Почтовый индекс, Расчетный счет, Название банка, Корреспондентский счет, БИК)
        );
        CREATE TABLE IF NOT EXISTS med_profile(
            med_profile TEXT
        );
        CREATE TABLE IF NOT EXISTS ksg(
            code VARCHAR(255),
            title TEXT,
            price INT,
            ratio TEXT, # JSON massive with (Коэффициент затрат, Коэффициенты специфики, Коэффициент уровня, Доля ЗП и прочих расходов, switch (Коэффициент уровня мед учреждения))
            mkb TEXT # внешние ключи в JSON
        );
        CREATE TABLE IF NOT EXISTS mkb(
            code VARCHAR(255),
            title TEXT,
            ksg TEXT, # внешние ключи в JSON
            service TEXT, # внешние ключи в JSON
            clinical_minimum TEXT # JSON 2d massive (КАТЕГОРИИ, НАЗВАНИЕ, ВРЕМЯ ДЕЙСТВИЯ (ДНЕЙ))
        );
        CREATE TABLE IF NOT EXISTS service(
            code VARCHAR(255),
            title TEXT,
            mkb TEXT, # внешние ключи в JSON
            ksg TEXT, # внешние ключи в JSON
            clinical_minimum TEXT # JSON 2d massive (КАТЕГОРИИ, НАЗВАНИЕ, ВРЕМЯ ДЕЙСТВИЯ (ДНЕЙ))
        );
        CREATE TABLE IF NOT EXISTS ratio_settings(
            parameter DECIMAL(12,2)
        );
        CREATE TABLE IF NOT EXISTS benefit_status(
            title TEXT
        );
        CREATE TABLE IF NOT EXISTS region(
            title TEXT,
            area TEXT # внешние ключи в JSON
        );
        CREATE TABLE IF NOT EXISTS area(
            area TEXT,
            region INT #внешний ключ
        );
        CREATE TABLE IF NOT EXISTS application_status(
        title TEXT
        );
        CREATE TABLE IF NOT EXISTS payment_type(
        title TEXT
        );
        CREATE TABLE IF NOT EXISTS application_type(
        title TEXT
        );
        ''')


db = DB('db_adminka', ['localhost', 'root', 'toor'])
db.connect_db()
db.create_table()


