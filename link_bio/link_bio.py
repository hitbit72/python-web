import reflex as rx

from rxconfig import config

# Backend
class state(rx.State):
    pass


# Frontend
def index() -> rx.Component:
    return rx.text("Hola Reflex!", color="blue")

app = rx.App()
app.add_page(index)

