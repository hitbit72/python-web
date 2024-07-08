import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.styles import Spacing as Spacing

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width = Size.LARGE.value,
                    height = Size.LARGE.value,
                    margin = Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items = "start",
                    spacing = Spacing.ZERO.value,
                    margin = Size.ZERO.value
                ),
            ),
        ),
        href=url,
        is_external=True,
        width = "100%"
    )


