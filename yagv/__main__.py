from .yagv import App

import pyglet


def main():
    # Disable error checking for increased performance
    pyglet.options['debug_gl'] = False

    App().main()


if __name__ == "__main__":
    main()


# EOF #

