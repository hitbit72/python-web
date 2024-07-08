import reflex as rx
import python_web.styles.styles as styles
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
from python_web.styles.styles import Spacing as Spacing
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.fonts import Font as Font

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                #fallback="JT",
                radius="full",
                size=Spacing.MEDIUM.value,
                src = "avatar.jpg",
                color = TextColor.BODY.value,
                bg = Color.CONTENT.value,
                padding = "2px",
                border=f"4px solid {Color.PRIMARY.value}"
            ),
            rx.vstack(
                rx.heading(
                    "Jorge Tejada",
                    style = styles.header_title_style,
                    size = Spacing.MEDIUM.value
                ),
                rx.text(
                    "@hitbit72",
                    margin_top = Size.ZERO.value,
                    color = TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("icons/youtube.svg", "https://www.google.com"),
                    link_icon("icons/github.svg", "https://github.com/hitbit72"),
                    link_icon("icons/twitch.svg", "https://www.google.com"),
                ),
                row_gap = "0",
                align_items="start",
                spacing=Spacing.DEFAULT.value,
            ),
            spacing=Spacing.BIG.value,
        ),
        rx.flex(
            info_text("+3", "Años de experiencia"),
            rx.spacer(),
            info_text("+50", "Aplicaciones creadas"),
            rx.spacer(),
            info_text("1k", "Seguidores"),
            width="100%"
        ),
        rx.text(
            """Soy programador freelance full-stack de python y PHP desde hace más de 5 años.
            Aquí podrás encontrar todos mis enlaces de interés. Bienbenid@s""",
            color = TextColor.BODY.value,
            font_size = Size.MEDIUM.value
        ),
        spacing=Spacing.BIG.value,
        align_items="start"
    )
