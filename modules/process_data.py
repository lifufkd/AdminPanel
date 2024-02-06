#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from decimal import Decimal
from datetime import datetime

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
                    if float(data[item].value) > 9:
                        cached_data.append(Decimal(9.99))
                    else:
                        cached_data.append(Decimal(round(float(data[item].value), 2)))
                except:
                    cached_data.append(Decimal(0))
            elif item in required[2:]:
                if data[item].value == '':
                    cached_data.append(None)
                else:
                    cached_data.append(data[item].value)
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