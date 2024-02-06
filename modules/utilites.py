#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import datetime
import json
import os
import parawrap
import xlwt
from time import gmtime, strftime
############static variables#####################

#################################################


def get_rtc():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def get_data_main_page(db):
    cat_quantity = {'ksg': 0, 'mkb': 0, 'service': 0, 'region': 0, 'area': 0, 'med_profile': 0, 'users': 0}
    temp = list()
    for cat in cat_quantity.keys():
        if cat == 'users':
            for role in range(4):
                temp.append(db.get_quantity(cat, ['role', role]))
            cat_quantity[cat] = temp  # 0 - admin, 1 - moderator, 2 - curator, 3 - user
        else:
            cat_quantity[cat] = db.get_quantity(cat)
    return cat_quantity


def unparse_json(data):
    return json.loads(data)


def parse_json(data):
    return json.dumps(data)


def update_profile(new_data, old_data, db):
    out = list()
    f_old = old_data[0:2] + [old_data[5]]
    compare = {0: 'login', 1: 'full_name', 2: 'password'}
    for diff in range(len(new_data)):
        if diff == 1:
            out.append([])
            for i in range(len(new_data[diff])):
                if new_data[diff][i] != '':
                    out[diff].append(new_data[diff][i])
                else:
                    out[diff].append(f_old[diff][i])
            db.add_db_entry(f'UPDATE users SET {compare[diff]} = %s WHERE id = {old_data[4]}', (parse_json(out[diff]), ))
        else:
            if new_data[diff] != '':
                out.append(new_data[diff])
                db.add_db_entry(f'UPDATE users SET {compare[diff]} = %s WHERE id = %s', (new_data[diff], old_data[5]))
            else:
                out.append(f_old[diff])
    for i in range(3):
        out.insert(i + 2, old_data[i + 2])
    return out


def word_wrap(text, max_len):
    s = ''
    data = parawrap.wrap(text, max_len)
    for i in data:
        s += i + '\n'
    return s


def save_export_xlsx(path, data, typ):
    if not os.path.exists(path):
        os.mkdir(path)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet")
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j])
    workbook.save(path + f'export_{typ}({strftime("%Y_%m_%d_%H_%M_%S", gmtime())}).xlsx')


def switch_btns_user(data, value, db):
    fields = {'1': 'agent', '2': 'blocked'}
    db.add_db_entry(f'UPDATE users SET {fields[data[1]]} = {value} WHERE id = "{data[0]}"', ())


def switch_btns_ksg(data, value, db):
    db.add_db_entry(f'UPDATE ksg SET ratio_switch = {value} WHERE id = "{data}"', ())


def delete_row(db, data):
    for i, g in data.items():
        db.add_db_entry(f'UPDATE {i} SET deleted = 1 WHERE {g[0]} = "{g[1]}"', ())


def insert_data_application(db, table, data):
    db.add_db_entry(f'INSERT INTO {table} (number, application_type, payment_type, application_status, close_author, patient, mkb, service, сhronic_diseases, comment_designer, comment_tutor, file, price, application_author, hospitalized, hospital, ratio, status, date_create, date_notice, date_hospitalized, date_close, deleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', data)


def update_data_application(db, table, data, row_id):
    db.add_db_entry(f'UPDATE {table} SET number = %s, application_type = %s, payment_type = %s, application_status = %s, close_author = %s, patient = %s, mkb = %s, service = %s, сhronic_diseases = %s, comment_designer = %s, comment_tutor = %s, file = %s, price = %s, application_author = %s, hospitalized = %s, hospital = %s, ratio = %s, status = %s, date_create = %s, date_notice = %s, date_hospitalized = %s, date_close = %s, deleted = %s WHERE id = {row_id}', data)


def insert_data_area(db, table, data):
    db.add_db_entry(f'INSERT INTO {table} (area, region, deleted) VALUES (%s, %s, %s)', data)


def update_data_area(db, table, data, row_id):
    db.add_db_entry(f'UPDATE {table} SET area = %s, region = %s, deleted = %s WHERE id = {row_id}', data)




