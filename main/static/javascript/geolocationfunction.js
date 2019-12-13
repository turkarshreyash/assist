var loc = document.getElementById("loc");
function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      loc.innerHTML = "Geolocation is not supported by this browser.";
    }
  }
  
  function showPosition(position) {
    loc.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
  }