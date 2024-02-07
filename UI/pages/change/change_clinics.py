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
            for x in range(23):
                self.__existed_data.append('')
        self.__data[0] = TextField(label='Название', value=self.__existed_data[0])
        self.__data[1] = Dropdown(hint_text='Медицинские профили', options=self.load_region(), value=self.__existed_data[1])
        self.__data[2] = Dropdown(hint_text='Модератор', options=self.load_region(), value=self.__existed_data[1])
        self.__data[3] = TextField(label="Коэффициент дифференциации", value=self.__existed_data[0], suffix_text="В формате 9.99 (не >9.99)")
        self.__data[4] = TextField(label="Базовая ставка", value=self.__existed_data[0], suffix_text="В формате 99999.99 (не >99999.99)")
        self.__data[5] = TextField(label="Сайт", value=self.__existed_data[0], prefix_text="https://", suffix_text=".com")
        self.__data[6] = TextField(label="Телефон", value=self.__existed_data[0], prefix_text="+7")
        self.__data[7] = TextField(label="E-mail", value=self.__existed_data[0])
        other_contacts = DataTable(
            border_radius=10,
            width=1500,
            border=border.all(2, "black"),
            columns=[
                DataColumn(Text("#")),
                DataColumn(Text("Тип")),
                DataColumn(Text("Значение")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text(value="1")),
                        DataCell(TextField(label="Тип", )),
                        DataCell(TextField(label="Значение")),
                ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="2")),
                        DataCell(TextField(label="Тип")),
                        DataCell(TextField(label="Значение")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="3")),
                        DataCell(TextField(label="Тип")),
                        DataCell(TextField(label="Значение")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="4")),
                        DataCell(TextField(label="Тип")),
                        DataCell(TextField(label="Значение")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="5")),
                        DataCell(TextField(label="Тип")),
                        DataCell(TextField(label="Значение")),
                    ]
                ),
            ]
        )
        self.__data[8] = Dropdown(hint_text='Регион', options=[dropdown.Option("Центральный федеральный округ"),
                                                       dropdown.Option("Южный федеральный округ"),
                                                       dropdown.Option("Уральский федеральный округ")])
        self.__data[9] = Dropdown(hint_text='Область',
                        options=[dropdown.Option("Белгородская область"), dropdown.Option("Брянская область"),
                                 dropdown.Option("Владимирская область")])
        self.__data[10] = TextField(label="Город")
        self.__data[11] = TextField(label="Адрес")
        self.__data[12] = TextField(label="Номер договора")
        self.__data[13] = TextField(label="Управляющий клиники")
        self.__data[14] = TextField(label="Должность управляющего")
        self.__data[15] = TextField(label="ИНН")
        self.__data[16] = TextField(label="КПП")
        self.__data[17] = TextField(label="ОГРН")
        self.__data[18] = TextField(label="Почтовый индекс")
        self.__data[19] = TextField(label="Название банка")
        self.__data[20] = TextField(label="Корреспондентский счет")
        self.__data[21] = TextField(label="БИК")
        self.__data[22] = FilledButton(text='Сохранить')
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
                            Text(value='Информация о заявке', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Divider(height=10),
                        Container(
                            Text(value='Базовые', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[0], padding=padding.only(left=50, right=50)),
                        Container(self.__data[1], padding=padding.only(left=50, right=50)),
                        Container(self.__data[2], padding=padding.only(left=50, right=50)),
                        Container(self.__data[3], padding=padding.only(left=50, right=50)),
                        Container(self.__data[4], padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Контакты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[5], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[6], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[7], padding=padding.only(left=50, right=50, top=10)),
                        Container(other_contacts, padding=padding.only(left=50, right=50, top=10)),
                        Divider(height=10),
                        Container(
                            Text(value='Расположение', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[8], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[9], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[10], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[11], padding=padding.only(left=50, right=50, top=10)),
                        Divider(height=10),
                        Container(
                            Text(value='Реквизиты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[12], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[13], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[14], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[15], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[16], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[17], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[18], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[19], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[20], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[21], padding=padding.only(left=50, right=50, top=10)),
                        Container(self.__data[22], padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                    scroll=ScrollMode.ALWAYS,
                    )
                )
            )
        )

class change_clinics:
    def __init__(self, vault, config, db):
        super(change_clinics, self).__init__()
        self.__save = None
        self.__bik = None
        self.__correspondent_account = None
        self.__bank_name = None
        self.__postcode = None
        self.__ogrn = None
        self.__kpp = None
        self.__tin = None
        self.__position_manager = None
        self.__clinic_manager = None
        self.__contract_number = None
        self.__address = None
        self.__city = None
        self.__area = None
        self.__region = None
        self.__other_contacts = None
        self.__email = None
        self.__phone = None
        self.__phone = None
        self.__site = None
        self.__base_rate = None
        self.__diff_coefficient = None
        self.__moderator = None
        self.__medical_profiles = None
        self.__name = None
        self.__states = None
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__load_drop_box = LoadDropBox(db)
        self.__load_pages = LoadPages(db)
        self.__process_data = ProcessData()
        self.__data_buttons = [self.__name, self.__medical_profiles, self.__moderator, self.__diff_coefficient,
                               self.__base_rate, self.__site, self.__phone, self.__email, self.__other_contacts,
                               self.__region, self.__area, self.__city, self.__address, self.__contract_number,
                               self.__clinic_manager, self.__position_manager, self.__tin, self.__kpp, self.__ogrn,
                               self.__postcode, self.__bank_name, self.__correspondent_account, self.__bik, self.__save]


    def change_clinics(self, pg: PageData):
        row_id = pg.page.client_storage.get("current_action")[1]
        self.__states = {'add': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db, self.__process_data),
                         'change': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db,
                                           self.__process_data, self.__load_pages, row_id)}
        if row_id is not None:
            name = 'изменить'
        else:
            name = 'создать'
        pg.page.title = f"Клиники - {name}"
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
                        )
                    )
                ],
                expand=True,
            )
        )
        pg.page.update()
