#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
#################################################

class Content(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return (Container
(
            padding=padding.only(left=30, right=30, top=15),
            expand=True,
            content=Container
                (
                shadow=BoxShadow
                    (
                    spread_radius=0.5,
                    blur_radius=15,
                    color=colors.BLUE_GREY_300,
                    offset=Offset(0, 0),
                    blur_style=ShadowBlurStyle.OUTER,
                ),
                border_radius=10,
                content=Row(
                    [
                        DataTable(
                            columns=
                            [
                                DataColumn(Text(value='Название', size=15)),
                                DataColumn(Text(value='Медецинские профили', size=15)),
                                DataColumn(Text(value='Сайт', size=15)),
                                DataColumn(Text(value='Телефон', size=15)),
                                DataColumn(Text(value='E-mail', size=15)),
                                DataColumn(Text(value='', size=15)),
                                DataColumn(Text(value='', size=15)),
                            ],
                            rows=self.generate_carts()
                        )
                    ]
                )
            )
        )
        )

    def generate_carts(self):
        carts = list()
        test = [['ЧУЗ "КБ "РЖД-Медицина" г. Красноярск', 'Травматология и ортопедия', 'https://dkb24.ru/', '+7 (391) 229-22-22', 'info@med54.ru'],
                ['ЧУЗ "КБ "РЖД-Медицина" г. Новосибирск', 'Травматология и ортопедия\nСердечно-сосудистая хирургия\nУрология\nОнкология', 'https://novosibirsk.rzd-medicine.ru/', '+7 (383) 328-19-19', 'info@med54.ru']]
        for cart in test:
            carts.append(
                DataRow(
                    cells=[
                        DataCell(Text(cart[0])),
                        DataCell(Text(cart[1])),
                        DataCell(Text(cart[2])),
                        DataCell(Text(cart[3])),
                        DataCell(Text(cart[4])),
                        DataCell(IconButton(icon=icons.MODE_EDIT_OUTLINE_OUTLINED, tooltip='Изменить')),
                        DataCell(IconButton(icon=icons.DELETE, tooltip='Удалить')),
                    ]
                )
            )
        return carts


class clinics_ui(UserControl):
    def __init__(self, pg):
        super().__init__()
        self.__pg = pg

    def add(self, event):
        self.__pg.navigator.navigate('clinics_change_clinics', self.__pg.page)

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(icon=icons.ADD, text='Создать',
                                  width=130, on_click=self.add)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
        btn_next_page1 = FilledButton(text='1', tooltip='thispage')
        btn_next_page2 = FilledButton(text='2', tooltip='nextpage2')
        btn_next_page3 = FilledButton(text='3', tooltip='nextpage3')
        pb = PopupMenuButton(
            items=[
                PopupMenuItem(icon=icons.CLOUD_DOWNLOAD, text='Экспорт')
            ]
        )

        return Container(
            height=1500,
            content=Column(
                [
                    Container(
                        content=Text(value='Клиники', size=20),
                        padding=padding.only(left=60, right=60, top=20)
                    ),
                    Container(
                        content=Row([btn_create, pb]),
                        padding=padding.only(left=50, top=10)
                    ),
                    Container(
                        content=Content()
                    ),
                    Container(
                        content=Row([btn_next_page1, btn_next_page2, btn_next_page3]),
                        alignment=alignment.bottom_center,
                        padding=padding.only(top=10, left=50),
                    ),
                ],
                expand=True,
                alignment=MainAxisAlignment.START,
            ),
        )
class Clinic:
    def __init__(self, vault, config, db):
        super(Clinic, self).__init__()
        self.__vault = vault
        self.__config = config

    def clinic(self, pg: PageData):
        pg.page.title = "Клиники"
        pg.page.theme_mode = 'dark'
        pg.page.add(
            Row(
                [
                    Container(
                        border_radius=10,
                        content=SideBar(self.__vault, pg),
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        )
                    ),
                    Container(
                        border_radius=10,
                        expand=True,
                        content=clinics_ui(pg),
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        )
                    )

                ],
                expand=True,
            )
        )
        pg.page.update()
