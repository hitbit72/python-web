import reflex as rx
import python_web.styles.styles as styles
from python_web.components.navbar import navbar
from python_web.views.header import header
from python_web.views.link import links
from python_web.views.sponsors import sponsors
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
                sponsors(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG.value,
                padding = styles.Size.LARGE.value
            ),
        ),
        footer(),
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title = "Hitbit72 | Diseño web y programación de aplicaciones",
    description = "Hola, mi nombre es Jorge Tejada. Soy desarrollador freelance full-stack",
    image = "avatar.jpg"
)



