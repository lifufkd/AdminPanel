#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from datetime import datetime
from decimal import Decimal
from modules.utilites import parse_json
#################################################


class ProcessData:
    def __init__(self):
        super(ProcessData, self).__init__()

    def application(self, data):
        cached_data = list()
        required = [11, 15, 17, 18, 19, 20]
        for item in range(len(data) - 1):
            if item == 11:
                try:
                    cached_data.append(int(data[item].value))
                except:
                    cached_data.append(0)
            elif item == 15:
                try:
                    if float(data[item].value) < 0:
                        raise
                    elif float(data[item].value) > 9:
                        cached_data.append(Decimal(9.99))
                    else:
                        cached_data.append(Decimal(round(float(data[item].value), 2)))
                except:
                    cached_data.append(Decimal(0))
            elif item in required[2:]:
                try:
                    cached_data.append(datetime.strptime(data[item].value, "%d-%m-%Y"))
                except:
                    cached_data.append(None)
            else:
                if data[item].value is None:
                    cached_data.append('')
                else:
                    cached_data.append(data[item].value)
        cached_data.insert(11, b'')
        cached_data.append(0)
        return cached_data

    def area(self, data):
        cached_data = list()
        for item in range(len(data) - 1):
            if data[item].value is None:
                cached_data.append('')
            else:
                cached_data.append(data[item].value)
        cached_data.append(0)
        return cached_data

    def users(self, data):
        cached_data = list()
        for item in range(len(data) - 1):
            if item in [1, 2, 3]:
                if len(data[1].value) == 0 or len(data[2].value) == 0 or len(data[3].value) == 0:
                    return None
                elif item in [2, 3]:
                    continue
                else:
                    cached_data.append(parse_json([data[1].value, data[2].value, data[3].value]))
            elif item == 4:
                try:
                    cached_data.append(datetime.strptime(data[item].value, "%d-%m-%Y"))
                except:
                    cached_data.append(None)
            elif item == 11:
                if (data[11].value != data[12].value) or (data[11].value or data[12].value) is None:
                    return None
                continue
            else:
                if data[item].value is None:
                    cached_data.append('')
                else:
                    cached_data.append(data[item].value)
        cached_data.append(0)
        return cached_data

    def med_profile(self, data):
        cached_data = list()
        for item in range(len(data) - 1):
            if item == 1:
                cached_data.append(data[item].value.split(', '))
            else:
                if data[item].value is None:
                    cached_data.append('')
                else:
                    cached_data.append(data[item].value)
        cached_data.append(0)
        return cached_data

    def service(self, data):
        cached_data = list()
        temp = list()
        for item in range(5):
            if item in [2, 3]:
                cached_data.append(data[item].value.split(', '))
            elif item == 4:
                for i in range(4, 13, 3):
                    temp.append([data[i].value, data[i+1].value, data[i+2].value])
                cached_data.append(parse_json(temp))
            else:
                if data[item].value is None:
                    cached_data.append('')
                else:
                    cached_data.append(data[item].value)
        cached_data.append(0)
        return cached_data

    def ksg(self, data):
        cached_data = list()
        temp = list()
        for item in range(len(data) - 1):
            if item in [8, 9, 10]:
                cached_data.append(data[item].value.split(', '))
            elif item in [3, 4, 5, 6]:
                try:
                    if float(data[item].value) < 0:
                        raise
                    elif float(data[item].value) > 1:
                        temp.append(1.00)
                    else:
                        temp.append(round(float(data[item].value), 2))
                except:
                    temp.append(0.00)
            elif item == 2:
                try:
                   cached_data.append(int(data[item].value))
                except:
                    cached_data.append(0)
            elif item == 7:
                if data[item].value:
                    cached_data.append(1)
                else:
                    cached_data.append(0)
            else:
                if data[item].value is None:
                    cached_data.append('')
                else:
                    cached_data.append(data[item].value)
        cached_data.insert(3, parse_json(temp))
        cached_data.append(0)
        return cached_data