var map = L.map("map", {attributionControl:false}).setView([46.897357855724714, -96.80289743876295], 15);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

var wmsUrl =
  "https://mapservices.weather.noaa.gov/eventdriven/services/radar/radar_base_reflectivity/MapServer/WMSServer";
var radarWMS = L.tileLayer.wms(wmsUrl, {
  layers: "1",
  format: "image/png",
  transparent: true,
  opacity: 0.8,
  attribution: "nowCOAST",
});
radarWMS.addTo(map);

function goToMainCampus(){
  map.flyTo([46.897357855724714, -96.80289743876295], 15)
}

function goToBarryHall(){
  map.flyTo([46.878785000568264, -96.79341316094806], 18)
}

function goToRenaissanceHall(){
  map.flyTo([46.87559110464578, -96.79051636055985], 18)
}