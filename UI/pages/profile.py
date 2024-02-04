#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar


#################################################


class ChangeProfile(UserControl):
    def __init__(self):
        super().__init__()

    def savechanges(self):
        pass

    def build(self):
        #ЗНАЧЕНИЯ#
        user_name = TextField(label='Имя')
        user_pass = TextField(label='Пароль', password=True)
        user_pass_confirm = TextField(label='Подтвердите пароль', password=True)
        user_login = TextField(label='Логин')
        btn_save = OutlinedButton(text='Сохранить', width=200, on_click=self.savechanges)

        return Container(
            height=1500,
            content=Column(
                [
                    Container(
                        content=Text(value='Профиль', size=20),
                        padding=padding.only(left=60, right=60, top=20)
                    ),
                    Container(
                        padding=padding.only(left=60, right=60),
                        content=user_name
                    ),
                    Container(
                        padding=padding.only(left=60, right=60),
                        content=user_login
                    ),
                    Container(
                        padding=padding.only(left=60, right=60),
                        content=user_pass
                    ),
                    Container(
                        padding=padding.only(left=60, right=60),
                        content=user_pass_confirm
                    ),
                    Container(
                        padding=padding.only(left=60, right=60),
                        content=btn_save,
                    ),
                ],
                expand=True,
                alignment=MainAxisAlignment.START,
            ),
        )


class Profile:
    def __init__(self, vault, config, db):
        super(Profile, self).__init__()
        self.__vault = vault
        self.__config = config

    def profile(self, pg: PageData):
        pg.page.title = "Профиль"
        pg.page.theme_mode = 'dark'
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
                        content=ChangeProfile(),
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
