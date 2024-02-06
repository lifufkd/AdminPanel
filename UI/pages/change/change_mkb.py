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
    def close_dlg(self, e):
        self.__dlg_modal.open = False
        self.__pg.page.update()

    def open_dlg_modal(self, e):
        self.__pg.page.dialog = self.__dlg_modal
        self.__dlg_modal.open = True
        self.__pg.page.update()

    def dlg_modal(self, data):
        self.__dlg_modal = AlertDialog(
            modal=True,
            title=Text(data[0]),
            content=Text(data[1]),
            actions=[
                TextButton("Ok", on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def save_changes(self, e):
        data = self.__process_data.area(self.__data)
        if self.__row_id is None:
            try:
                insert_data_area(self.__db, 'area', data)
                self.init_dlg(True)
            except:
                self.init_dlg(False)
        else:
            try:
                update_data_area(self.__db, 'area', data, self.__row_id)
                self.init_dlg(True)
            except:
                self.init_dlg(False)

    def init_dlg(self, switch):
        if switch:
            self.dlg_modal(['Данные успешно сохранены!', 'god damn right'])
            self.open_dlg_modal(None)
        else:
            self.dlg_modal(['Данные не сохранены', 'дополните заявку'])
            self.open_dlg_modal(None)

    def existed_data(self):
        return self.__load_pages.application(self.__row_id)


    def build(self):
        if self.__row_id is not None:
            self.existed_data = self.existed_data()
        else:
            for x in range(5):
                self.__existed_data.append('')
        self.__data[0] = TextField(label="Код", value=self.__existed_data[0])
        self.__data[1] = TextField(label="Название", value=self.__existed_data[0])
        self.__data[2] = TextField(label="КСГ", value=self.__existed_data[0])
        self.__data[3] = TextField(label="Услуги", value=self.__existed_data[0])
        self.__data[4] = FilledButton(text='Сохранить')
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
                        DataCell(TextField(label="Название",)),
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
                        Container(self.__data[0], padding=padding.only(left=50, right=50)),
                        Container(self.__data[1], padding=padding.only(left=50, right=50)),
                        Container(self.__data[2], padding=padding.only(left=50, right=50)),
                        Container(self.__data[3], padding=padding.only(left=50, right=50)),
                        Container(
                            Text(value='Клинический минимум', size=14),
                            padding=padding.only(left=50, right=50, top=5, bottom=2),
                        ),
                        Container(clinical_minimum, padding=padding.only(left=50, right=50)),
                        Container(self.__data[4], padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                    )
                )
            )
        )
class change_mkb:
    def __init__(self, vault, config, db):
        super(change_mkb, self).__init__()
        self.__save = None
        self.__service = None
        self.__csg = None
        self.__name = None
        self.__code = None
        self.__states = None
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__load_drop_box = LoadDropBox(db)
        self.__load_pages = LoadPages(db)
        self.__process_data = ProcessData()

    def change_mkb(self, pg: PageData):
        row_id = pg.page.client_storage.get("current_action")[1]
        self.__states = {'add': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db, self.__process_data),
                         'change': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db,
                                           self.__process_data, self.__load_pages, row_id)}
        self.__data_buttons = [self.__code, self.__name, self.__csg, self.__service, self.__save]
        if row_id is not None:
            name = 'изменить'
        else:
            name = 'создать'
        pg.page.title = f"МКБ - {name}"
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
