var map = L.map('map').setView([20,0],2)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map)

var attacks = [

[37.77,-122.41],
[51.50,-0.12],
[35.68,139.69],
[-1.29,36.82]

]

attacks.forEach(function(a){

L.circle(a,{
color:'red',
radius:50000
}).addTo(map)

})