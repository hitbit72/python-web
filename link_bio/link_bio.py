import reflex as rx

from rxconfig import config

# Backend
class state(rx.State):
    pass


# Fontend
def index() -> rx.Component:
    return rx.text("Hola Reflex!")

app = rx.App()
app.add_page(index)

