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
        name = TextField(label='Название')
        medical_profiles = Dropdown(hint_text='Медицинские профили', options=[dropdown.Option("Акушерское дело"), dropdown.Option("Гематология"), dropdown.Option("Гериатрия")])
        moderator = Dropdown(hint_text='Модератор', options=[dropdown.Option("No choices to choose form")])
        diff_coefficient = TextField(label="Коэффициент дифференциации")
        base_rate = TextField(label="Базовая ставка")
        site = TextField(label="Сайт")
        phone = TextField(label="Телефон")
        email = TextField(label="E-mail")
        region = Dropdown(hint_text='Регион', options=[dropdown.Option("Центральный федеральный округ"),
                                                       dropdown.Option("Южный федеральный округ"),
                                                       dropdown.Option("Уральский федеральный округ")])
        area = Dropdown(hint_text='Область',
                        options=[dropdown.Option("Белгородская область"), dropdown.Option("Брянская область"),
                                 dropdown.Option("Владимирская область")])
        city = TextField(label="Город")
        address = TextField(label="Адрес")
        contract_number = TextField(label="Номер договора")
        clinic_manager = TextField(label="Управляющий клиники")
        position_manager = TextField(label="Должность управляющего")
        tin = TextField(label="ИНН")
        kpp = TextField(label="КПП")
        ogrn = TextField(label="ОГРН")
        postcode = TextField(label="Почтовый индекс")
        bank_name = TextField(label="Название банка")
        correspondent_account = TextField(label="Корреспондентский счет")
        bik = TextField(label="БИК")
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
                            Text(value='Информация о заявке', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Divider(height=10),
                        Container(
                            Text(value='Базовые', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(name, padding=padding.only(left=50, right=50)),
                        Container(medical_profiles, padding=padding.only(left=50, right=50)),
                        Container(moderator, padding=padding.only(left=50, right=50)),
                        Container(diff_coefficient, padding=padding.only(left=50, right=50)),
                        Container(base_rate, padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Контакты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(site, padding=padding.only(left=50, right=50, top=10)),
                        Container(phone, padding=padding.only(left=50, right=50, top=10)),
                        Container(email, padding=padding.only(left=50, right=50, top=10)),
                        Divider(height=10),
                        Container(
                            Text(value='Расположение', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(region, padding=padding.only(left=50, right=50, top=10)),
                        Container(area, padding=padding.only(left=50, right=50, top=10)),
                        Container(city, padding=padding.only(left=50, right=50, top=10)),
                        Container(address, padding=padding.only(left=50, right=50, top=10)),
                        Divider(height=10),
                        Container(
                            Text(value='Реквизиты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(contract_number, padding=padding.only(left=50, right=50, top=10)),
                        Container(clinic_manager, padding=padding.only(left=50, right=50, top=10)),
                        Container(position_manager, padding=padding.only(left=50, right=50, top=10)),
                        Container(tin, padding=padding.only(left=50, right=50, top=10)),
                        Container(kpp, padding=padding.only(left=50, right=50, top=10)),
                        Container(ogrn, padding=padding.only(left=50, right=50, top=10)),
                        Container(postcode, padding=padding.only(left=50, right=50, top=10)),
                        Container(bank_name, padding=padding.only(left=50, right=50, top=10)),
                        Container(correspondent_account, padding=padding.only(left=50, right=50, top=10)),
                        Container(bik, padding=padding.only(left=50, right=50, top=10)),
                        Container(save, padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                    scroll=ScrollMode.ALWAYS,
                    )
                )
            )
        )

class change_clinics:
    def __init__(self, vault, config, db):
        super(change_clinics, self).__init__()
        self.__vault = vault
        self.__config = config

    def change_clinics(self, pg: PageData):
        pg.page.title = "Клиники - Создать"
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
                        content=Content(),
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
