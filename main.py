import badger2040

WIDTH = 296
HEIGHT = 128

# The built-in bitmap font is reliably ASCII-only. The accent is drawn as a
# small line so the heading renders ALVARO with an accent.
NAME = "ALVARO"
ROLE = "Software Developer"
COMMUNITY = "Python Navarra member"
STATS = (
    ("Python", 10),
    ("Rust", 6),
    ("Coffee", 10),
    ("Social", 3),
)


def draw_segmented_bar(display, label, filled, y):
    """Draw one label plus ten graphical, outlined segments."""
    bar_x = 82
    segment_width = 18
    segment_height = 8
    segment_step = 20

    display.text(label, 12, y, WIDTH, 1)

    for index in range(10):
        x = bar_x + (index * segment_step)
        if index < filled:
            display.rectangle(x, y, segment_width, segment_height)
        else:
            display.line(x, y, x + segment_width - 1, y)
            display.line(x, y + segment_height - 1, x + segment_width - 1, y + segment_height - 1)
            display.line(x, y, x, y + segment_height - 1)
            display.line(x + segment_width - 1, y, x + segment_width - 1, y + segment_height - 1)


def draw_badge():
    display = badger2040.Badger2040()
    display.set_font("bitmap8")

    # White canvas, then black ink for the terminal/card treatment.
    display.set_pen(15)
    display.clear()
    display.set_pen(0)

    # High-contrast nameplate.
    display.rectangle(8, 5, 168, 30)
    display.set_pen(15)
    display.text(NAME, 13, 8, WIDTH, 3)
    display.line(26, 5, 31, 1)  # Accent over the initial A.

    display.set_pen(0)
    display.set_font("bitmap6")
    display.text(ROLE, 12, 40, WIDTH, 1)
    dot_x = 12 + display.measure_text(ROLE, 1) + 4
    display.rectangle(dot_x, 42, 2, 2)
    display.text(COMMUNITY, dot_x + 8, 40, WIDTH, 1)

    display.set_font("bitmap8")
    display.line(12, 51, 284, 51)

    for row, (label, filled) in enumerate(STATS):
        draw_segmented_bar(display, label, filled, 57 + (row * 12))

    display.line(12, 105, 284, 105)
    display.rectangle(10, 109, 58, 14)
    display.set_pen(15)
    display.text("STATUS", 14, 112, WIDTH, 1)
    display.set_pen(0)
    display.text("Coffee-driven development", 78, 112, WIDTH, 1)

    # One e-ink refresh: the image remains after USB power is removed.
    display.update()

    # Keep the static image active when launched from Badger OS.
    while True:
        display.keepalive()
        display.halt()


draw_badge()
