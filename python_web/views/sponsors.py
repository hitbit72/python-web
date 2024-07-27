import reflex as rx
from python_web.components.title import title
from python_web.components.link_sponsors import link_sponsors
from python_web.styles.styles import Spacing as Spacing

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Insignias"),
        rx.flex(
            link_sponsors(
                "/introduction_cybersecurity204x204.png",
                "https://www.credly.com/badges/8bf27c32-5bb5-4966-9bd7-aa6a674c3c45/public_url",
                "Insignia Introduction to Cybersecurity"
            ),
            rx.spacer(),
            link_sponsors(
                "/endpoint_security204x204.png",
                "https://www.credly.com/badges/a0b8e943-9d7d-43ed-9cbc-8fe8b5ef36b0/public_url",
                "Insignia Endpoint Security"
            ),
            rx.spacer(),
            link_sponsors(
                "/webdevelopment_python204x204.png",
                "https://www.credly.com/badges/8e46806f-c34f-4ebc-bb25-153fb5312676/public_url",
                "Insignia Web Development with Python"
            ),
            spacing = Spacing.BIG.value,
            flex_direction=["column", "row"]
        ),
        width = "100%",
        align_items="start",
        spacing=Spacing.SMALL.value
    )
