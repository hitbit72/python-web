import reflex as rx
from python_web.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Linkedin","https://www.linkedin.com/in/jtl-35b901294/"),
        link_button("Youtube","https://www.youtube.com"),
        link_button("Discord","https://discrod.gg")
    )
