import sys
import pyaudio
import wave
import config
import play_audio
from watson_developer_cloud import VisualRecognitionV3, TextToSpeechV1

chunk = 1024

def classify_image(image):
    wav_file = open('test.wav', 'wb')
    wav_file.write('')
    tts = TextToSpeechV1(username=config.tts_user,\
            password=config.tts_password)
    visual_recognition = VisualRecognitionV3('2016-05-20',\
                    api_key=config.vision_api)
    with open(image, 'rb') as f:
        results = visual_recognition.classify(images_file=f)
        for classes in results["images"][0]["classifiers"][0]["classes"]:
            speech = tts.synthesize(classes["class"], 'en-US_AllisonVoice',
                            'audio/wav')
            with open('test.wav', 'a') as f:
                f.write(speech)
            print(classes["class"])
    return

classify_image(sys.argv[1])
play_audio.play_audio('test.wav')
