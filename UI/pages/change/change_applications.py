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
        number = TextField(label='Номер')
        application_type = Dropdown(hint_text='Тип заявки', options=[dropdown.Option("Быстрая заявка"), dropdown.Option("Обычная заявка")])
        payment_type = Dropdown(hint_text='Тип оплаты', options=[dropdown.Option("ОМС"), dropdown.Option("ПМУ")])
        application_status = Dropdown(hint_text='Статус заявки', options=[dropdown.Option("Черновик"), dropdown.Option("Быстрая заявка"), dropdown.Option("Модерация"), dropdown.Option("Новая заявка"), dropdown.Option("На рассмотрении"), dropdown.Option("Согласование даты"), dropdown.Option("Лист ожидания"), dropdown.Option("Согласование направления"), dropdown.Option("В работе"), dropdown.Option("Завершено"), dropdown.Option("Закрыто пользователем"), dropdown.Option("Закрыто куратором")])
        author_of_closing_request = Dropdown(hint_text='Автор закрытия заявки', options=[dropdown.Option("No choices to choose form")])
        patient = Dropdown(hint_text='Пациент', options=[dropdown.Option("No choices to choose form")])
        mkb = Dropdown(hint_text='МКБ', options=[dropdown.Option("No choices to choose form")])
        service = Dropdown(hint_text='Услуга', options=[dropdown.Option("No choices to choose form")])
        chronic_diseases = TextField(label="Хронические заболевания")
        comment_at_checkout = TextField(label="Комментарий при оформлении")
        comment = TextField(label="Комментарий")
        cost = TextField(label="Стоимость")
        author_of_the_application = Dropdown(hint_text='Автор заявки', options=[dropdown.Option("No choices to choose form")])
        confirmation_of_receipt = Dropdown(hint_text='Подтверждение факта поступления', options=[dropdown.Option("Не госпитализирован"), dropdown.Option("Госпитализирован")])
        clinic = Dropdown(hint_text='Клиника', options=[dropdown.Option("No choices to choose form")])
        reward = TextField(label="Вознаграждение")
        reward_status = Dropdown(hint_text='Статус вознаграждения', options=[dropdown.Option("В обработке"), dropdown.Option("Начислено"), dropdown.Option("Выплачено")])
        date_of_creation = TextField(label="Дата создания")
        date_of_notifications = TextField(label="Дата уведомления")
        date_of_hospitalization = TextField(label="Дата госпитализации")
        application_closing_date = TextField(label="Дата закрытия заявки")
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
                        Container(number, padding=padding.only(left=50, right=50)),
                        Container(application_type, padding=padding.only(left=50, right=50)),
                        Container(payment_type, padding=padding.only(left=50, right=50)),
                        Container(application_status, padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Болезнь', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(patient, padding=padding.only(left=50, right=50)),
                        Container(mkb, padding=padding.only(left=50, right=50)),
                        Container(service, padding=padding.only(left=50, right=50)),
                        Container(chronic_diseases, padding=padding.only(left=50, right=50)),
                        Container(comment_at_checkout, padding=padding.only(left=50, right=50)),
                        Container(comment, padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Финансы', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(cost, padding=padding.only(left=50, right=50)),
                        Container(author_of_the_application, padding=padding.only(left=50, right=50)),
                        Container(confirmation_of_receipt, padding=padding.only(left=50, right=50)),
                        Container(clinic, padding=padding.only(left=50, right=50)),
                        Container(reward, padding=padding.only(left=50, right=50)),
                        Container(reward_status, padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Даты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(date_of_creation, padding=padding.only(left=50, right=50)),
                        Container(date_of_notifications, padding=padding.only(left=50, right=50)),
                        Container(date_of_hospitalization, padding=padding.only(left=50, right=50)),
                        Container(application_closing_date, padding=padding.only(left=50, right=50)),
                        Container(save, padding=padding.only(left=50, right=50, top=10, bottom=10)),
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

    def change_application(self, pg: PageData):
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
                        content=Content(),
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
