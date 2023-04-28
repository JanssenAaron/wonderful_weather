var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var wmsUrl = "https://nowcoast.noaa.gov/arcgis/services/nowcoast/radar_meteo_imagery_nexrad_time/MapServer/WMSServer"
var radarWMS = L.tileLayer.wms(wmsUrl, {
    layers: '1',
    format: 'image/png',
    transparent: true,
    opacity: 0.8,
    attribution: 'nowCOAST'
});
radarWMS.addTo(map)
