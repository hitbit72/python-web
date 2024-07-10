import reflex as rx
from python_web.components.title import title
from python_web.components.link_sponsors import link_sponsors
from python_web.styles.styles import Spacing as Spacing

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsors(
                "elgato.png",
                "",
                "Logotipo de ElGato"
            ),
            rx.spacer(),
            link_sponsors(
                "mvp.png",
                "",
                "Logotipo de Microsoft MVP"
            ),
            spacing = Spacing.BIG.value,
            flex_direction=["column", "row"]
        ),
        width = "100%",
        align_items="start",
        spacing=Spacing.SMALL.value
    )
