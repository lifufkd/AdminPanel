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
        role = Dropdown(hint_text='Роль', options=[dropdown.Option("Admin"), dropdown.Option("Неопределенна"), dropdown.Option("Куратор")])
        name = TextField(label="Имя")
        middle_name = TextField(label="Фамилия")
        last_name = TextField(label="Отчество")
        birthday = TextField(label="День рождения")
        email = TextField(label="E-mail")
        phone = TextField(label="Телефон")
        region = Dropdown(hint_text='Регион', options=[dropdown.Option("Центральный федеральный округ"), dropdown.Option("Южный федеральный округ"), dropdown.Option("Уральский федеральный округ")])
        area = Dropdown(hint_text='Область', options=[dropdown.Option("Белгородская область"), dropdown.Option("Брянская область"), dropdown.Option("Владимирская область")])
        agent = Switch(value=False)
        blocked = Switch(value=False)
        password = TextField(label='Пароль', password=True, can_reveal_password=True)
        password_retry = TextField(label='Повторите пароль', password=True, can_reveal_password=True)
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
                            Text(value='Основная информация', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(role, padding=padding.only(left=50, right=50)),
                        Container(name, padding=padding.only(left=50, right=50)),
                        Container(middle_name, padding=padding.only(left=50, right=50)),
                        Container(last_name, padding=padding.only(left=50, right=50)),
                        Container(birthday, padding=padding.only(left=50, right=50)),
                        Container(email, padding=padding.only(left=50, right=50)),
                        Container(phone, padding=padding.only(left=50, right=50)),
                        Container(region, padding=padding.only(left=50, right=50)),
                        Container(area, padding=padding.only(left=50, right=50)),
                        Container(Text(value='Агент', size=14), padding=padding.only(left=50, right=50, top=7)),
                        Container(agent, padding=padding.only(left=50, right=50)),
                        Container(Text(value='Заблокирован', size=14), padding=padding.only(left=50, right=50, top=7)),
                        Container(blocked, padding=padding.only(left=50, right=50)),
                        Divider(height=5),
                        Container(
                            Text(value='Изменить пароль', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(password, padding=padding.only(left=50, right=50)),
                        Container(password_retry, padding=padding.only(left=50, right=50)),
                        Container(save, padding=padding.only(left=50, right=50, top=10, bottom=10))
                    ],
                        scroll=ScrollMode.ALWAYS,
                    )
                )
            )
        )

class change_users:
    def __init__(self, vault, config, db):
        super(change_users, self).__init__()
        self.__states = None
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__load_drop_box = LoadDropBox(db)
        self.__load_pages = LoadPages(db)
        self.__process_data = ProcessData()

    def change_users(self, pg: PageData):
        row_id = pg.page.client_storage.get("current_action")[1]
        self.__states = {'add': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db, self.__process_data),
                         'change': Content(self.__load_drop_box, self.__data_buttons, pg, self.__db,
                                           self.__process_data, self.__load_pages, row_id)}
        pg.page.title = "Пользователи - Создать"
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
