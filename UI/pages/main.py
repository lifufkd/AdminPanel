#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from flet_navigator import PageData
from UI.sidebar import SideBar
#################################################


class Main:
    def __init__(self):
        super(Main, self).__init__()

    def main(self, pg: PageData):
        pg.page.title = "Главное меню"
        pg.page.theme_mode = 'dark'
        fig, ax = plt.subplots()

        fruits = ["apple", "blueberry", "cherry", "orange"]
        counts = [40, 100, 30, 55]
        bar_labels = ["red", "blue", "_red", "orange"]
        bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]
        ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

        ax.set_ylabel("fruit supply")
        ax.set_title("Fruit supply by kind and color")
        ax.legend(title="Fruit color")
        pg.page.add(
            Row(
                [
                Container(
                    content=SideBar(),
                ),
                VerticalDivider(width=1),
                Container(
                    bgcolor=colors.BLACK,
                    height=1000,
                    width=1500,
                    content=Row([
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(fig),
                    ),
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(fig),
                    ),
                    Container(
                        height=450,
                        width=450,
                        content=MatplotlibChart(fig),
                            ),
                        ],
                        vertical_alignment=CrossAxisAlignment.START,
                        alignment=MainAxisAlignment.SPACE_AROUND,
                    ),
                ),
            ],
                expand=True,
            )
        )
        pg.page.update()