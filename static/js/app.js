var map = L.map('map',{ center: center, zoom: 15});
var locate_button = document.getElementById("locate_button");

L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiaHJnYWVydG5lciIsImEiOiJja2IyajYzMmIwOGgxMzFzMGFrcjVsd3R1In0.m3g_tfRrzVvC1mrIiMXhQA', {
 attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a> <img src="/static/images/circle.png">'
}).addTo(map);

function onEachFeature(feature, layer) {
    layer.bindPopup(feature.name);
}

var geojsonMarkerOptions = {
    radius: 8,
    fillColor: "#32CD32",
    color: "#32CD32",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8,
}

L.geoJSON(bus_stops, {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, geojsonMarkerOptions);},
    onEachFeature: onEachFeature
}).addTo(map);

var realtime = L.realtime({
    url: 'http://127.0.0.1:5000/update',
    crossOrigin: true,
    type: 'json'
}, {
    interval: 500, onEachFeature(f, l) {}
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