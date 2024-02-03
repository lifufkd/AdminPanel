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
                                DataColumn(Text(value='Номер', size=15)),
                                DataColumn(Text(value='Тип заявки', size=15)),
                                DataColumn(Text(value='Тип оплаты', size=15)),
                                DataColumn(Text(value='Статус заявки', size=15)),
                                DataColumn(Text(value='Подтверждение факта поступления', size=15)),
                                DataColumn(Text(value='Дата создания', size=15)),
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
        test = [['Артемьева №1 - 10.01.2024', 'Обычная заявка', 'ПМУ', 'Черновик', 'Не госпитализирован', 'В обработке',
                 '10.12.2023 18:34:25'],
                ['Романовский №4 - 09.01.24', 'Обычная заявка', 'ПМУ', 'Черновик', 'Не госпитализирован', 'В обработке',
                 '18.10.2023 19:21:10']]
        for cart in test:
            carts.append(
                DataRow(
                    cells=[
                        DataCell(Text(cart[0])),
                        DataCell(Text(cart[1])),
                        DataCell(Text(cart[2])),
                        DataCell(Text(cart[3])),
                        DataCell(Text(cart[4])),
                        DataCell(Text(cart[5])),
                        DataCell(Text(cart[6]))
                    ]
                )
            )
        return carts


class application_ui(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(text='Создать',
                                  width=110)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
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
                        content=Content()
                    )
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

    def application(self, pg: PageData):
        pg.page.title = "Заявки"
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
                        content=application_ui(),
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
