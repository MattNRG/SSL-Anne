import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# SEE KOOD ON MÕELDUD KATSETUSEKS!! Hetkel töötab kahe mootori paariga

VASAK_EDASI = 12
VASAK_TAGASI = 13
PAREM_EDASI = 18
PAREM_TAGASI = 19
MOTOR_EN = 26

pins = [VASAK_EDASI, VASAK_TAGASI, PAREM_EDASI, PAREM_TAGASI, MOTOR_EN]
for p in pins:
    GPIO.setup(p, GPIO.OUT)

# PWM (Hetkel on kiirus 1 kHz, piirame sellega voolu, kuna mootorid on 12v)
v_ed = GPIO.PWM(VASAK_EDASI, 1000)
v_tag = GPIO.PWM(VASAK_TAGASI, 1000)
p_ed = GPIO.PWM(PAREM_EDASI, 1000)
p_tag = GPIO.PWM(PAREM_TAGASI, 1000)

for pwm in [v_ed, v_tag, p_ed, p_tag]:
    pwm.start(0)

def motorDriver(Left, Right):
    Left = max(-200, min(200, Left))
    Right = max(-200, min(200, Right))

    # Kas vähemalt üks mootor liigub?
    GPIO.output(MOTOR_EN, GPIO.HIGH if (Left != 0 or Right != 0) else GPIO.LOW)

    # VASAK MOOTOR
    if Left > 0:
        v_tag.ChangeDutyCycle(0)
        v_ed.ChangeDutyCycle(abs(Left) / 200 * 100)
    elif Left < 0:
        v_ed.ChangeDutyCycle(0)
        v_tag.ChangeDutyCycle(abs(Left) / 200 * 100)
    else:
        v_ed.ChangeDutyCycle(0)
        v_tag.ChangeDutyCycle(0)

    # PAREM MOOTOR
    if Right > 0:
        p_tag.ChangeDutyCycle(0)
        p_ed.ChangeDutyCycle(abs(Right) / 200 * 100)
    elif Right < 0:
        p_ed.ChangeDutyCycle(0)
        p_tag.ChangeDutyCycle(abs(Right) / 200 * 100)
    else:
        p_ed.ChangeDutyCycle(0)
        p_tag.ChangeDutyCycle(0)
