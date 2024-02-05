#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
#################################################


class ContentFilled(UserControl):
    def __init__(self):
        super().__init__()


class ContentEmpty(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        code = TextField(label="Код")
        name = TextField(label="Название")
        cost = TextField(label="Стоимость")
        cost_ratio = TextField(label="Коэффициент затрат")
        specificity_coefficients = TextField(label="Коэффициенты специфики")
        level_coefficient = TextField(label="Коэффициент уровня")
        share_of_salary_and_other_expenses = TextField(label="Доля зарплаты и прочих расходов")
        coefficient_of_the_medical_institution_level = Switch()
        mkb = TextField(label="МКБ")
        service = TextField(label="Услуги")
        med_profiles = TextField(label="Мед. профили")
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
                            Text(value='Информация о КСГ', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Divider(height=10),
                        Container(
                            Text(value='Базовые', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(code, padding=padding.only(left=50, right=50)),
                        Container(name, padding=padding.only(left=50, right=50)),
                        Container(cost, padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Коэффициенты', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(cost_ratio, padding=padding.only(left=50, right=50)),
                        Container(specificity_coefficients, padding=padding.only(left=50, right=50)),
                        Container(level_coefficient, padding=padding.only(left=50, right=50)),
                        Container(share_of_salary_and_other_expenses, padding=padding.only(left=50, right=50)),
                        Container(
                            Text(value='Коэффициент уровня мед учреждения', size=14),
                            padding=padding.only(left=50, right=50, top=5,),
                        ),
                        Container(coefficient_of_the_medical_institution_level, padding=padding.only(left=50, right=50)),
                        Divider(height=10),
                        Container(
                            Text(value='Связи', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Container(mkb, padding=padding.only(left=50, right=50)),
                        Container(service, padding=padding.only(left=50, right=50)),
                        Container(med_profiles, padding=padding.only(left=50, right=50)),
                        Container(save, padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                        scroll=ScrollMode.ALWAYS,
                    )
                )
            )
        )

class change_ksg:
    def __init__(self, vault, config, db):
        super(change_ksg, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__states = {'add': ContentEmpty(), 'change': ContentFilled()}

    def change_ksg(self, pg: PageData):
        pg.page.title = "КСГ - Создать"
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
