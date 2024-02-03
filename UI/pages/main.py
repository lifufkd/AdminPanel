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
from modules.utilites import get_data_main_page
#################################################


class Diagram:
    def __init__(self):
        super(Diagram, self).__init__()
        self.__content = {1: ['База услуг', 'КСГ', 'МКБ', 'Услуги'], 2: ['Справочники', 'Регионы', 'Области', 'Мед. профили'], 3: ['Пользователи', 'Админы', 'Кураторы', 'Модераторы', 'Пользователи'] }

    def add_diagram(self, cont, data):
        fig, ax = plt.subplots()
        fruits = [self.__content[cont][1], self.__content[cont][2], self.__content[cont][3]]
        counts = [data[0], data[1], data[2]]
        bar_colors = ["tab:red", "tab:blue", "tab:orange"]
        if cont == 3:
            fruits.append(self.__content[cont][4])
            counts.append(data[3])
            bar_colors.append('tab:green')
        ax.bar(fruits, counts, color=bar_colors)
        ax.set_title(self.__content[cont][0])
        return fig


class Main:
    def __init__(self, vault, config, db):
        super(Main, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__diagram = Diagram()

    def main(self, pg: PageData):
        diagram_data = get_data_main_page(self.__db)
        pg.page.title = "Главное меню"
        pg.page.theme_mode = 'dark'
        pg.page.add(
            Row(
                [
                Container(
                    content=SideBar(self.__vault, pg),
                ),
                VerticalDivider(width=1),
                Container(
                    height=1000,
                    width=1500,
                    content=Row([
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(self.__diagram.add_diagram(1, [diagram_data['ksg'], diagram_data['mkb'], diagram_data['service']])),
                    ),
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(self.__diagram.add_diagram(2, [diagram_data['region'], diagram_data['area'], diagram_data['med_profile']])),
                    ),
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(self.__diagram.add_diagram(3, [diagram_data['users'][0], diagram_data['users'][1], diagram_data['users'][2], diagram_data['users'][3]])),
                            ),
                        ],
                        vertical_alignment=CrossAxisAlignment.START,
                        alignment=MainAxisAlignment.SPACE_AROUND,
                    ),
                ),
            ],
                expand=True,
            )
        )
        pg.page.update()
        plt.close()