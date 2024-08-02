import reflex as rx

# Comun
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "avatar.jpg"
_meta=[
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "sumary_large_image"},
    {"name": "twuitter:site", "content": "@hitbit72"}
]

# index
index_title = "Hitbit72 | Diseño web y programación de aplicaciones"
index_description = "Hola, mi nombre es Jorge Tejada. Soy desarrollador freelance full-stack"
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)



# Cursos
cursos_title = "Hitbit72 | Cursos gratuitos"
cursos_description = "Cursos gratuitos para la comunidad"
cursos_meta = [
    {"name": "og:title", "content": cursos_title},
    {"name": "og:description", "content": cursos_description},
]
cursos_meta.extend(_meta)
