import gpiod
import keyboard
import time
from gpiod.line import Direction, Value


# GPIO pin numbers (BCM pin numbering)
LEFT_PIN = 5
RIGHT_PIN = 6
DOWN_PIN = 13
PAUSE_PIN = 19
ENTER_PIN = 26
UP_PIN = 0
TAB_PIN = 11

with gpiod.request_lines('/dev/gpiochip0', consumer="blink-example",
    config={
        TAB_PIN: gpiod.LineSettings(
            direction=Direction.OUTPUT,
            output_value=Value.LOW,
        ),
        UP_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.edge_detection.BOTH,
            bias=gpiod.LineSettings.bias.PULL_UP,
        ),
        LEFT_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.edge_detection.BOTH,
            bias=gpiod.LineSettings.bias.PULL_UP,
        ),
        RIGHT_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.edge_detection.BOTH,
            bias=gpiod.LineSettings.bias.PULL_UP,
        ),
        DOWN_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.edge_detection.BOTH,
            bias=gpiod.LineSettings.bias.PULL_UP,
        ),
        PAUSE_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.edge_detection.BOTH,
            bias=gpiod.LineSettings.bias.PULL_UP,
        ),
        ENTER_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.edge_detection.BOTH,
            bias=gpiod.LineSettings.bias.PULL_UP,
        ),
    },
) as request:
    while True:
        events = request.wait_edge_events(timeout=1)
        if events:
            for event in request.read_edge_events():
                line_offset = event.line_offset  # The GPIO pin that triggered the event
                event_type = event.event_type  # Type of event (e.g., rising or falling edge)
                            # Print event information (for debugging purposes)
                print(f"Event on line {line_offset}: {event_type}")

                if line_offset == LEFT_PIN:
                                key = 'left'
                elif line_offset == RIGHT_PIN:
                                key = 'right'
                elif line_offset == DOWN_PIN:
                                key = 'down'
                elif line_offset == PAUSE_PIN:
                                key = 'esc'
                elif line_offset == ENTER_PIN:
                                key = 'enter'
                elif line_offset == UP_PIN:
                                key = 'up'
                elif line_offset == TAB_PIN:
                                key = 'tab'
                else:
                                continue  # If the event is from an untracked GPIO line, skip it

                            # Handle key press or release based on event type
                if event_type == gpiod.EdgeEvent.Type.RISING_EDGE:
                                keyboard.release(key)  # Key release on rising edge
                elif event_type == gpiod.EdgeEvent.Type.FALLING_EDGE:
                                keyboard.press(key)  # Key press on falling edge

                time.sleep(0.01)
