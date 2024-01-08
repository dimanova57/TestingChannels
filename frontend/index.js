const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/new_chat/');

chatSocket.onopen = function(event){
    console.log('WebSocket connection is open.');
    sendMessage('New user connected')
}

chatSocket.onclose = function(event) {
    console.log('WebSocket connection is closed.');
}

chatSocket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    console.log(message);

    var messages = document.getElementById('chatMessages');
    messages.innerHTML += `${message.message}<br>`
}

document.getElementById('messageForm').addEventListener('submit', function(el){
    el.preventDefault();
    var messageForm = document.getElementById('messageForm');
    var messageText = messageForm.message.value;

    sendMessage(messageText);
})

function sendMessage(text){
    const messageData = JSON.stringify({'message': text,  'type': 'chat.message'});

    chatSocket.send(messageData);
}