def on_button_pressed_a():
    global biasValue
    biasValue += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global biasValue
    biasValue += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

biasValue = 0

def on_forever():
    Kitronik_Move_Motor.motor_balance(Kitronik_Move_Motor.SpinDirections.LEFT, 0)
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 100)
basic.forever(on_forever)
