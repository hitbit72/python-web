import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.styles import Spacing as Spacing

def link_button(title: str, body: str, image: str, url: str, is_externa = True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width = Size.BIG_MEDIUM.value,
                    height = Size.BIG_MEDIUM.value,
                    margin = Size.MEDIUM.value,
                    alt = title
                ),
                rx.vstack(
                    rx.text(
                        title,
                        size = Spacing.SMALL.value,
                        style= styles.button_title_style
                    ),
                    rx.text(
                        body,
                        size = Spacing.SMALL.value,
                        style= styles.button_body_style,
                    ),
                    align_items = "start",
                    spacing = Spacing.VERY_SMALL.value,
                    padding_y=Size.VERY_SMALL.value,
                    padding_right = Size.VERY_SMALL.value
                    #margin = Size.ZERO.value
                ),
                align="center",
                width = "100%"
            ),
        ),
        href=url,
        is_external=is_externa,
        width = "100%"
    )



