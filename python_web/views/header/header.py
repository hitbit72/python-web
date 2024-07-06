import reflex as rx
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
from python_web.styles.styles import Spacing as Spacing


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JT", radius="full", size="5"),
            rx.vstack(
                rx.heading(
                    "Jorge Tejada",
                    size = Spacing.LARGE.value
                ),
                rx.text(
                    "@hitbit"
                ),
                rx.hstack(
                    link_icon("youtube", "https://www.google.com"),
                    link_icon("message-circle-more", "https://www.google.com"),
                    link_icon("twitch", "https://www.google.com"),
                ),
                row_gap = "0",
                align_items="start",
            ),
            spacing=Spacing.BIG.value,
        ),
        rx.flex(
            info_text("+3", "Años de experiencia"),
            rx.spacer(),
            info_text("+3", "Años de experiencia"),
            rx.spacer(),
            info_text("+3", "Años de experiencia"),
            width="100%"
        ),
        rx.text(
            "Soy programador freelance full-stack de python y PHP desde hace más de 5 años.",
        ),
        spacing=Spacing.BIG.value,
        align_items="start"
    )
