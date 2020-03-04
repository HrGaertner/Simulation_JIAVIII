var map = L.map('map',{ center: [49.4292523,7.7600434], zoom: 15});

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
 attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var realtime = L.realtime({
    url: 'http://127.0.0.1:5000/update',
    crossOrigin: true,
    type: 'json'
}, {
    interval: 500
}).addTo(map);