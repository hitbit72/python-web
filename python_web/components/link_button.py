import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.styles import Spacing as Spacing

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    "chevrons-right",
                    width = Size.BIG.value,
                    height = Size.BIG.value,
                    margin = Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing = Spacing.VERY_SMALL.value,
                    align_items = "start",
                    margin = Size.ZERO.value,
                ),
                align = "center"
            ),
        ),
        href=url,
        is_external=True,
        width = "100%"
    )


