import numpy as np
from scipy.fftpack import dct
import librosa

def load_audio__(audio):
  signal, sampling_rate = librosa.load(audio)
  return signal, sampling_rate

def emphasis__(signal, coef=0.97):
  return np.append(signal[0], signal[1:] - coef * signal[:-1])

def framing__(signal, sampling_rate=44100, frame_size=1, frame_stride=0.5):
  frame_length, frame_step = frame_size * sampling_rate, frame_stride * sampling_rate  # Convert from seconds to samples
  signal_length = len(signal)
  frame_length = int(round(frame_length))
  frame_step = int(round(frame_step))
  num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step) + 1)  # Make sure that we have at least 1 frame

  pad_signal_length = (num_frames - 1) * frame_step + frame_length
  z = np.zeros((pad_signal_length - signal_length))
  pad_signal = np.append(signal, z) # Pad Signal to make sure that all frames have equal number of samples without truncating any samples from the original signal

  indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
  return pad_signal[indices.astype(np.int32, copy=False)]

def windowing__(signal, sampling_rate=44100, frame_size=1):
  windowed = signal * np.hamming(int(round(frame_size * sampling_rate)))
  # frames *= 0.54 - 0.46 * numpy.cos((2 * numpy.pi * n) / (frame_length - 1))
  return windowed

def fft__(signal, NFFT=512):
  mag_frames = np.absolute(np.fft.rfft(signal, NFFT))  # Magnitude of the FFT
  return ((1.0 / NFFT) * ((mag_frames) ** 2)) # Power Spectrum

def melbank__(signal, nfilt=40, sr=44100, NFFT=512):
  low_freq_mel = 0
  high_freq_mel = (2595 * np.log10(1 + (sr / 2) / 700))  # Convert Hz to Mel
  mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  # Equally spaced in Mel scale
  hz_points = (700 * (10**(mel_points / 2595) - 1))  # Convert Mel to Hz
  bin = np.floor((NFFT + 1) * hz_points / sr)

  fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
  for m in range(1, nfilt + 1):
    f_m_minus = int(bin[m - 1])   # left
    f_m = int(bin[m])             # center
    f_m_plus = int(bin[m + 1])    # right

    for k in range(f_m_minus, f_m):
      fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
    for k in range(f_m, f_m_plus):
      fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
  filter_banks = np.dot(signal, fbank.T)
  filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)  # Numerical Stability
  return (20 * np.log10(filter_banks)), fbank

def dct__(signal, coef=13):
  return dct(signal, type=2, axis=1, norm='ortho')[:, 1 : (coef + 1)]
