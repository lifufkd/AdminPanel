#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from flet_navigator import PageData
#################################################


class SideBar(UserControl):
    def __init__(self):
        super().__init__()
        self.__buttonnames = ['Заявки', 'Клиники', 'Пользователи', 'Услуги', 'Справочники', 'Выйти']

    def navigation(self, e):
        if self.__buttonnames[0] == e.control.tooltip:
            print('Заявка')
        elif self.__buttonnames[1] == e.control.tooltip:
            print('Клиники')
        elif self.__buttonnames[2] == e.control.tooltip:
            print('Пользователи')
        elif self.__buttonnames[3] == e.control.tooltip:
            print('Услуги')
        elif self.__buttonnames[4] == e.control.tooltip:
            print('Справочники')
        elif self.__buttonnames[5] == e.control.tooltip:
            print('Выйти')

    def HighLight(self, e):
        # хуйня чтобы подсвечивались кнопки в сайдбаре
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].color = "white54"
            e.control.update()

    def UserData(self, initials: str, name: str, descriptions: str):
        return Container(
            content=Row(
                controls=[
                    Container(  # это квадрат с инициалами NT типа
                        width=42,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=22,
                            weight="bold",
                        ),
                    ),
                    Column(
                        spacing=1,
                        alignment='center',
                        controls=[
                            Text(  # текст с именем и фамилией
                                value=name,
                                size=15,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200  # скорость анимации
                            ),
                            Text(
                                value=descriptions, #Frontend dev
                                size=12,
                                weight='w400',
                                color="white54",
                                opacity=1,
                                animate_opacity=200,  # скорость анимации
                            )
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.navigation(e),
            tooltip=text,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=15,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]

            )
        )

    def build(self):
        return Container(
            padding=30,
            content=Column(
                controls=[
                    # сюда иконки хуярить, будут в столбик
                    self.UserData("NT", "Nikita Tsapkov", "Frontend Developer"),  # инициалы челов
                    # разделитель
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon(icons.REQUEST_PAGE, self.__buttonnames[0]),
                    self.ContainedIcon(icons.BUSINESS_OUTLINED, self.__buttonnames[1]),
                    self.ContainedIcon(icons.SUPERVISED_USER_CIRCLE, self.__buttonnames[2]),
                    # под пользователями еще 2 кнопки
                    self.ContainedIcon(icons.ATTACH_MONEY, self.__buttonnames[3]),
                    # под услугами еще 4 кнопки
                    self.ContainedIcon(icons.DEHAZE_OUTLINED, self.__buttonnames[4]),
                    # под справочниками еще 3 кнопки
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, self.__buttonnames[5]),
                ]
            ),
        )


class Main:
    def __init__(self):
        super(Main, self).__init__()

    def main(self, pg: PageData):
        pg.page.title = "Главное меню"
        pg.page.theme_mode = 'dark'
        fig, ax = plt.subplots()

        fruits = ["apple", "blueberry", "cherry", "orange"]
        counts = [40, 100, 30, 55]
        bar_labels = ["red", "blue", "_red", "orange"]
        bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]
        logout = SideBar()
        ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

        ax.set_ylabel("fruit supply")
        ax.set_title("Fruit supply by kind and color")
        ax.legend(title="Fruit color")
        pg.page.add(
            Row(
                [
                Container(
                    content=SideBar(),
                ),
                VerticalDivider(width=1),
                Container(
                    bgcolor=colors.BLACK,
                    height=1000,
                    width=1500,
                    content=Row([
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(fig),
                    ),
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(fig),
                    ),
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(fig),
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