import sys
import pyaudio
import wave

def play_audio(stream):
    chunk = 1024
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
