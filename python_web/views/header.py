import reflex as rx
import python_web.styles.styles as styles
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
from python_web.styles.styles import Spacing as Spacing
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.fonts import Font as Font


def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="JT",
                radius="full",
                size=Spacing.BIG.value,
                src = "/avatar.jpg",
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
                    margin_bottom = Size.MEDIUM.value,
                    color = Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon("/icons/youtube.svg", "https://www.youtube.com", "Youtube"),
                    link_icon("/icons/github.svg", "https://github.com/hitbit72", "Github"),
                    link_icon("/icons/twitch.svg", "https://www.twitch.com", "Twitch"),
                    link_icon("/icons/instagram.svg", "https://www.instagram.com/", "Instagram"),
                    link_icon("/icons/tiktok.svg", "https://www.tiktok.com/es/", "TikTok")
                ),
                align_items="start",
                spacing=Spacing.ZERO.value,
            ),
            spacing=Spacing.MEDIUM.value,
            width="100%"
            #column_gap = "20px"
        ),
        baseHead(details),
        spacing=Spacing.MEDIUM.value,
        align_items="start",
    )



def baseHead(details) -> rx.Component:
    if details:
        return rx.box(
            rx.flex(
                info_text("3+", "Años de experiencia"),
                rx.spacer(),
                info_text("50+", "Aplicaciones creadas"),
                rx.spacer(),
                info_text("500+", "Seguidores"),
                width="100%"
            ),
            rx.text(
                """Soy programador freelance full-stack de python y PHP desde hace más de 5 años.
                Aquí podrás encontrar todos mis enlaces de interés. Bienbenid@s""",
                color = TextColor.BODY.value,
                font_size = Size.MEDIUM.value,
                margin_top = Size.DEFAULT.value
            ),
         width="100%",
        )
    return rx.box()
