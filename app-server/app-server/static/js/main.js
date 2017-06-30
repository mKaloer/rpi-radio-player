var socket = null;
var radio = new Radio();
var radioController = new RadioController();

$(document).ready(function() {
    // Materialize CSS menu setup
    $(".button-collapse").sideNav();

    rivets.bind($('#player-card'), {radio: radio, radioController: radioController});
    rivets.bind($('.stations-card'), {radio: radio, radioController: radioController});
    rivets.bind($('#add-station-card'), {radio: radio, radioController: radioController});
    socket = io.connect("http://" + window.location.hostname + "/socket.io");
    socket.nsp = "/";
    socket.on('status', function(status) {
	if ($('#volume-slider:active')[0]) {
	    // Currently dragging volume. Do nothing value
	    status.volume = radio.status.volume;
	}
	radio.status = status;
    });
    socket.on('station', function(station) {
	// Update stations list
	existing_station = radio.stations.filter(function (s) { return s.id === station.id; })[0];
	if (!existing_station) {
	    // Station does not exist. Update list.
	    radio.get_stations();
	} else {
	    if (station.is_favorite && !existing_station.is_favorite) {
		// Add to list
		radio.favorites.push(existing_station);
	    } else if (!station.is_favorite && existing_station.is_favorite) {
		// Remove from list
		radio.favorites.splice(radio.favorites.indexOf(existing_station),1);
	    }
	    existing_station.is_favorite = station.is_favorite;
	}
    });

    radio.socket = socket;
});

// Rivets formatters
rivets.formatters.station_name = function(status){
    if (status.name) {
	return status.name;
    } else {
	if (status.state == "PLAYING") {
	    return "Unknown name";
	} else {
	    return "Not playing";
	}
    }
}

rivets.formatters.negate = function(value) {
    return !value;
};

rivets.formatters.eq = function(value, args) {
    return value === args;
};

rivets.formatters.neq = function(value, args) {
    return value != args;
};
