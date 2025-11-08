import gpiod
import keyboard
import time

# GPIO pin numbers (BCM pin numbering)
LEFT_PIN = 5
RIGHT_PIN = 6
DOWN_PIN = 13
PAUSE_PIN = 19
ENTER_PIN = 26

# Open the GPIO chip (usually /dev/gpiochip0 for the default chip)
chip = gpiod.Chip("/dev/gpiochip0")

# Request the GPIO lines as inputs with pull-up resistors enabled (default value = 1)
left_line = chip.get_line(LEFT_PIN)
right_line = chip.get_line(RIGHT_PIN)
down_line = chip.get_line(DOWN_PIN)
pause_line = chip.get_line(PAUSE_PIN)
enter_line = chip.get_line(ENTER_PIN)

# Configure the lines as input with pull-up resistors
left_line.request(consumer="arcade-buttons", type=gpiod.LINE_REQ_DIR_IN, default_val=1)
right_line.request(consumer="arcade-buttons", type=gpiod.LINE_REQ_DIR_IN, default_val=1)
down_line.request(consumer="arcade-buttons", type=gpiod.LINE_REQ_DIR_IN, default_val=1)
pause_line.request(consumer="arcade-buttons", type=gpiod.LINE_REQ_DIR_IN, default_val=1)
enter_line.request(consumer="arcade-buttons", type=gpiod.LINE_REQ_DIR_IN, default_val=1)

try:
    while True:
        # Check each button press (GPIO line will be low when button is pressed)
        if left_line.get_value() == 0:  # Button pressed (Low)
            print("Left button pressed")
            keyboard.press_and_release("left")

        if right_line.get_value() == 0:
            print("Right button pressed")
            keyboard.press_and_release("right")

        if down_line.get_value() == 0:
            print("Down button pressed")
            keyboard.press_and_release("down")

        if pause_line.get_value() == 0:
            print("Pause button pressed")
            keyboard.press_and_release("esc")  # Use "esc" instead of "escape"

        if enter_line.get_value() == 0:
            print("Enter button pressed")
            keyboard.press_and_release("enter")

        time.sleep(0.1)  # Sleep for 100ms to debounce

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    # Clean up GPIO lines
    chip.close()
    print("GPIO resources cleaned up.")
