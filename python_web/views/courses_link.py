import reflex as rx
from python_web.routes import Route
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.styles.styles import Spacing as Spacing


def links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Curso Python Web",
            "Aprende Python desde cero de forma muy facil",
            "/python_highlighted.png",
            "https://www.youtube.com/watch?v=n2YrGsXJC6Y&t=1s",
            is_externa=True
        ),
        link_button(
            "Curso de python WEB avanzado",
            "Python web avanzado, API REST, Docker, PostgreSQL...",
            "/python_highlighted.png",
            "https://www.youtube.com/watch?v=bNy8OZJfA6I&t=1206s",
            is_externa=True
        ),
        title("Mucho más en"),
        link_button(
            "@mouredev by Brais Moure",
            "Tutoriales sobre programación de lunes a viernes",
            "/icons/youtube.svg",
            "https://www.youtube.com/@mouredev/featured",
            is_externa=True
        ),
        width = "100%",
        spacing=Spacing.SMALL.value
    )
