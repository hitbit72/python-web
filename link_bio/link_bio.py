"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

# Backend
class State(rx.State):
    """The app state."""
    pass


# Frontend
def index() -> rx.Component:
    return rx.text("Hola Reflex", color="blue")



app = rx.App()
app.add_page(index)
app._compile()
