let socket = new WebSocket('ws://127.0.0.1:6789')
let red = document.getElementById('red')
let green = document.getElementById('green')
let blue = document.getElementById('blue')

socket.onmessage = (event) => {
    message = JSON.parse(event.data)
    let button = message.button
    if (button) {
        document.getElementById('btn').innerText = 'button ' + button
    } else {
        red.innerText = message.red
        green.innerText = message.green
        blue.innerText = message.blue
    }
}

function toggle(color) {
    socket.send(color)
}
