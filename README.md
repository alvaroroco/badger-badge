# Badger Badge — Badger 2040 original

A static MicroPython conference badge for the **Pimoroni Badger 2040 original (RP2040)**. It is **not** for the Badger 2040 W.

The program draws once and calls `display.update()` exactly once. Its graphical bars use rectangles and lines—never Unicode block characters.

## Approximate layout

```text
┌────────────────────────────────────┐
│ ÁLVARO                             │
│ Software Developer · Python Navarra member │
│ ────────────────────────────────── │
│ Python   ■■■■■■■■■■                 │
│ Rust     ■■■■■■□□□□                 │
│ Coffee   ■■■■■■■■■■                 │
│ Social   ■■■□□□□□□□                 │
│                                    │
│ STATUS  works on my machine        │
└────────────────────────────────────┘
```

The actual bars are ten individual outlined or filled graphical segments. The `Á` accent is drawn as a line over the ASCII `A`, avoiding any dependency on extended-character support in the built-in bitmap font.

## Use

1. Download the current **`badger2040`** MicroPython UF2 for the original Badger 2040 from [Pimoroni's firmware releases](https://github.com/pimoroni/badger2040/releases/latest). Do **not** use a `badger2040w` UF2.
2. If firmware installation is needed, connect the board by USB, hold **BOOT/USR**, press **RST**, then copy the `badger2040` UF2 to the `RPI-RP2` drive.
3. Open **Thonny**, choose the MicroPython interpreter/port for the connected Badger, then open `main.py`.
4. Save it to the device as `badge.py`, then press **Run** once. Do not overwrite the Badger OS launcher with `main.py` unless you deliberately want this badge to replace the device's startup program.
5. Wait for the single e-ink refresh to complete, then unplug the USB cable.
6. The rendered badge remains visible without battery power because e-ink retains the image.

## Files

- `main.py` — the complete badge; no Wi-Fi, Bluetooth, button handling, animation, or periodic updates.
