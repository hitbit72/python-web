import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

# Contants Max width de la web
MAX_WIDTH = "560px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.3em"
    BIG_MEDIUM = "1.5em"
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
    "font_family": Font.DEFAULT.value,
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

navbar_title_style = dict(
    font_family = Font.LOGO.value,
    font_size = Size.LARGE.value
)

header_title_style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.BIG_MEDIUM.value,
    color = TextColor.HEADER.value,
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    font_family = Font.TITLE.value,
    font_size = Size.LARGE.value,
    color = TextColor.HEADER.value
)


button_title_style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value
)

