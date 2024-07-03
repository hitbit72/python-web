import reflex as rx
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
        width="100%"
    )

app = rx.App()
app.add_page(index)

