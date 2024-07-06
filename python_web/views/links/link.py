import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.styles.styles import Spacing as Spacing


def links() -> rx.Component:
    return rx.vstack(
        title("Comnidad"),
        link_button(
            "Linkedin",
            "datos de linkedin",
            "https://www.linkedin.com/in/jtl-35b901294/"
        ),
        link_button(
            "Youtube",
            "canal principal",
            "https://www.youtube.com"
        ),
        link_button(
            "Discord",
            "Chat de los colegas",
            "https://discrod.gg"
        ),
        title("Recursos"),
        link_button(
            "Linkedin",
            "datos de linkedin",
            "https://www.linkedin.com/in/jtl-35b901294/"
        ),
        link_button(
            "Youtube",
            "canal principal",
            "https://www.youtube.com"
        ),
        link_button(
            "Discord",
            "Chat de los colegas",
            "https://discrod.gg"
        ),
        width = "100%",
        spacing=Spacing.SMALL.value
    )
