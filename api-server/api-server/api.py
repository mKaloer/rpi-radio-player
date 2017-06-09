from flask import Flask, jsonify, request

import radio_rpc

app = Flask(__name__)
radio = radio_rpc.RadioRPC('web-radio:50051')

@app.route("/play", methods=['POST'])
def play():
    url = request.args.get('url')
    if url:
        app.logger.debug("Play: " + url)
    try:
        status = radio.play(url)
        return _format_status(status)
    except ValueError as e:
        response = jsonify({
            'msg': str(e)
        })
        response.status_code = 400
        return response


@app.route("/stop", methods=['POST'])
def stop():
    status = radio.stop()
    return _format_status(status)


@app.route("/status")
def radio_status():
    status = radio.get_status()
    return _format_status(status)


def _format_status(status):
    return jsonify({
        'url': status['url'],
        'state': status['state'].name
    })
