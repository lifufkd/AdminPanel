#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import datetime
import json
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
    print(old_data[4])
    out = list()
    f_old = old_data[0:2] + [old_data[4]]
    compare = {0: 'login', 1: 'full_name', 2: 'password'}
    for diff in range(len(new_data)):
        if diff == 1:
            for i in range(len(new_data[diff])):
                if new_data[diff][i] != '':
                    out.append(new_data[diff][i])
                else:
                    out.append(f_old[diff][i])
            db.add_db_entry(f'UPDATE users SET %s = "{parse_json(out)}" WHERE id = %s', [compare[diff], old_data[5]])
        else:
            if new_data[diff] != '':
                pass
                #db.add_db_entry(f'UPDATE users SET {compare[diff]} = "{new_data[diff]}" WHERE id = "{old_data[5]}"', ())


