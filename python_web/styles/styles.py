import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor

# Contants Max width de la web
MAX_WIDTH = "560px"

# Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    MEDIUM = "6"
    BIG = "7"
    VERY_BIG = "9"

# Styles default
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.vstack: {
        "align_items": "center",
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}


title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)


button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value
)

