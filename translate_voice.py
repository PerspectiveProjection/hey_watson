from watson_developer_cloud import SpeechToTextV1
import json
import config

stt = SpeechToTextV1(username=config.stt_user, password=config.stt_password)
audio_file = open('test.wav', 'rb')
audio_data = stt.recognize(audio_file, content_type='audio/wav')
print audio_data['results'][0]['alternatives'][0]['transcript']
