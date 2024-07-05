import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"(c) 2023-{datetime.date.today().year} HITBIT BY JORGE TEJADA V1.",
            href="https://www.linkedin.com/in/jtl-35b901294",
            is_external=True
        ),
        rx.text("BUILDING SOFTWARE FROM ANDALUCIA", as_="div"),
    )
