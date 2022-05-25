import librosa
import scipy.signal as signal
import numpy as np
import tensorflow as tf

audio_sample, sampling_rate = librosa.load("akmu.wav", sr=None)

S = np.abs(librosa.stft(audio_sample, n_fft=1024, hop_length=512, win_length=1024, window=signal.hann))
pitches, magnitudes = librosa.piptrack(S=S, sr=sampling_rate)


from spleeter.separator import Separator
Separator.__init__(self=Separator)
Separator._separate_librosa(self=Separator, waveform=S, audio_descriptor=2)