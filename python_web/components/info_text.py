import reflex as rx
from python_web.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold",
            color="blue",
            as_="span"
        ),
        f" {body}",
        font_size=Size.MEDIUM.value
    )
