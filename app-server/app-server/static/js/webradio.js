_send_request = function(obj, endpoint, params, callback, type = "GET", data = null) {
    if (Object.keys(params).length === 0) {
	var param_list = "";
    } else {
	var param_list = '?' + $.param(params);
    }

    var url = "http://192.168.1.108/api/" + endpoint + param_list

    var callback_curry = function(data) {
	callback(obj, data);
    }

    var json_data = data ? JSON.stringify(data) : null;
    var content_type = data ? "application/json; charset=utf-8" : null;
    $.ajax({
	url: url,
	type: type,
	data: json_data,
	contentType: content_type,
	success: callback_curry
    });
};

function Radio() {
    this.play_url = function(url) {
	_send_request(this, 'play', {
	    'url': url
	}, function(radio, data) {
	    radio.status = data;
	}, "POST");
    };
    this.play_station = function(station_id) {
	_send_request(this, 'play', {
	    'station_id': station_id
	}, function(radio, data) {
	    radio.status = data;
	}, "POST");
    };
    this.stop = function() {
	_send_request(this, 'stop', {}, function(radio, data) {
	    radio.status = data;
	}, "POST");
    };
    this.get_status = function() {
	_send_request(this, 'status', {}, function(radio, data) {
	    radio.status = data;
	}, "GET");
    };
    this.get_stations = function() {
	_send_request(this, 'stations', {}, function(radio, data) {
	    radio.stations = data;
	    radio.favorites = radio.stations.filter(function(s) { return s.is_favorite; });
	}, "GET");
    };
    this.add_station = function(name, url) {
	_send_request(this, 'stations', {}, function(radio, data) {

	}, "POST", {
	    "name": name,
	    "url": url
	});
    };

    this.status = {};
    this.stations = [];
    this.favorites = [];
    this.get_status();
    this.get_stations();
};

function RadioController() {
    this.play_station = function(e, view) {
	var station = view.station;
	var radio = view.radio;
	radio.play_station(station.id);
    };
    this.play_pause_current = function(e, view) {
	var radio = view.radio;
	if (radio.status.state === "PLAYING") {
	    radio.stop();
	} else {
	    radio.play_url(radio.status.url);
	}
    };
    this.stop = function(e, view) {
	var radio = view.radio;
	radio.stop();
    };
    this.set_favorite = function(e, view) {
	var station = view.station;
	_send_request(station, 'stations/' + station.id, {}, function(station, data) {
	}, "PUT", {
	    'name': station.name,
	    'url': station.url,
	    "is_favorite": !station.is_favorite,
	});
	if (station.is_favorite) {
	    // Remove station from favorites list
	    radio.favorites.splice(radio.favorites.indexOf(station),1);
	    station.is_favorite = false;
	} else {
	    // Add station from favorites list
	    radio.favorites.push(station);
	    station.is_favorite = true;
	}
    };
    this.add_station = function(e, view) {
	e.preventDefault();
	var radio = view.radio;
	var name = $(this).find("#add-station-name")[0];
	var url = $(this).find("#add-station-url")[0];
	var form = $.find("#add-station-form")[0];
	radio.add_station(name.value, url.value);
	form.reset();
	Materialize.updateTextFields();
    };
};
