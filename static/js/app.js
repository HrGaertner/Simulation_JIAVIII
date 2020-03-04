var map = L.map('map',{ center: [49.4292523,7.7600434], zoom: 15});
var locate_button = document.getElementById("locate_button");

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
 attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors <img src="/static/images/circle.png">'
}).addTo(map);

function onEachFeature(feature, layer) {
    layer.bindPopup(feature.name);
}

var geojsonMarkerOptions = {
    radius: 8,
    fillColor: "#32CD32",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8,
    onEachFeature: onEachFeature
}

L.geoJSON(bus_stops, {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, geojsonMarkerOptions);}
}).addTo(map);

var realtime = L.realtime({
    url: 'http://127.0.0.1:5000/update',
    crossOrigin: true,
    type: 'json'
}, {
    interval: 500
}).addTo(map);

// placeholders for the L.marker and L.circle representing user's current position and accuracy
    var current_position, current_accuracy;

    function onLocationFound(e) {
      // if position defined, then remove the existing position marker and accuracy circle from the map
      if (current_position) {
          map.removeLayer(current_position);
          map.removeLayer(current_accuracy);
      }

      var radius = e.accuracy / 2;

      current_position = L.marker(e.latlng).addTo(map)
        .bindPopup("You are within " + radius + " meters from this point").openPopup();

      current_accuracy = L.circle(e.latlng, radius).addTo(map);
    }

    map.on('locationfound', onLocationFound);
    //map.on('locationerror', onLocationError);

    // wrap map.locate in a function
    function locate() {
      if(locate_button.checked){
        map.locate({setView: true, maxZoom: 16});
      }
    }

    // call locate every 3 seconds... forever
    setInterval(locate, 3000);