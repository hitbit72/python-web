import reflex as rx
import python_web.styles.styles as styles


def title(title: str) -> rx.Component:
    return rx.heading(
        title,
        size = styles.Spacing.BIG.value,
        style = styles.title_style
    )

