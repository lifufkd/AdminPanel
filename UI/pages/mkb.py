#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from flet_navigator import PageData
from UI.sidebar import SideBar
#################################################


class Mkb:
    def __init__(self, vault, config, db):
        super(Mkb, self).__init__()
        self.__vault = vault
        self.__config = config

    def mkb(self, pg: PageData):
        pg.page.title = "МКБ"
        pg.page.theme_mode = 'dark'
        pg.page.add(
            Row(
                [
                Container(
                    content=SideBar(self.__vault, pg),
                    ),
                VerticalDivider(width=1),
            ],
                expand=True,
            )
        )
        pg.page.update()