#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from datetime import datetime
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
from modules.load_data import LoadDropBox
from modules.utilites import insert_data, unparse_json
#################################################


class ContentFilled(UserControl):
    def __init__(self, load_drop_box, buttons, pg, db):
        super().__init__()
        self.__load_drop_box = load_drop_box
        self.__data_buttons = buttons
        self.__pg = pg
        self.__db = db


class ContentEmpty(UserControl):
    def __init__(self, load_drop_box, buttons, pg, db):
        super().__init__()
        self.__dlg_modal = None
        self.__load_drop_box = load_drop_box
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
        cached_data = list()
        required = [11, 15, 17, 18, 19, 20]
        for item in range(len(self.__data) - 1):
            if item == 11:
                try:
                    cached_data.append(int(self.__data[item].value))
                except:
                    cached_data.append(0)
            elif item == 15:
                try:
                    if float(self.__data[item].value) > 9:
                        cached_data.append(9.99)
                    else:
                        cached_data.append(round(float(self.__data[item].value), 2))
                except:
                    cached_data.append(0)
            elif item in required[2:]:
                try:
                    cached_data.append(datetime.strptime(self.__data[item].value, '%m/%d/%y %H:%M'))
                except:
                    cached_data.append(datetime(1970, 1, 1, 0, 0))
            else:
                if self.__data[item].value is None:
                    cached_data.append('')
                else:
                    cached_data.append(self.__data[item].value)
        cached_data.insert(11, b'')
        cached_data.append(0)
        try:
            insert_data(self.__db, 'application', cached_data)
            self.dlg_modal(['Данные успешно сохранены!', 'god damn right'])
            self.open_dlg_modal(None)
        except:
            self.dlg_modal(['Данные не сохранены', 'дополните заявку'])
            self.open_dlg_modal(None)

    def load_application_type(self):
        carts = list()
        for cart in self.__load_drop_box.load_application_type():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def payment_type(self):
        carts = list()
        for cart in self.__load_drop_box.load_payment_type():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def status(self):
        carts = list()
        for cart in self.__load_drop_box.application_status():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def close_author(self):
        carts = list()
        fios = list()
        for fio in self.__load_drop_box.close_author():
            user_fio = unparse_json(fio[0])
            fios.append([f'{user_fio[0]} {user_fio[1]} {user_fio[2]}', fio[1]])
        for cart in fios:
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def mkb(self):
        carts = list()
        for cart in self.__load_drop_box.mkb():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def service(self):
        carts = list()
        for cart in self.__load_drop_box.service():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def hospitalized(self):
        carts = list()
        for cart in self.__load_drop_box.hospitalized():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def hospital(self):
        carts = list()
        for cart in self.__load_drop_box.hospital():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def benefit_status(self):
        carts = list()
        for cart in self.__load_drop_box.benefit_status():
            carts.append(
                dropdown.Option(text=cart[0], key=cart[1])
            )
        return carts

    def build(self):
        self.__data[0] = TextField(label='Номер')
        self.__data[1] = Dropdown(hint_text='Тип заявки', options=self.load_application_type())
        self.__data[2] = Dropdown(hint_text='Тип оплаты', options=self.payment_type())
        self.__data[3] = Dropdown(hint_text='Статус заявки', options=self.status())
        self.__data[4] = Dropdown(hint_text='Автор закрытия заявки', options=self.close_author())
        self.__data[5] = Dropdown(hint_text='Пациент', options=self.close_author())
        self.__data[6] = Dropdown(hint_text='МКБ', options=self.mkb())
        self.__data[7] = Dropdown(hint_text='Услуга', options=self.service())
        self.__data[8] = TextField(label="Хронические заболевания")
        self.__data[9] = TextField(label="Комментарий при оформлении")
        self.__data[10] = TextField(label="Комментарий")
        self.__data[11] = TextField(label="Стоимость")
        self.__data[12] = Dropdown(hint_text='Автор заявки', options=self.close_author())
        self.__data[13] = Dropdown(hint_text='Подтверждение факта поступления', options=self.hospitalized())
        self.__data[14] = Dropdown(hint_text='Клиника', options=self.hospital())
        self.__data[15] = TextField(label="Вознаграждение")
        self.__data[16] = Dropdown(hint_text='Статус вознаграждения', options=self.benefit_status())
        self.__data[17] = TextField(label="Дата создания")
        self.__data[18] = TextField(label="Дата уведомления")
        self.__data[19] = TextField(label="Дата госпитализации")
        self.__data[20] = TextField(label="Дата закрытия заявки")
        self.__data[21] = FilledButton(text='Сохранить', on_click=self.save_changes)
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
                            Text(value='Болезнь', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[5], padding=padding.only(left=50, right=50)),
                        Container(self.__data[6], padding=padding.only(left=50, right=50)),
                        Container(self.__data[7], padding=padding.only(left=50, right=50)),
                        Container(self.__data[8], padding=padding.only(left=50, right=50)),
                        Container(self.__data[9], padding=padding.only(left=50, right=50)),
                        Container(self.__data[10], padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Финансы', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[11], padding=padding.only(left=50, right=50)),
                        Container(self.__data[12], padding=padding.only(left=50, right=50)),
                        Container(self.__data[13], padding=padding.only(left=50, right=50)),
                        Container(self.__data[14], padding=padding.only(left=50, right=50)),
                        Container(self.__data[15], padding=padding.only(left=50, right=50)),
                        Container(self.__data[16], padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Даты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(self.__data[17], padding=padding.only(left=50, right=50)),
                        Container(self.__data[18], padding=padding.only(left=50, right=50)),
                        Container(self.__data[19], padding=padding.only(left=50, right=50)),
                        Container(self.__data[20], padding=padding.only(left=50, right=50)),
                        Container(self.__data[21], padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                    scroll=ScrollMode.ALWAYS,
                    )
                )
            )
        )


class change_applications:
    def __init__(self, vault, config, db):
        super(change_applications, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__load_drop_box = LoadDropBox(db)
        self.__states = None
        self.__save = None
        self.__reward = None
        self.__reward_status = None
        self.__date_of_creation = None
        self.__date_of_notifications = None
        self.__date_of_hospitalization = None
        self.__application_closing_date = None
        self.__clinic = None
        self.__confirmation_of_receipt = None
        self.__author_of_the_application = None
        self.__cost = None
        self.__comment_at_checkout = None
        self.__number = None
        self.__application_type = None
        self.__payment_type = None
        self.__application_status = None
        self.__author_of_closing_request = None
        self.__patient = None
        self.__mkb = None
        self.__service = None
        self.__comment = None
        self.__chronic_diseases = None
        self.__data_buttons = [self.__number, self.__application_type, self.__payment_type, self.__application_status,
                       self.__author_of_closing_request, self.__patient, self.__mkb, self.__service,
                       self.__chronic_diseases,
                       self.__comment_at_checkout, self.__comment, self.__cost, self.__author_of_the_application,
                       self.__confirmation_of_receipt, self.__clinic,
                       self.__reward, self.__reward_status, self.__date_of_creation, self.__date_of_notifications,
                       self.__date_of_hospitalization, self.__application_closing_date, self.__save]

    def change_application(self, pg: PageData):
        self.__states = {'add': ContentEmpty(self.__load_drop_box, self.__data_buttons, pg, self.__db),
         'change': ContentFilled(self.__load_drop_box, self.__data_buttons, pg, self.__db)}
        pg.page.title = "Заявки - Создать"
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
                        content=self.__states[pg.page.client_storage.get("current_action")],
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
