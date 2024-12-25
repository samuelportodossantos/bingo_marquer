const socket = new WebSocket('ws:10.0.0.19:5001')


function add_ball(ball_number) {
    const ball = document.createElement('div')
    ball.classList.add('ball')
    ball.innerText = ball_number
    balls_container = document.getElementsByClassName('content')
    balls_container[0].append(ball)
}

socket.onmessage = function(event) {
    const data = JSON.parse(event.data)
    add_ball(data.new_ball)
    console.log('Received from server', data)
}

socket.onclose = function(event) {
    console.log('Socket closed');
}

socket.onerror = function(error) {
    console.log(error);
}
