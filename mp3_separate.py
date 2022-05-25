import librosa
import scipy.signal as signal
import numpy as np
import pydub
from pydub import AudioSegment

import os
# 2stems = vocals and accompaniment
# 4stems = vocals, drums, bass, and other
# 5stems = vocals, drums, bass, piano, and other
stems = str(input('stems 선택 : 2, 4, 5 >>>'))
path = str(input(r'파일이 있는 경로를 정해주세요. >>>'))
os.chdir(path)
file_name = str(input('음악 파일의 이름을 적어주세요. >>>'))

nsfile_name = file_name.replace(' ', '_')

try:
    os.rename(path+file_name+'.mp3', path+nsfile_name+'.mp3')
except FileNotFoundError:

# files
src = "musicfile/start(gaho).mp3"
dst = "musicfile/start(gaho)ver3.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


    pass
print('기다려주세요.')
spl = r'spleeter separate -p spleeter:' + \
    str(stems)+r'stems -o output '+nsfile_name+'.mp3'
# 'spleeter separate -p spleeter:2stems -o output my_song.mp3'
os.system(spl)

audio_sample, sampling_rate = librosa.load("musicfile/start(gaho)ver3.wav", sr = None)

S = np.abs(librosa.stft(audio_sample, n_fft=1024, hop_length=512, win_length = 1024, window=signal.hann))
pitches, magnitudes = librosa.piptrack(S=S, sr=sampling_rate)

shape = np.shape(pitches)
nb_samples = shape[0]
nb_windows = shape[1]

for i in range(0, nb_windows):
    index = magnitudes[:,i].argmax()
    pitch = pitches[index,i]