#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from functools import partial
from modules.utilites import get_data_main_page
from flet_navigator import PageData
#################################################


class SideBar(UserControl):
    def __init__(self):
        super().__init__()

    def HighLight(self, e):
        # хуйня чтобы подсвечивались кнопки в сайдбаре
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].color = "white54"
            e.control.update()

    def UserData(self, initials: str, name: str, descriptions: str):
        return Container(
            content=Row(
                controls=[
                    Container(  # это квадрат с инициалами NT типа
                        width=42,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=22,
                            weight="bold",
                        ),
                    ),
                    Column(
                        spacing=1,
                        alignment='center',
                        controls=[
                            Text(  # текст с именем и фамилией
                                value=name,
                                size=15,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200  # скорость анимации
                            ),
                            Text(
                                value=descriptions, #Frontend dev
                                size=12,
                                weight='w400',
                                color="white54",
                                opacity=1,
                                animate_opacity=200,  # скорость анимации
                            )
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=15,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]

            )
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                controls=[
                    # сюда иконки хуярить, будут в столбик
                    self.UserData("NT", "Nikita Tsapkov", "Frontend Developer"),  # инициалы челов
                    # разделитель
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon(icons.REQUEST_PAGE, "Заявки"),
                    self.ContainedIcon(icons.BUSINESS_OUTLINED, "Клиники"),
                    self.ContainedIcon(icons.SUPERVISED_USER_CIRCLE, "Пользователи"),
                    # под пользователями еще 2 кнопки
                    self.ContainedIcon(icons.ATTACH_MONEY, "Услуги"),
                    # под услугами еще 4 кнопки
                    self.ContainedIcon(icons.DEHAZE_OUTLINED, "Справочники"),
                    # под справочниками еще 3 кнопки
                    Divider(height=5, color="white24"),
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, "Выйти"),
                ]
            ),
        )


class PieChart(UserControl):
    def __init__(self):
        super().__init__()

    def PieChart(self, page: Page):
        normal_radius = 50
        hover_radius = 60
        normal_title_style = TextStyle(
            size=16, color=colors.WHITE, weight=FontWeight.BOLD
        )
        hover_title_style = TextStyle(
            size=22,
            color=colors.WHITE,
            weight=FontWeight.BOLD,
            shadow=BoxShadow(blur_radius=2, color=colors.BLACK54),
        )

        def on_chart_event(e: PieChartEvent):
            for idx, section in enumerate(chart.sections):
                if idx == e.section_index:
                    section.radius = hover_radius
                    section.title_style = hover_title_style
                else:
                    section.radius = normal_radius
                    section.title_style = normal_title_style
            chart.update()

        chart = PieChart(
            sections=[
                PieChartSection(
                    value=40,
                    title="40%",
                    title_style=normal_title_style,
                    color=colors.BLUE,
                    radius=normal_radius,
                ),
                PieChartSection(
                    value=30,
                    title="30%",
                    title_style=normal_title_style,
                    color=colors.YELLOW,
                    radius=normal_radius,
                ),
                PieChartSection(
                    value=15,
                    title="15%",
                    title_style=normal_title_style,
                    color=colors.PURPLE,
                    radius=normal_radius,
                ),
                PieChartSection(
                    value=15,
                    title="15%",
                    title_style=normal_title_style,
                    color=colors.GREEN,
                    radius=normal_radius,
                ),
            ],
            sections_space=0,
            center_space_radius=40,
            on_chart_event=on_chart_event,
            expand=True,
        )
        page.add(chart)


class Main:
    def __init__(self):
        super(Main, self).__init__()

    def main(self, pg: PageData):
        pg.page.title = "Главное меню"
        pg.page.theme_mode = 'dark'
        pg.page.vertical_alignment = MainAxisAlignment.CENTER
        pg.page.horizontal_alignment = MainAxisAlignment.CENTER
        pg.page.add(
            Container(
                width=200,
                height=1000,
                bgcolor='black',
                border_radius=10,
                animate=animation.Animation(500, 'decelerate'),  # анимация для сайдбара
                alignment=alignment.center,
                padding=10,
                content=SideBar(),
            )
        )
        pg.page.add(
            Container(
                width=1000,
                height=500,
                bgcolor='black',
                border_radius=10,
                animate=animation.Animation(500, 'decelerate'),  # анимация для сайдбара
                alignment=alignment.center,
                padding=10,
                content=PieChart(),
            )
        )
        pg.page.update()