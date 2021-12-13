# from ml4a import image
from ml4a import audio
from ml4a.models import wav2lip
import cv2
import librosa
import librosa.filters

def load_wav(path, sr):
    return librosa.load(path)
    # return librosa.core.load(path, sr=sr)[0]

# input_image = image.monalisa()
# input_image = cv2.imread('face.png')
# input_image = '/home/A100_data/ETC/no_5_sample_hq_bright.mp4'
input_image = 'output.mp4'

sample_rate = 52000
f = open('sentence.txt', 'r', encoding='utf-8')
encText = f.readline()
print(encText)
# tts = gTTS(text=line, lang='ko')

import urllib.request
client_id = "zhtscjxj2c"
client_secret = "RLcjNhiXZbzxbuuWOoOtV8jCTHILfAAVRCMr3tYW"
	# encText = urllib.parse.quote("qwer")
data = "speaker=nsunhee&volume=0&speed=0&pitch=0&format=mp3&text=" + encText;
url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
request.add_header("X-NCP-APIGW-API-KEY", client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

print("TTS mp3 저장")
response_body = response.read()
with open('HLHLHLHLHLHL.mp3', 'wb') as f:
	f.write(response_body)

print('tts done')
input_audio = load_wav('./HLHLHLHLHLHL.mp3', sample_rate)

wav2lip.run(input_image,
            input_audio,
            sampling_rate = sample_rate,
            output_video = 'wav2lip_example.mp4',
            pads = [0, 10, 0, 0],
            resize_factor = 2,
            crop = None,
            box = None, rotate=True)
