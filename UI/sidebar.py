#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
#################################################


class SideBar(UserControl):
    def __init__(self, vault, pg):
        super().__init__()
        self.__buttonnames = ['Заявки', 'Клиники', 'Пользователи', 'Услуги', 'Справочники', 'Выйти', 'Пользователь']
        self.__user_info = pg.page.session.get(vault[0])

    def navigation(self, e): #настроки для навигации
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
        elif self.__buttonnames[6] == e.control.tooltip:
            print('Пользователь')

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
            on_click=lambda e: self.navigation(e),
            tooltip='Пользователь',
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
                    self.UserData(f'{self.__user_info[1][0][0].upper()}{self.__user_info[1][1][0].upper()}', f'{self.__user_info[1][0]} {self.__user_info[1][1]}', self.__user_info[2]),  # инициалы челов
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