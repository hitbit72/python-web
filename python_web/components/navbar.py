import reflex as rx
import python_web.styles.styles as styles
from python_web.routes import Route
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text(
                    "hitbit",
                    color = Color.PRIMARY.value,
                    as_="span"
                ),
                rx.text(
                    "dev",
                    color = Color.SECONDARY.value,
                    as_="span"
                ),
                style = styles.navbar_title_style,
            ),
            href = Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
