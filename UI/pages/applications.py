#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
from modules.utilites import save_export_xlsx, delete_row
from modules.load_data import LoadData
#################################################


class Content(UserControl):
    def __init__(self, load_data, config, pg, db):
        super().__init__()
        self.__dlg_modal = None
        self.__load_data = load_data
        self.__config = config
        self.__pg = pg
        self.__db = db

    def delete_row(self, event):
        delete_row(self.__db, {'application': ['id', event.control.tooltip]})
        self.__pg.page.update()

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
        for cart in self.__load_data.application():
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
                        DataCell(IconButton(icon=icons.DELETE, tooltip=cart[7], on_click=self.delete_row)),

                    ]
                )
            )
        return carts


class application_ui(UserControl):
    def __init__(self, pg, load_data, config, db):
        super().__init__()
        self.__pg = pg
        self.__load_data = load_data
        self.__config = config
        self.__db = db

    def add(self, event):
        self.__pg.page.client_storage.set("current_action", "add")
        self.__pg.navigator.navigate('applications_change_applications', self.__pg.page)

    def create_export(self, event):
        save_export_xlsx(self.__config['export_xlsx_path'], self.__load_data.application(), 'applications')

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(icon=icons.ADD, text='Создать', on_click=self.add)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
        btn_next_page1 = FilledButton(text='1', tooltip='thispage')
        btn_next_page2 = FilledButton(text='2', tooltip='nextpage2')
        btn_next_page3 = FilledButton(text='3', tooltip='nextpage3')
        pb = PopupMenuButton(
            items=[
                PopupMenuItem(icon=icons.CLOUD_DOWNLOAD, text='Экспорт', on_click=self.create_export)
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
                        content=Content(self.__load_data, self.__config, self.__pg, self.__db),
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
        self.__load_data = LoadData(db)

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
                        content=application_ui(pg, self.__load_data, self.__config, self.__db),
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
