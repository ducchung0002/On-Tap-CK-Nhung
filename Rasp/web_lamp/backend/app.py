import asyncio
import websockets
import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
connected = set()
# LED
LED_PINS = {'red': 2, 'green': 3, 'blue': 4}
LED_STATE = {'red': 0, 'green': 0, 'blue': 0}

for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

async def broadcast(message):
    await asyncio.gather(*(ws.send(message) for ws in connected))

async def server(websocket, path):
    connected.add(websocket)
    try:
        await websocket.send(json.dumps(LED_STATE))
        while True:
            color = await websocket.recv()
            LED_STATE[color] = 1 - LED_STATE[color]
            GPIO.output(LED_PINS[color], LED_STATE[color])
            # broadcast to all clients
            await broadcast(json.dumps(LED_STATE))
    finally:
        connected.remove(websocket)

# BUTTON
def button_callback(channel):
    index = BUTTON_PINS.index(channel)
    message = json.dumps({'button': index + 1})
    asyncio.run(broadcast(message))

BUTTON_PINS = [17, 27, 22]
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
#
start_server = websockets.serve(server, '0.0.0.0', 6789)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
