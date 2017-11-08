import sys
import pyaudio
import wave
import config
from watson_developer_cloud import VisualRecognitionV3, TextToSpeechV1

chunk = 1024

def classify_image(image):
    tts = TextToSpeechV1(username=config.tts_user,\
            password=config.tts_password)
    visual_recognition = VisualRecognitionV3('2016-05-20',\
                    api_key=config.vision_api)
    with open('frame.jpg', 'rb') as f:
            results = visual_recognition.classify(images_file=f)
            for classes in results["images"][0]["classifiers"][0]["classes"]:
                    speech = tts.synthesize(classes["class"], 'en-US_AllisonVoice',
                                    'audio/wav')
                    with open('test.wav', 'wb') as f:
                            f.write(speech)
                    print(classes["class"])
                    wf = wave.open('test.wav', 'rb')
                    p = pyaudio.PyAudio()
                    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(), rate=wf.getframerate(),
                                    output=True)
                    data = wf.readframes(chunk)
                    while data != '':
                            stream.write(data)
                            data=wf.readframes(chunk)
                    stream.close()
                    p.terminate()
    return

classify_image(sys.argv[1])
