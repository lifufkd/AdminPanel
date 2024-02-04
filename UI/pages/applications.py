#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
import datetime
from modules.utilites import word_wrap
#################################################


class Content(UserControl):
    def __init__(self, db):
        super().__init__()
        self.__db = db
        self.__c_page = 1 # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        self.__max_len = 30  # перенос слов по 15 символов

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
                                DataColumn(Text(value='Номер', size=15)),
                                DataColumn(Text(value='Тип заявки', size=15)),
                                DataColumn(Text(value='Тип оплаты', size=15)),
                                DataColumn(Text(value='Статус заявки', size=15)),
                                DataColumn(Text(value='Подтверждение факта поступления', size=15)),
                                DataColumn(Text(value='Статус вознаграждения', size=15)),
                                DataColumn(Text(value='Дата создания', size=15)),
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
        data = list()
        pointer = {1: 'application_type', 2: 'payment_type', 3: 'application_status', 4: 'hospitalized', 5: 'benefit_status', 6: 'date_format'}
        raw_data = self.__db.get_data(f'SELECT number, application_type, payment_type, application_status, hospitalized, status, date_create FROM application ORDER BY date_create DESC LIMIT 15 OFFSET {(self.__c_page-1)*15}', ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row in pointer.keys():
                    if row == 6:
                        l1.append(rows[row].strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        l1.append(word_wrap(self.__db.get_data(f'SELECT title FROM {pointer[row]} WHERE id = {rows[row]}', ())[0][0], self.__max_len))
                else:
                    l1.append(word_wrap(rows[row], self.__max_len))
            data.append(l1)
        for cart in data:
            carts.append(
                DataRow(
                    cells=[
                        DataCell(Text(cart[0])),
                        DataCell(Text(cart[1])),
                        DataCell(Text(cart[2])),
                        DataCell(Text(cart[3])),
                        DataCell(Text(cart[4])),
                        DataCell(Text(cart[5])),
                        DataCell(Text(cart[6])),
                        DataCell(IconButton(icon=icons.MODE_EDIT_OUTLINE_OUTLINED, tooltip='Изменить')),
                        DataCell(IconButton(icon=icons.DELETE, tooltip='Удалить')),

                    ]
                )
            )
        return carts


class application_ui(UserControl):
    def __init__(self, pg, db):
        super().__init__()
        self.__pg = pg
        self.__db = db

    def add(self, event):
        self.__pg.navigator.navigate('applications_change_applications', self.__pg.page)

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(icon=icons.ADD, text='Создать', on_click=self.add)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
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
                        content=Text(value='Заявки', size=20),
                        padding=padding.only(left=60, right=60, top=20)
                    ),
                    Container(
                        content=Row([btn_create, pb]),
                        padding=padding.only(left=50, top=10)
                    ),
                    Container(
                        content=Content(self.__db),
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


class Application:
    def __init__(self, vault, config, db):
        super(Application, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db

    def application(self, pg: PageData):
        pg.page.title = "Заявки"
        pg.page.theme_mode = 'dark'
        pg.page.vertical_alignment = MainAxisAlignment.CENTER
        pg.page.horizontal_alignment = CrossAxisAlignment.CENTER
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
                        content=application_ui(pg, self.__db),
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        ),
                    )
                ],
                expand=True,
            )
        )
        pg.page.update()
