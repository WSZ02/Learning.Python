import flet
from flet import *
import time
import random


class GenerateGrid(UserControl):
    def __init__(self, difficulty):
        self.grid = Column(opacity=0, animate_opacity=300)
        self.blue_titles: int = 0
        self.difficulty: int = difficulty
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
                container.bgcolor = random.choices(
                    colors, weights=[10, self.difficulty]
                )[0]
                container.data = container.bgcolor

                if container.bgcolor == "#4cbbb5":
                    self.blue_titles += 1

        self.grid.controls = rows
        return self.grid

        pass


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    stage = Text(size=13, weight="bold")
    result = Text(size=16, weight="bold")

    start_button = Container(
        content=ElevatedButton(
        on_click=lambda e: start_game(e, GenerateGrid(2)),
        content=Text("Start!", size=13, weight="bold"),
        style=ButtonStyle(
                shape={"": RoundedRectangleBorder(radius=8)}, color={"": "white"}
            ),
            height=45,
            width=255
        )
    )

    def start_game(e, level):

        grid = level
        page.controls.insert(
            3, grid
        )
        page.update()

        grid.grid.opacity = 1
        grid.grid.update()

        #change stage number
        stage.value = f"Stage: {grid.difficulty - 1}"
        stage.update()
        #preventing from clicking it twice
        start_button.disabled = True
        start_button.update()

        time.sleep(1.5) #how long blue titles are shown

        for rows in grid.controls[0].controls[:]:
            for container in rows.controls[:]:
                if (
                    container.bgcolor == "#4cbbb5"
                ): #if container color is blue, then
                    container.bgcolor = "#5c443b"
                    container.update()

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
        Row(alignment=MainAxisAlignment.CENTER, controls=[stage]),
        Divider(height=10, color="transparent"),
        #Start button
        Row(alignment=MainAxisAlignment.CENTER, controls=[start_button]),
    )


    page.update()

if __name__  == "__main__":
    flet.app(target=main)