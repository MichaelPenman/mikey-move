input.onButtonPressed(Button.A, function () {
    biasValue += -1
})
input.onButtonPressed(Button.B, function () {
    biasValue += 1
})
let biasValue = 0
basic.forever(function () {
    basic.showNumber(biasValue)
    Kitronik_Move_Motor.motorBalance(Kitronik_Move_Motor.SpinDirections.Left, biasValue)
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 10)
})
