#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import datetime
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
