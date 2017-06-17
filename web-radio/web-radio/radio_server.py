from concurrent import futures
import logging
import time

import grpc

import radiomessages_pb2_grpc
import radiomessages_pb2
import radio

logger = logging.getLogger(__name__)

class RadioServicer(radiomessages_pb2_grpc.RadioServicer):


    STATE_PLAYING = 'PLAYING'
    STATE_STOPPED = 'STOPPED'
    STATE_MUTED = 'MUTED'

    _curr_url = None
    _curr_state = STATE_STOPPED

    def __init__(self):
        self.radio = radio.Radio()


    def Play(self, request, context):
        logger.info("Received play request. Url: %s", request.url)
        if not request.url:
            if self._curr_url:
                # Get last URL
                url = self._curr_url
                logger.debug("Play prev url: %s", url)
            else:
                # No known url
                logger.debug("Play requested, but no URL to play")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("No URL to play")
                return radiomessages_pb2.StatusResponse()
        else:
            url = request.url
            logger.debug("Play new url: %s", url)

        self._curr_url = url
        self._curr_state = RadioServicer.STATE_PLAYING

        self.radio.play_url(url)
        return self._get_status()


    def Stop(self, request, context):
        logger.info("Received stop request")
        self._curr_state = RadioServicer.STATE_STOPPED
        self.radio.stop()
        return self._get_status()


    def Status(self, request, context):
        logger.info("Received status request")
        return self._get_status()


    def _get_status(self):
        status = self.radio.get_status()
        return radiomessages_pb2.StatusResponse(
            url=self._curr_url,
            state=self._curr_state,
            title=status['title'],
            name=status['name'],
            volume=RadioServicer._try_int(status['volume']),
            bitrate=RadioServicer._try_int(status['bitrate']),
        )


    @staticmethod
    def _try_int(val):
        if val is None:
            return None
        else:
            return int(val)


def serve():
    logging.info("Creating grpc server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    radiomessages_pb2_grpc.add_RadioServicer_to_server(
        RadioServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("grpc server started")
    while True:
        time.sleep(10000)


if __name__ == "__main__":
    serve()
