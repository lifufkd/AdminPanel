#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import flet as ft
from flet_navigator import VirtualFletNavigator
from UI.pages import log_in, main
############static variables#####################

#################################################


class UI:
    def __init__(self, config, db):
        super(UI, self).__init__()
        self.__vault_keys = ['current_user']
        self.__config = config
        self.__db = db
        self.__log_in = log_in.Log_in(self.__vault_keys, config, db)
        self.__main = main.Main(self.__vault_keys, config, db)

    def main(self, page: ft.Page):
        page.theme_mode = 'dark'
        flet_navigator = VirtualFletNavigator(
            {
                '/': self.__log_in.log_in,
                'main': self.__main.main
            }
        )
        flet_navigator.render(page)

