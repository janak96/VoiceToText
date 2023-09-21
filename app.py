from vosk import Model, KaldiRecognizer
import pyaudio

# define the model
model = Model("./Vosk/vosk-model-small-hi-0.22")
recognizer = KaldiRecognizer(model,16000)


# get mic input stream
mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

# Lorem Ipsum

# read the stream and make out the text
while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())

