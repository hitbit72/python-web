import reflex as rx
import python_web.styles.styles as styles


def title(title: str) -> rx.Component:
    return rx.heading(
        title,
        size = "6",
        style = styles.title_style
    )

