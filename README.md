# Raspberry Pi Internet Radio
Internet radio controlled with a web-based front-end or a REST api.


## Setup
All components are implemented as docker containers. To start, install Docker and docker-compose and run
```
docker-compose up
```
This will start all containers and a web server will be accessible at port 8080.

## API reference
The radio API is used to control the radio and to manage stations. The endpoints are:

### Play
```
POST /api/play
```

#### Parameters:
| Parameter               | Value                         |
| ------------------------|-------------------------------|
| `url` (optional)        | The station URL to play       |
| `station_id` (optional) | The id of the station to play |

#### Response:
A status message. For example:
```
{
   "volume":100,
   "bitrate":"92",
   "state":"PLAYING",
   "name":"DR P6 BEAT",
   "url":"http://live-icy.gss.dr.dk/A/A29H.mp3.m3u",
   "title":"Senest spillet: Yuk Foo | Wolf Alice"
}
```
The state can either be `PLAYING` or `STOPPED`.

### Stop
```
POST /api/stop
```

#### Response:
A status message.

### Volume
```
POST /api/volume
```

#### Parameters:
| Parameter   | Value                          |
| ------------|--------------------------------|
| `vol`       | The volume (between 0 and 100) |

#### Response:
A status message.

### Station list
```
GET /api/stations
```

#### Parameters:
| Parameter                | Value                                                              |
|--------------------------|--------------------------------------------------------------------|
| `is_favorite` (optional) | Boolean value specifying whether to only receive favorite stations |

#### Response:
An array of stations:
```
[
   {
      "id":2,
      "url":"http://live-icy.gss.dr.dk/A/A03H.mp3.m3u",
      "is_favorite":false,
      "name":"DR P1"
   },
   {
      "id":3,
      "url":"http://live-icy.gss.dr.dk/A/A04H.mp3.m3u",
      "is_favorite":false,
      "name":"DR P2"
   },
   {
      "id":5,
      "url":"http://live-icy.gss.dr.dk/A/A10H.mp3.m3u",
      "is_favorite":false,
      "name":"DR P4 Nordjylland"
   }
]
```

### Station info
```
GET /api/stations/[station_id]
```

#### Response:
A station object:
```
{
   "id":2,
   "url":"http://live-icy.gss.dr.dk/A/A03H.mp3.m3u",
   "is_favorite":false,
   "name":"DR P1"
}
```

### Station modification
Stations can be created with `POST` requests:
```
POST /api/stations/
```
With data containing a new station object.


Stations can be updated with `PUT` requests:
```
PUT /api/stations/[station_id]
```

and deleted with `DELETE` requests:
```
DELETE /api/stations/[station_id]
```

## Architecture
The entire project is structured in five Docker containers: app-server (front-end), api-server, web-radio (the radio component), db (PostgreSQL), and nginx.

The front-end is styled with [Materialize](http://materializecss.com/) and implemented using [Rivets.js](http://rivetsjs.com/) and [Socket.io](https://socket.io/). The web-servers (front-end and API) are implemented with [Flask](http://flask.pocoo.org/) running behind [Gunicorn](http://gunicorn.org/) and [nginx](https://nginx.org/). The web radio is implemented using [Music Player Daemon](https://www.musicpd.org/). All communication between containers is done using [GRPC](http://www.grpc.io/).


## General Setup Tips
To improve the analogue audio output, add the following line to `/boot/config.txt`
```
audio_pwm_mode=2
```
(via [this forum post](https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=136445))
