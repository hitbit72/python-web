import reflex as rx
from python_web.routes import Route
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.styles.styles import Spacing as Spacing


def links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Curso Pyhton",
            "Aprende Python desde cero de forma muy facil",
            "/icons/discord.svg",
            Route.COURSES.value,
            is_externa=False
        ),
        link_button(
            "Retos de programación",
            "Ruta de estudio semanal para practicar lógica de programación",
            "/icons/linkedin.svg",
            "https://www.linkedin.com/in/jtl-35b901294/"
        ),
        title("Mucho más en"),
        link_button(
            "Youtube",
            "Tutoriales sobre programación de lunes a viernes",
            "/icons/youtube.svg",
            "https://www.youtube.com"
        ),
        width = "100%",
        spacing=Spacing.SMALL.value
    )
