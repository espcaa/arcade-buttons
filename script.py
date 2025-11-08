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

with gpiod.request_lines('/dev/gpiochip0', consumer="blink-example",
    config={
        LEFT_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.EdgeDetection.BOTH_EDGES,
            bias=gpiod.LineSettings.Bias.PULL_UP,
        ),
        RIGHT_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.EdgeDetection.BOTH_EDGES,
            bias=gpiod.LineSettings.Bias.PULL_UP,
        ),
        DOWN_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.EdgeDetection.BOTH_EDGES,
            bias=gpiod.LineSettings.Bias.PULL_UP,
        ),
        PAUSE_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.EdgeDetection.BOTH_EDGES,
            bias=gpiod.LineSettings.Bias.PULL_UP,
        ),
        ENTER_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            edge_detection=gpiod.LineSettings.EdgeDetection.BOTH_EDGES,
            bias=gpiod.LineSettings.Bias.PULL_UP,
        ),
    },
) as request:
    while True:
        events = request.event_wait(timeout=1)
        if events:
            for event in request.read_events():
                line_offset = event.line_offset
                event_type = event.event_type

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
                else:
                    continue

                if event_type == gpiod.LineEvent.Type.RISING_EDGE:
                    keyboard.release(key)
                elif event_type == gpiod.LineEvent.Type.FALLING_EDGE:
                    keyboard.press(key)
        time.sleep(0.01)
