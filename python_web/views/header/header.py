import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="JT", radius="full", size="5"),
        rx.text("@hitbit"),
        rx.text("HOLA MI NOMBRE ES JORGE TEJADA"),
        rx.text("Soy programador full-stack freelance de python y PHP desde hace más de 5 años.")
    )
