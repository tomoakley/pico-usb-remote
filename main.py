from machine import Pin, ADC
import sys
import select
import time

relay = Pin(9, Pin.OUT, value=0)
button = Pin(26, Pin.IN, Pin.PULL_UP)
relay.off()

relay_state = False  # Track current state
last_voltage = 3.3
button_pressed = False
active_side = 'left'

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

def trigger_switch():
    relay.on()
    time.sleep(0.5)
    relay.off()
    if (active_side == 'left'):
        active_side = 'right'
    else:
        active_side == 'left'
    print(f"{switched: true, active_side: {active_side}}")

while True:
    if button.value() == 0:
        print("button pressed")
        trigger_switch()
        while button.value() == 0:
            time.sleep(0.05)
        time.sleep(0.2)  # Debounce after releas
    if poll.poll(0):
        data = sys.stdin.readline().strip()
        if data == "SWITCH":
            trigger_switch()
        elif data == "PING":
            print("PONG")
