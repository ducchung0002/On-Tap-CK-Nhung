let socket = new WebSocket('ws://192.168.1.9:6789')
let red = document.getElementById('red')
let green = document.getElementById('green')
let blue = document.getElementById('blue')
  
socket.onmessage = (event) => {
  message = JSON.parse(event.data)
  let button = message.button
  if (button) {
    if (button == 3) {
    } else if (button == 2) {
    } else if (button == 1) {
    }
  } else {
    red.innerText = message.red
    green.innerText = message.green
    blue.innerText = message.blue
  }
}

function toggle(color) {
  socket.send(color)
}
