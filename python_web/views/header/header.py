import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="JT", radius="full", size="5"),
        rx.text("@hitbit", as_="div"),
        rx.text("HOLA MI NOMBRE ES JORGE TEJADA"),
        rx.text("Soy programador freelance desde hace más de 5 años"),
    )
