#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
from modules.load_data import LoadDropBox, LoadPages
from modules.process_data import ProcessData


#################################################


class Content(UserControl):
    def __init__(self, load_drop_box, buttons, pg, db, process_data, load_pages=None, row_id=None):
        super().__init__()
        self.__dlg_modal = None
        self.__existed_data = []
        self.__load_drop_box = load_drop_box
        self.__load_pages = load_pages
        self.__process_data = process_data
        self.__row_id = row_id
        self.__data = buttons
        self.__pg = pg
        self.__db = db

    def build(self):
        code = TextField(label="Код")
        name = TextField(label="Название")
        mkb = TextField(label="МКБ")
        csg = TextField(label="КСГ")
        clinical_minimum = DataTable(
            border_radius=10,
            width=1500,
            border=border.all(2, "black"),
            columns=[
                DataColumn(Text("#")),
                DataColumn(Text("Категории")),
                DataColumn(Text("Название")),
                DataColumn(Text("Время действия (Дней)")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text(value="1")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="2")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="3")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="4")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="5")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                )
            ]
        )
        save = FilledButton(text='Сохранить')
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
                content=Column(
                    [
                        Container(
                            Text(value='МКБ - Создать', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Divider(height=10),
                        Container(code, padding=padding.only(left=50, right=50)),
                        Container(name, padding=padding.only(left=50, right=50)),
                        Container(mkb, padding=padding.only(left=50, right=50)),
                        Container(csg, padding=padding.only(left=50, right=50)),
                        Container(
                            Text(value='Клинический минимум', size=14),
                            padding=padding.only(left=50, right=50, top=5, bottom=2),
                        ),
                        Container(clinical_minimum, padding=padding.only(left=50, right=50)),
                        Container(save, padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                    )
                )
            )
        )
class change_service:
    def __init__(self, vault, config, db):
        super(change_service, self).__init__()
        self.__states = None
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__load_drop_box = LoadDropBox(db)
        self.__load_pages = LoadPages(db)
        self.__process_data = ProcessData()

    def change_service(self, pg: PageData):
        row_id = pg.page.client_storage.get("current_action")[1]
        self.__states = {'add': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db, self.__process_data),
                         'change': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db,
                                           self.__process_data, self.__load_pages, row_id)}
        pg.page.title = "Услуги - Создать"
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
                        content=self.__states[pg.page.client_storage.get("current_action")[0]],
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
