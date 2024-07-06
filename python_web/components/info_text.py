import reflex as rx
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value,
            as_="span"
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color = TextColor.BODY.value
    )
