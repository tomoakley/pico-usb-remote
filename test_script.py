import serial
import serial.tools.list_ports
import sys
import time

# Find your Pico's serial port
# It's usually /dev/tty.usbmodem* or /dev/cu.usbmodem*
port = "/dev/cu.usbmodem21201"  # Use the one from your mpremote output
baud = 9600

try:
    ser = serial.Serial(port, baud, timeout=1)
except serial.SerialException as e:
    print(f"Couldn't open {port}: {e}")
    print("Available USB devices:")
    for p in serial.tools.list_ports.comports():
        print(f"  {p.device}  {p.description}  ({p.hwid})")
    sys.exit(1)

time.sleep(1)  # Wait for connection

print("Sending SWITCH command...")
ser.write(b"SWITCH\n")
time.sleep(0.5)

status = None
while ser.in_waiting:
    line = ser.readline().decode().strip()
    if line:
        print(f"Pico: {line}")
        if line in ("Relay ON", "Relay OFF"):
            status = line

if status:
    print(f"Done! Relay status: {status}")
else:
    print("Done! No status received.")

ser.close()
