from concurrent import futures
import grpc
from speech_recognition_service import SpeechRecognizer
from stub.speech_recognition_open_api_pb2_grpc import add_SpeechRecognizerServicer_to_server
from lib.inference_lib import Wav2VecCtc
from auth_interceptor import AuthInterceptor


MAX_MESSAGE_LENGTH = 50 * 1024 * 1024

def run():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        # interceptors=(AuthInterceptor('Bearer mysecrettoken'),)
        
    	options = [('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)] 
        
        
    )
    add_SpeechRecognizerServicer_to_server(SpeechRecognizer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
