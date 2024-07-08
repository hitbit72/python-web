import reflex as rx
import datetime
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            padding_bottom=Size.MEDIUM.value,
            height = Size.VERY_BIG.value
        ),
        rx.link(
            f"(c) 2023-{datetime.date.today().year} HITBIT by Jorge Tejada V1.",
            href="https://www.linkedin.com/in/jtl-35b901294",
             is_external=True,
             font_size=Size.MEDIUM.value,
             color = TextColor.FOOTER.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM ANDALUCIA",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color = TextColor.FOOTER.value,
        row_gap="0px"
    )
