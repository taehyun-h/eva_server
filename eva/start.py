from eva.protocol.service import sign
from concurrent import futures
import time
import grpc


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add service
    sign.add_servicer_to_server(server)
    server.add_insecure_port('[::]:50051')

    # start server
    print("Start Server")
    server.start()

    # keep running python
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


run_server()
