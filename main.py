#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import threading
import time
import json
from modules.db import DB
from UI.visual_draw import UI
from modules.args_parser import Parser
import flet as ft
import os

############static variables#####################
config_name = 'secrets.json'
#################################################

if __name__ == '__main__':
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = Parser(f'{work_dir}/{config_name}')
    db = DB(config._Parser__current_config)
    ui = UI(config._Parser__current_config, db, work_dir)
    ft.app(target=ui.main_menu)