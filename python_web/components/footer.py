import reflex as rx
import datetime
from python_web.styles.styles import Size as Size
from python_web.styles.styles import Spacing as Spacing
from python_web.styles.colors import Color as Color
from python_web.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/favicon.ico",
            height = Size.VERY_BIG.value,
            width = Size.VERY_BIG.value,
            alt = "Logotipo de hitbit"
        ),
        rx.link(
            rx.box(
                f"(c) 2023-{datetime.date.today().year} ",
                rx.text(
                    "HITBIT by Jorge Tejada",
                    as_="span",
                    color = Color.PRIMARY.value
                ),
                " V4.",
                color = TextColor.FOOTER.value,
                padding_top=Size.DEFAULT.value,
            ),
            href="https://www.linkedin.com/in/jtl-35b901294",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src = "/icons/github.svg",
                    height = Size.LARGE.value,
                    width = Size.LARGE.value,
                    alt = "Logotipo de github"
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM ANDALUCIA",
                    font_size=Size.MEDIUM.value,
                    color = TextColor.FOOTER.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href ="https://github.com/hitbit72/python-web",
            is_external=True,
        ),
        align_items = "center",
        #margin_bottom = Size.BIG.value,
        padding_bottom = Size.BIG.value,
        padding_x = Size.BIG.value,
        color = TextColor.FOOTER.value,
        spacing = Spacing.ZERO.value
    )
