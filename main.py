basic.show_leds("""
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    """)
basic.pause(1000)
basic.show_icon(IconNames.HAPPY)

def on_forever():
    serial.write_number(input.acceleration(Dimension.STRENGTH))
    basic.pause(2000)
basic.forever(on_forever)
