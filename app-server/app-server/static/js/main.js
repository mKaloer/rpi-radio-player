var radio = new Radio();
var radioController = new RadioController();
var socket = null;

$(document).ready(function() {
    // Materialize CSS menu setup
    $(".button-collapse").sideNav();

    $("#add-station-form").submit(function(e) {
	var name = $(this).find("#add-station-name")[0].value;
	var url = $(this).find("#add-station-url")[0].value;
	radio.add_station(name, url);
	e.preventDefault();
    });

    rivets.bind($('#player-card'), {radio: radio, radioController: radioController});
    rivets.bind($('#favorites-card'), {radio: radio, radioController: radioController});
    rivets.bind($('#stations-card'), {radio: radio, radioController: radioController});
    rivets.bind($('#add-station-card'), {radio: radio, radioController: radioController});
    socket = io.connect("http://" + window.location.hostname + "/socket.io");
    socket.nsp = "/";
    socket.on('status', function(status) {
	radio.status = status;
    });
});

// Rivets formatters
rivets.formatters.play_btn = function(value){
    if (value === "PLAYING") {
	return "pause_circle_filled"
    } else {
	return "play_circle_filled"
    }
}
rivets.formatters.favorite_icon = function(value){
    if (value === true) {
	return "favorite"
    } else {
	return "favorite_border"
    }
}
