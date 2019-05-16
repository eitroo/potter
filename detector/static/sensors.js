window.addEventListener("devicemotion", accelerometer,True);
window.addEventListener('deviceorientation', orientation, True);

var socket =io();

var x, y, z, alpha, gamma, beta;
arr = [];
var isOn = false;
//Running always
function accelerometer(event){
    x = event.accelerationIncludingGravity.x;
    y = event.accelerationIncludingGravity.y;
    z = event.accelerationIncludingGravity.z;
}

function orientation(event){
    alpha = event.alpha;
    gamma = event.gamma;
    beta = event.beta;
}


//Start here
function start(){
    if (isOn){
    isOn = true;
    interval = setInterval(arraying, 200);
    document.querySelector("#send").innerHTML = 'stop'
    } else {
        clearInterval(interval);
        isOn = false;
        document.querySelector("#send").innerHTML = 'start'
    }
}

//Appending every 200 ms
function arraying(){
    arr.push(x,y,z,alpha,gamma,beta);
    if(arr.length >=30){
        send();
    }
}

//Sending to socket on views.py
function send(){
    socket.emit('detect', {'samples':arr});
    arr.length = 0;
}

//Recieving from socket on views.py, displaying result in the HTML
socket.on('Result', res =>{
    document.querySelector('#indicator').innerHTML = res;
})
