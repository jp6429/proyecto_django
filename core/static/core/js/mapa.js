//  Este es el codigo del mapa que me corrio

var mymap = L.map('map').setView([-33.4569400, -70.6482700], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(mymap);

// Aqui estoy marcando un punto de nuestra tienda fisica en el mapa

let marker = L.marker([-33.4569400, -70.6482700]).addTo(mymap)