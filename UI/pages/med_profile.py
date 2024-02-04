#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from modules.utilites import word_wrap
from UI.sidebar import SideBar
#################################################


class Content(UserControl):
    def __init__(self, db):
        super().__init__()
        self.__db = db
        self.__c_page = 1  # выбор страницы, в поле ввода по умолчанию поставить .value = 1
        self.__max_len = 400  # перенос слов по 15 символов

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
                                DataColumn(Text(value='КСГ', size=15)),
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
        data = list()
        pointer = {1: ['relative_ksg_med_profile', 'id_med_profile']}
        raw_data = self.__db.get_data(
            f'SELECT med_profile, id FROM med_profile ORDER BY med_profile DESC LIMIT 15 OFFSET {(self.__c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row in pointer:
                    l1.append(self.__db.get_quantity(pointer[row][0], [pointer[row][1], rows[1]]))
                else:
                    l1.append(word_wrap(rows[row], self.__max_len))
            data.append(l1)
        for cart in data:
            carts.append(
                DataRow(
                    cells=[
                        DataCell(Text(cart[0])),
                        DataCell(Text(cart[1])),
                        DataCell(IconButton(icon=icons.MODE_EDIT_OUTLINE_OUTLINED, tooltip='Изменить')),
                        DataCell(IconButton(icon=icons.DELETE, tooltip='Удалить')),
                    ]
                )
            )
        return carts


class med_profile_ui(UserControl):
    def __init__(self, pg, db):
        super().__init__()
        self.__pg = pg
        self.__db = db

    def add(self, event):
        self.__pg.navigator.navigate('med_profile_change_med_profile', self.__pg.page)

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(icon=icons.ADD,
                                  text='Создать', on_click=self.add)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
        btn_next_page1 = FilledButton(text='1', tooltip='thispage')
        btn_next_page2 = FilledButton(text='2', tooltip='nextpage2')
        btn_next_page3 = FilledButton(text='3', tooltip='nextpage3')

        return Container(
            height=1500,
            content=Column(
                [
                    Container(
                        content=Text(value='Мед. профили', size=20),
                        padding=padding.only(left=60, right=60, top=20)
                    ),
                    Container(
                        content=Row([btn_create]),
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
                expand=True,
                alignment=MainAxisAlignment.START,
            ),
        )


class Med_profile:
    def __init__(self, vault, config, db):
        super(Med_profile, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db

    def med_profile(self, pg: PageData):
        pg.page.title = "Мед. профили"
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
                        content=med_profile_ui(pg, self.__db),
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