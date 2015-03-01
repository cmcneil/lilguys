function create_location_maps_widget(map_div_id, lat_input_id, lng_input_id) {
    // Load the map
    var mapOptions = {
        center: { lat: 37.7833, lng: -122.417},
        zoom: 10
    };
    var map = new google.maps.Map(document.getElementById(map_div_id), mapOptions);
    
    // Create an onclick listener
    google.maps.event.addListener(map, "click", function(event) {
        var latitude = event.latLng.lat();
        var longitude = event.latLng.lng();

        var lat_input = document.getElementById(lat_input_id);
        var lng_input = document.getElementById(lng_input_id);

        lat_input.value = latitude;
        lng_input.value = longitude;
    });
}
