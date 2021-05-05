basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
basic.pause(1000)
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    serial.writeNumber(input.acceleration(Dimension.Strength))
    basic.pause(2000)
})
