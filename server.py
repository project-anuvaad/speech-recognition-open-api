from concurrent import futures
import grpc
from speech_recognition_service import SpeechRecognizer
from stub.speech_recognition_open_api_pb2_grpc import add_SpeechRecognizerServicer_to_server
from inference_lib.wav2vec_ctc import Wav2VecCtc


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SpeechRecognizerServicer_to_server(SpeechRecognizer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
