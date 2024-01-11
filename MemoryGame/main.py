import flet
from flet import *
import time
import random

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
        #Stage of the game row
        Row(alignment=MainAxisAlignment.CENTER, controls=[stage]),
        Divider(height=10, color="transparent"),
        #Start button
        Row(alignment=MainAxisAlignment.CENTER, controls=[start_button]),
    )


    page.update()

if __name__  == "__main__":
    flet.app(target=main)