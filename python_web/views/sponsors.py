import reflex as rx
from python_web.components.title import title
from python_web.components.link_sponsors import link_sponsors
from python_web.styles.styles import Spacing as Spacing

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsors(
                "elgato.png",
                url = ""
            ),
            link_sponsors(
                "mvp.png",
                url = ""
            ),
            spacing = Spacing.BIG.value
        ),
        width = "100%",
        align_items = "start"
    )