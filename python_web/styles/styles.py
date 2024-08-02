import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font, FontWeight

# Referencias
# iconos: https://fontawesome.com
# Funetes: https://fonts.google.com/
# mouredev: https://mouredev.reflex.run/

# Contants Max width de la web
MAX_WIDTH = "560px"

# Fuentes
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.3em"
    BIG_MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    DUMBO = "6em"
    JUMBO = "8em"

#Spacing
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
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
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
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value
)

header_title_style = dict(
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.BIG_MEDIUM.value,
    color = TextColor.HEADER.value,
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.BIG_MEDIUM.value,
    color = TextColor.HEADER.value
)


button_title_style = dict(
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_weight = FontWeight.LIGHT.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value
)

