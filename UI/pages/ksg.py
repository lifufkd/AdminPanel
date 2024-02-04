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
    def __init__(self, db):
        super().__init__()
        self.__db = db
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
                                DataColumn(Text(value='Код', size=15)),
                                DataColumn(Text(value='Название', size=15)),
                                DataColumn(Text(value='Стоимость', size=15)),
                                DataColumn(Text(value='Коэффициент уровня мед учреждения', size=15)),
                                DataColumn(Text(value='МКБ', size=15)),
                                DataColumn(Text(value='Услуги', size=15)),
                                DataColumn(Text(value='Мед. профили', size=15)),
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
        raw_data = self.__db.get_data(
            f'SELECT name, med_profiles, site, phone_number, email FROM hospital ORDER BY name DESC LIMIT 15 OFFSET {(self.__c_page - 1) * 15}',
            ())
        for rows in raw_data:
            l1 = []
            for row in range(len(rows)):
                if row == 1:
                    profiles = ''
                    for item in unparse_json(rows[row]):
                        profiles += self.__db.get_data(f'SELECT med_profile FROM med_profile WHERE id = {item}', ())[0][
                                        0] + ', '
                    l1.append(word_wrap(profiles, self.__max_len))
                else:
                    l1.append(word_wrap(rows[row], self.__max_len))
            data.append(l1)
        test = [['st38.001', 'Соматические заболевания, осложненные старческой астенией', '8263', '192', '0', '1'],
                ['st37.026', 'Продолжительная медицинская реабилитация пациентов с\nзаболеваниями центральной нервной системы и с\nзаболеваниями опорно-двигательного аппарата и\nпериферической нервной системы (сестринский уход)', '32988', '0', '7','1']]
        for cart in test:
            carts.append(
                DataRow(
                    cells=[
                        DataCell(Text(cart[0])),
                        DataCell(Text(cart[1])),
                        DataCell(Text(cart[2])),
                        DataCell(Switch(value=False, on_change=self.switchbnt())),
                        DataCell(Text(cart[3])),
                        DataCell(Text(cart[4])),
                        DataCell(Text(cart[5])),
                        DataCell(IconButton(icon=icons.MODE_EDIT_OUTLINE_OUTLINED, tooltip='Изменить')),
                        DataCell(IconButton(icon=icons.DELETE, tooltip='Удалить')),
                    ]
                )
            )
        return carts


class ksg_ui(UserControl):
    def __init__(self, pg, db):
        super().__init__()
        self.__pg = pg
        self.__db = db

    def add(self, event):
        self.__pg.navigator.navigate('ksg_change_ksg', self.__pg.page)


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
                        content=Text(value='КСГ', size=20),
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
                expand=True,
                alignment=MainAxisAlignment.START,
            ),
        )

class Ksg:
    def __init__(self, vault, config, db):
        super(Ksg, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db

    def ksg(self, pg: PageData):
        pg.page.title = "КСГ"
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
                        content=ksg_ui(pg, self.__db),
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
