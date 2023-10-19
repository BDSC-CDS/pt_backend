import sys
print(sys.path)

from concurrent import futures
import time
import grpc
import api.v1.templatebackend.index_pb2_grpc as index_service
from internal.api.v1.index_controller import IndexController
import logging

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Register user service    

    index_serve = IndexController()
    index_service.add_IndexControllerServicer_to_server(index_serve, server)    
    
    server.add_insecure_port('[::]:50051')
    server.start()    
    
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        logging.debug('GRPC stop')
        server.stop(0)

if __name__ == '__main__':
    grpc_server()