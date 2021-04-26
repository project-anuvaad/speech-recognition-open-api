import pytest

from stub.speech_recognition_open_api_pb2 import RecognitionInput, SpeechRecognitionRequest, RecognitionConfig, \
    RecognitionAudio, Language, SpeechRecognitionResult


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from stub.speech_recognition_open_api_pb2_grpc import add_SpeechRecognizerServicer_to_server
    return add_SpeechRecognizerServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from speech_recognition_service import SpeechRecognizer
    return SpeechRecognizer()


@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from stub.speech_recognition_open_api_pb2_grpc import SpeechRecognizerStub
    return SpeechRecognizerStub


# def test_if_audio_url_is_handled(grpc_stub):
#     audio_url = "http://localhost/audio.mp3"
#     request = RecognitionInput(audio_url=audio_url)
#     response = grpc_stub.recognize(request)
#     assert response.result == audio_url
#
#
# def test_if_audio_bytes_is_handled(grpc_stub):
#     audio_bytes = b"http://localhost/audio.mp3"
#     request = RecognitionInput(audio_bytes=audio_bytes)
#     response = grpc_stub.recognize(request)
#     assert response.result == str(audio_bytes)


def test_recognize_v2(grpc_stub):
    audio_bytes = b"http://localhost/audio.mp3"
    lang = Language(value='en', name='English')
    config = RecognitionConfig(language=lang, transcriptionFormat='SRT', samplingRate='_44KHZ')
    audio = RecognitionAudio(audioContent=audio_bytes)
    request = SpeechRecognitionRequest(audio=audio, config=config)
    resp = grpc_stub.recognizeV2(request)
    assert SpeechRecognitionResult.Status.Name(resp.status) == 'SUCCESS'
