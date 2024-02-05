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
        self.__db = MySQLdb.connect(host=self.__config['db_host'], passwd=self.__config['db_passwd'], user=self.__config['db_user'], db=self.__config['db_name'], autocommit=True)
        self.__cursor = self.__db.cursor()

    def create_table(self):
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            login TEXT,
            password TEXT,
            role INT, # 0 - admin, 1 - moderator, 2 - curator, 3 - user
            full_name JSON, # JSON massive (имя, фамилия, отчество)
            photo MEDIUMBLOB,
            date_create DATETIME,
            email VARCHAR(255),
            phone_number TEXT,
            region INT, # внешний ключ
            area INT, # внешний ключ
            agent BOOL,
            blocked BOOL,
            deleted BOOL
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
            hospitalized INT,
            hospital INT, # внешний ключ
            ratio DECIMAL(7,2),
            status INT, # внешний ключ
            date_create DATETIME,
            date_notice DATETIME,
            date_hospitalized DATETIME,
            date_close DATETIME,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS hospitalized(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS hospital(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT,
            med_profiles TEXT, # внешние ключи в JSON
            moderator INT, # внешний ключ
            ratio INT, # Из ratio_settings
            base_rate INT,
            site TEXT,
            phone_number TEXT,
            email VARCHAR(255),
            other_contact TEXT, # JSON 2d massive
            region INT, # внешний ключ
            area INT, # внешний ключ
            city TEXT,
            addres TEXT,
            photo LONGTEXT, # JSON massive with blobs
            requisites TEXT, # JSON dict with (Номер договора, Управляющий клиники, Должность управляющего, ФИО управляющего, ИНН, КПП, ОГРН, Почтовый индекс, Расчетный счет, Название банка, Корреспондентский счет, БИК)
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS med_profile(
            id INT AUTO_INCREMENT PRIMARY KEY,
            med_profile TEXT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS ksg(
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(255),
            title TEXT,
            price INT,
            ratio TEXT, # JSON massive with (Коэффициент затрат, Коэффициенты специфики, Коэффициент уровня, Доля ЗП и прочих расходов),
            ratio_switch BOOL,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS relative_ksg_mkb(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_ksg INT,
            id_mkb INT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS relative_ksg_service(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_ksg INT,
            id_service INT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS relative_ksg_med_profile(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_ksg INT,
            id_med_profile INT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS relative_mkb_service(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_mkb INT,
            id_service INT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS mkb(
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(255),
            title TEXT,
            clinical_minimum TEXT, # JSON 2d massive (КАТЕГОРИИ, НАЗВАНИЕ, ВРЕМЯ ДЕЙСТВИЯ (ДНЕЙ))
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS service(
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(255),
            title TEXT,
            clinical_minimum TEXT, # JSON 2d massive (КАТЕГОРИИ, НАЗВАНИЕ, ВРЕМЯ ДЕЙСТВИЯ (ДНЕЙ))
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS ratio_settings(
            id INT AUTO_INCREMENT PRIMARY KEY,
            parameter DECIMAL(12,2),
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS benefit_status(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS region(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS area(
            id INT AUTO_INCREMENT PRIMARY KEY,
            area TEXT,
            region INT, #внешний ключ
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS application_status(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS payment_type(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            deleted BOOL
        );
        CREATE TABLE IF NOT EXISTS application_type(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            deleted BOOL
        );
        ''')

    def add_db_entry(self, query, var):
        self.__cursor.execute(query, var)
        self.__db.commit()

    def authorization(self, login, password):
        self.__cursor.execute(f'SELECT login, full_name, email, photo, id, password FROM users WHERE login = "{login}" AND password = "{password}" AND role = "0" AND blocked = "0" AND "deleted" = 0')
        user_data = self.__cursor.fetchone()
        if user_data is not None:
            return list(user_data)

    def get_quantity(self, table, addition=None):
        if addition is not None:
            self.__cursor.execute(f'SELECT count(*) FROM {table} WHERE {addition[0]} = "{addition[1]}" AND deleted = 0')
        else:
            self.__cursor.execute(f'SELECT count(*) FROM {table} WHERE deleted = 0')
        return list(self.__cursor.fetchone())[0]

    def get_data(self, query, var):
        self.__cursor.execute(query, var)
        return list(self.__cursor.fetchall())

