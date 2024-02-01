#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import flet as ft
from modules.utilites import get_data_main_page
from flet_navigator import PageData
#################################################


class Log_in:
    def __init__(self, vault, config, db):
        super(Log_in, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db

    def log_in(self, pg: PageData):
        pg.page.title = "Вход"
        pg.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        images = ft.Row()
        for i in range(1):
            images.controls.append(
                ft.Image(
                    src=f'{self.__config["logo_path"]}',
                    width=420,
                )
            )
        pg.page.update()

        def login(event):
            user_data = self.__db.authorization(user_login.value, user_pass.value)
            if user_data is not None:
                pg.page.session.set(self.__vault[0], user_data)
                pg.navigator.navigate('main', pg.page)
            else:
                print(get_data_main_page(self.__db))

        def validate(event):
            if all([user_login.value, user_pass.value]):
                btn_login.disabled = False
            else:
                btn_login.disabled = True
            pg.page.update()

        user_login = ft.TextField(label='Логин', width=400, on_change=validate)
        user_pass = ft.TextField(label='Пароль', width=400, on_change=validate)
        btn_login = ft.OutlinedButton(text='Войти', width=400, on_click=login, disabled=True)
        btn_save = ft.Checkbox(label='Запомнить', value=False)
        title_text = ft.Text(value='Добро пожаловать в SherDOC -\nздоровье это элементарно!',
                             text_align=ft.TextAlign.CENTER, size=20)
        under_text = ft.Text(value='Пожалуйста, войдите в свою учетную запись', size=15, text_align=ft.TextAlign.CENTER,
                             color='grey')

        pg.page.add(
            ft.Row(
                [
                    images
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            title_text
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    under_text
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            user_login,
                            user_pass,
                            btn_login,
                            btn_save
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )




