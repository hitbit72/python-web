import reflex as rx
import datetime
from python_web.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"(c) 2023-{datetime.date.today().year} HITBIT by Jorge Tejada V1.",
            href="https://www.linkedin.com/in/jtl-35b901294",
             is_external=True,
             font_size=Size.MEDIUM.value,
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM ANDALUCIA",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important"
        ),
        margin_bottom=Size.BIG.value,
    )
