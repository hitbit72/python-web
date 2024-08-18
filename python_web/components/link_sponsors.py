import reflex as rx
from python_web.styles.styles import Size as Size

def link_sponsors(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = imagen,
            height = Size.DUMBO.value,
            width = "auto",
            alt = alt
        ),
        href=url,
        is_external=True
    )
