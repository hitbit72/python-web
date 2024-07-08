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
            "icons/linkedin.svg",
            "https://www.linkedin.com/in/jtl-35b901294/"
        ),
        link_button(
            "Youtube",
            "canal principal",
            "icons/youtube.svg",
            "https://www.youtube.com"
        ),
        link_button(
            "Discord",
            "Chat de los colegas",
            "icons/discord.svg",
            "https://discrod.gg"
        ),
        title("Recursos y más"),
        link_button(
            "Linkedin",
            "datos de linkedin",
            "icons/linkedin.svg",
            "https://www.linkedin.com/in/jtl-35b901294/"
        ),
        link_button(
            "Youtube",
            "canal principal",
            "icons/youtube.svg",
            "https://www.youtube.com"
        ),
        link_button(
            "Discord",
            "Chat de los colegas",
            "icons/discord.svg",
            "https://discrod.gg"
        ),
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "icons/email.svg",
            "https://www.youtube.com"
        ),
        link_button(
            "Email",
            "correo electrónico",
            "icons/email.svg",
            "mailto: corro@correo.com"
        ),
        width = "100%",
        spacing=Spacing.SMALL.value
    )
