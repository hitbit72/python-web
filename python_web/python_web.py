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
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG.value
            ),
        ),
        footer()
    )


app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)



