from concurrent import futures
import logging
import time

import grpc

import radiomessages_pb2_grpc
import radiomessages_pb2
import radio

class RadioServicer(radiomessages_pb2_grpc.RadioServicer):


    STATE_PLAYING = 'PLAYING'
    STATE_STOPPED = 'STOPPED'
    STATE_MUTED = 'MUTED'

    _curr_url = None
    _curr_state = STATE_STOPPED


    def Play(self, request, context):
        if not request.url:
            if self._curr_url:
                # Get last URL
                url = self._curr_url
                logging.debug("Play prev url: %s", url)
            else:
                # No known url
                logging.debug("Play requested, but no URL to play")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("No URL to play")
                return radiomessages_pb2.StatusResponse()
        else:
            url = request.url
            logging.debug("Play new url: %s", url)

        self._curr_url = url
        self._curr_state = RadioServicer.STATE_PLAYING

        radio.play_url(url)
        return self._get_status()


    def Stop(self, request, context):
        logging.debug("Stopping")
        self._curr_state = RadioServicer.STATE_STOPPED
        radio.stop()
        return self._get_status()


    def Status(self, request, context):
        logging.debug("Status requested")
        return self._get_status()


    def _get_status(self):
        return radiomessages_pb2.StatusResponse(url=self._curr_url, state=self._curr_state)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    radiomessages_pb2_grpc.add_RadioServicer_to_server(
        RadioServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    while True:
        time.sleep(10000)


if __name__ == "__main__":
    serve()
