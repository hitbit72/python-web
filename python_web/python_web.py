import reflex as rx
import python_web.styles.styles as styles
from python_web.components.navbar import navbar
from python_web.views.header.header import header
from python_web.views.links.link import links
from python_web.components.footer import footer


# Backend
class state(rx.State):
    pass


# Frontend
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
        align_items = "center",
        justify_content = "center"
    )

def prueba() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                "Ejemplo",
                bg="red",
                width="20%"
            ),
            rx.box(
                "Ejemplo2",
                bg="orange"
            ),
            align_items = "center",
            justify_content = "center"
        )
    )

# styles=styles.BASE_STYLE
app = rx.App(styles=styles.BASE_STYLE)
app.add_page(index)



