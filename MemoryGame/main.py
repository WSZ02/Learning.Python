import flet
from flet import *
import time
import random



class GenerateGrid(UserControl):
    def __init__(self):
        super().__init__()
        self.grid = Column(opacity=1, animate_opacity=300)
        super().__init__()

    def build(self):
        rows: list = [
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=54,
                        height=54,
                        animate=300,
                        border=border.all(1, "white"),
                        on_click=None,  #change later
                    )
                    for _ in range(5)
                ],
            )
            for _ in range(5)
        ]

        colors: list = ["#5c443b", "#4cbbb5"]

        for row in rows:
            for container in row.controls[:]:
                container.bgcolor = random.choices(colors, weights=[10, 2])[0]

        self.grid.controls = rows
        return self.grid

        pass


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    stage = Text(size=13, weight="bold")
    result = Text(size=16, weight="bold")

    start_button =Container(
        content=ElevatedButton(
        on_click=None, #Change later!
        content=Text("Start!", size=13, weight="bold"),
        style=ButtonStyle(
                shape={"": RoundedRectangleBorder(radius=8)}, color={"": "white"}
            ),
            height=45,
            width=255
        )
    )
    page.add(
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Text(
                    "Memory Game",
                    size=22,
                    weight="bold",
                ),
            ],
        ),
        #Result row
        Row(alignment=MainAxisAlignment.CENTER, controls=[result]),
        Divider(height=10, color="transparent"),
        Divider(height=10, color="transparent"),
        GenerateGrid(),
        #Stage of the game row
        Row(alignment=MainAxisAlignment.CENTER, controls=[stage]),
        Divider(height=10, color="transparent"),
        #Start button
        Row(alignment=MainAxisAlignment.CENTER, controls=[start_button]),
    )


    page.update()

if __name__  == "__main__":
    flet.app(target=main)