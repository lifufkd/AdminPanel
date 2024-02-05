#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from modules.utilites import word_wrap, unparse_json


#################################################


class LoadData:
    def __init__(self, db):
        super(LoadData, self).__init__()
        self.__db = db

    def application(self):
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 30  # перенос слов по 15 символов
        data = list()
        pointer = {1: 'application_type', 2: 'payment_type', 3: 'application_status', 4: 'hospitalized',
                   5: 'benefit_status', 6: 'date_format'}
        raw_data = self.__db.get_data(
            f'SELECT number, application_type, payment_type, application_status, hospitalized, status, date_create, id FROM application WHERE deleted = 0 ORDER BY date_create DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row in pointer.keys():
                    if row == 6:
                        l1.append(rows[row].strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        l1.append(word_wrap(
                            self.__db.get_data(f'SELECT title FROM {pointer[row]} WHERE id = {rows[row]} AND deleted = 0', ())[0][0],
                            max_len))
                elif row == 7:
                    l1.append(rows[row])
                else:
                    l1.append(word_wrap(rows[row], max_len))
            data.append(l1)
        return data

    def area(self):
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 400  # перенос слов по 15 символов
        data = list()
        raw_data = self.__db.get_data(
            f'SELECT area, region, id FROM area WHERE deleted = 0 ORDER BY area DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row == 1:
                    l1.append(self.__db.get_data(f'SELECT title FROM region WHERE id = {rows[1]} AND deleted = 0', ())[0][0])
                elif row == 2:
                    l1.append(rows[row])
                else:
                    l1.append(word_wrap(rows[row], max_len))
            data.append(l1)
        return data

    def clinics(self):
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 30  # перенос слов по 15 символов
        raw_data = self.__db.get_data(
            f'SELECT name, med_profiles, site, phone_number, email, id FROM hospital WHERE deleted = 0 ORDER BY name DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row == 1:
                    profiles = ''
                    for item in unparse_json(rows[row]):
                        profiles += self.__db.get_data(f'SELECT med_profile FROM med_profile WHERE id = {item} AND deleted = 0', ())[0][
                                        0] + ', '
                    l1.append(word_wrap(profiles, max_len))
                elif row == 5:
                    l1.append(rows[row])
                else:
                    l1.append(word_wrap(rows[row], max_len))
            data.append(l1)
        return data

    def ksg(self):
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 30  # перенос слов по 15 символов
        pointer = {4: ['relative_ksg_mkb', 'id_ksg'], 5: ['relative_ksg_service', 'id_ksg'],
                   6: ['relative_ksg_med_profile', 'id_ksg']}
        raw_data = self.__db.get_data(
            f'SELECT code, title, price, ratio_switch, id FROM ksg WHERE deleted = 0 ORDER BY code DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows) + 2):
                if row == 3:
                    if rows[row] == 1:
                        l1.append(True)
                    else:
                        l1.append(False)
                elif row in pointer:
                    l1.append(self.__db.get_quantity(pointer[row][0], [pointer[row][1], rows[4]]))
                elif row == 2:
                    l1.append(rows[row])
                else:
                    l1.append(word_wrap(rows[row], max_len))
            l1.append(rows[4])
            data.append(l1)
        return data

    def med_profile(self):
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 400  # перенос слов по 15 символов
        pointer = {1: ['relative_ksg_med_profile', 'id_med_profile']}
        raw_data = self.__db.get_data(
            f'SELECT med_profile, id FROM med_profile WHERE deleted = 0 ORDER BY med_profile DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row in pointer:
                    l1.append(self.__db.get_quantity(pointer[row][0], [pointer[row][1], rows[1]]))
                    l1.append(rows[row])
                else:
                    l1.append(word_wrap(rows[row], max_len))
            data.append(l1)
        return data

    def mkb(self):
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 200  # перенос слов по 15 символов
        pointer = {2: ['relative_ksg_mkb', 'id_mkb'], 3: ['relative_mkb_service', 'id_mkb']}
        raw_data = self.__db.get_data(
            f'SELECT code, title, id FROM mkb WHERE deleted = 0 ORDER BY code DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows) + 1):
                if row in pointer:
                    l1.append(self.__db.get_quantity(pointer[row][0], [pointer[row][1], rows[2]]))
                else:
                    l1.append(word_wrap(rows[row], max_len))
            l1.append(rows[2])
            data.append(l1)
        return data

    def region(self):
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 400  # перенос слов по 15 символов
        raw_data = self.__db.get_data(
            f'SELECT title, id FROM region WHERE deleted = 0 ORDER BY title DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row == 1:
                    l1.append(self.__db.get_quantity('area', ['region', rows[1]]))
                    l1.append(rows[row])
                else:
                    l1.append(word_wrap(rows[row], max_len))
            data.append(l1)
        return data

    def users(self):
        roles = {0: 'Администратор', 1: 'Модератор', 2: 'Куратор', 3: 'Пользователь'}
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        raw_data = self.__db.get_data(
            f'SELECT id, role, full_name, photo, date_create, email, phone_number, agent, blocked FROM users WHERE deleted = 0 ORDER BY id DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row == 1:
                    l1.append(roles[rows[row]])
                elif row == 2:
                    fio = unparse_json(rows[row])
                    l1.append(f'{fio[0]}\n{fio[1]}\n{fio[2]}')
                elif row == 4:
                    l1.append(rows[row].strftime('%Y-%m-%d %H:%M:%S'))
                elif row in [7, 8]:
                    if rows[row] == 1:
                        l1.append(True)
                    else:
                        l1.append(False)
                else:
                    l1.append(rows[row])
            data.append(l1)
        return data

    def service(self):
        data = list()
        c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        max_len = 200  # перенос слов по 15 символов
        pointer = {2: ['relative_ksg_service', 'id_service'], 3: ['relative_mkb_service', 'id_service']}
        raw_data = self.__db.get_data(
            f'SELECT code, title, id FROM service WHERE deleted = 0 ORDER BY code DESC LIMIT 15 OFFSET {(c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows) + 1):
                if row in pointer:
                    l1.append(self.__db.get_quantity(pointer[row][0], [pointer[row][1], rows[2]]))
                else:
                    l1.append(word_wrap(rows[row], max_len))
            l1.append(rows[2])
            data.append(l1)
        return data


class LoadDropBox:
    def __init__(self, db):
        super(LoadDropBox, self).__init__()
        self.__db = db

    def load_application_type(self):
        return self.__db.get_data(
            f'SELECT title, id FROM application_type WHERE deleted = 0 ORDER BY title',
            ())

    def load_payment_type(self):
        return self.__db.get_data(
            f'SELECT title, id FROM payment_type WHERE deleted = 0 ORDER BY title',
            ())

    def application_status(self):
        return self.__db.get_data(
            f'SELECT title, id FROM application_status WHERE deleted = 0 ORDER BY title',
            ())

    def close_author(self):
        return self.__db.get_data(
            f'SELECT full_name, id FROM users WHERE deleted = 0 ORDER BY full_name',
            ())

    def mkb(self):
        return self.__db.get_data(
            f'SELECT code, id FROM mkb WHERE deleted = 0 ORDER BY code',
            ())

    def service(self):
        return self.__db.get_data(
            f'SELECT code, id FROM service WHERE deleted = 0 ORDER BY code',
            ())

    def hospitalized(self):
        return self.__db.get_data(
            f'SELECT title, id FROM hospitalized WHERE deleted = 0 ORDER BY title',
            ())

    def hospital(self):
        return self.__db.get_data(
            f'SELECT name, id FROM hospital WHERE deleted = 0 ORDER BY name',
            ())

    def benefit_status(self):
        return self.__db.get_data(
            f'SELECT title, id FROM benefit_status WHERE deleted = 0 ORDER BY title',
            ())
