#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
from modules.utilites import word_wrap, unparse_json

#################################################


class Content(UserControl):
    def __init__(self, db):
        super().__init__()
        self.__db = db
        self.__c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
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
                                DataColumn(Text(value='ID', size=15)),
                                DataColumn(Text(value='Роль', size=15)),
                                DataColumn(Text(value='ФИО', size=15)),
                                DataColumn(Text(value='Фото', size=15)),
                                DataColumn(Text(value='Дата создания', size=15)),
                                DataColumn(Text(value='E-mail', size=15)),
                                DataColumn(Text(value='Телефон', size=15)),
                                DataColumn(Text(value='Агент', size=15)),
                                DataColumn(Text(value='Заблокирован', size=15)),
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

    def switchbnt(self):
        pass

    def generate_carts(self):
        carts = list()
        roles = {0: 'Администратор', 1: 'Модератор', 2: 'Куратор', 3: 'Пользователь'}
        data = list()
        raw_data = self.__db.get_data(
            f'SELECT id, role, full_name, photo, date_create, email, phone_number, agent, blocked FROM users ORDER BY id DESC LIMIT 15 OFFSET {(self.__c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row == 1:
                    l1.append(roles[row])
                elif row == 2:
                    fio = unparse_json(rows[row])
                    l1.append(f'{fio[0]}\n{fio[1]}\n{fio[2]}')
                elif row == 4:
                    l1.append(rows[row].strftime('%Y-%m-%d %H:%M:%S'))
                elif row in [7, 8]:
                    if rows[row] == 1:
                        l1.append(True)
                    else:
                        l1.append(False)
                else:
                    l1.append(rows[row])
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
                        DataCell(Switch(value=cart[7], on_change=self.switchbnt)),
                        DataCell(Switch(value=cart[8], on_change=self.switchbnt)),
                        DataCell(IconButton(icon=icons.MODE_EDIT_OUTLINE_OUTLINED, tooltip='Изменить')),
                        DataCell(IconButton(icon=icons.DELETE, tooltip='Удалить')),
                    ],
                )
            )
        return carts


class user_ui(UserControl):
    def __init__(self, pg, db):
        super().__init__()
        self.__pg = pg
        self.__db = db

    def add(self, event):
        self.__pg.navigator.navigate('users_change_users', self.__pg.page)

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(icon=icons.ADD,
                                  text='Создать', on_click=self.add)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
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
                        content=Text(value='Пользователи', size=20),
                        padding=padding.only(left=60, right=60, top=20)
                    ),
                    Container(
                        content=Row([btn_create, pb]),
                        padding=padding.only(left=50, top=10)
                    ),
                    Container(
                        content=Content(self.__db)
                    ),
                    Container(
                        content=Row([btn_next_page1, btn_next_page2, btn_next_page3]),
                        alignment=alignment.bottom_center,
                        padding=padding.only(top=10, left=50),
                    ),
                ],
                scroll=ScrollMode.ALWAYS,
                expand=True,
                alignment=MainAxisAlignment.START,
            ),
        )


class User:
    def __init__(self, vault, config, db):
        super().__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db

    def user(self, pg: PageData):
        pg.page.title = "Пользователи"
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
                        ),
                    ),
                    Container(
                        border_radius=10,
                        expand=True,
                        content=user_ui(pg, self.__db),
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
