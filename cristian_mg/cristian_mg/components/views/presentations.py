import reflex as rx


def presentation() -> rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.image(
                    src="/foto_1.png",
                    width="15em",
                    height="auto",
                    border_radius="25%",
                    position="relative"
                ),
                rx.heading(
                    "Cristian Montoya",
                    size="8",
                    font_family="IBM Plex Mono",
                    width="15em",
                    position="absolute",
                    top="80px",  # Ajusta la posición según sea necesario
                    left="190px",  # Ajusta la posición según sea necesario
                    color="white"  # Ajusta el color del texto según sea necesario
                ),
                rx.heading(
                    "Garces",
                    size="8",
                    font_family="IBM Plex Mono",
                    width="15em",
                    position="absolute",
                    top="108px",  # Ajusta la posición según sea necesario
                    left="397px",  # Ajusta la posición según sea necesario
                    color="white"  # Ajusta el color del texto según sea necesario
                ),
                rx.heading(
                    "Python Developer",
                    size="8",
                    font_family="IBM Plex Mono",
                    width="15em",
                    position="absolute",
                    top="137px",  # Ajusta la posición según sea necesario
                    left="397px",  # Ajusta la posición según sea necesario
                    color="#ff2a6d"  # Ajusta el color del texto según sea necesario
                ),
                rx.separator(
                    color="#ff2a6d",
                    position="absolute",
                    top="11.4em",
                    left="15.3em",
                    width="30em",
                    decorative=True,
                    size="4",

                ),
                rx.hstack(
                    rx.text("Download CV", size="5"),
                    rx.text("LinkIn", size="5"),
                    rx.text("Github", size="5"),
                    spacing="5",
                    justify="between",
                    top="11.5em",
                    left="15.3em",
                    position="absolute",
                    width="20em"
                )
            ),
            position="relative",
            display="inline-block",
            width="auto"
        ),
        bg="#000000",
        width="auto",
        padding_x="7em"

    )


# ]Eskjbdfv brwiuoghbefvhberpñsbrv
#
# ++-*/78543131l
