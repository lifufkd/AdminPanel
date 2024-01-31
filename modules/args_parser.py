#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import json
import os
import sys
############static variables#####################

#################################################


class Parser:
    def __init__(self, file_path):
        super(Parser, self).__init__()
        self.__file_path = file_path
        self.__default = {'db_name': '', 'db_host': '', 'db_user': '', 'db_passwd': '', 'logo_path': ''}
        self.__current_config = None
        self.parse_args()

    def load_conf(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                config = file.read()
        else:
            self.create_conf()
            sys.exit('config is empty')
        return config

    def parse_args(self):
        args = json.loads(self.load_conf())
        self.__current_config = args

    def create_conf(self):
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.__default, sort_keys=True, indent=4))
