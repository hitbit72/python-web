import reflex as rx
import python_web.utils  as utils
import python_web.styles.styles as styles
from python_web.components.navbar import navbar
from python_web.views.header import header
from python_web.views.index_link import links
from python_web.views.sponsors import sponsors
from python_web.components.footer import footer

# Frontend

@rx.page(
    title = utils.index_title,
    description = utils.index_description,
    image = utils.preview,
    meta = utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG.value,
                padding = styles.Size.LARGE.value
            ),
        ),
        footer(),
    )
