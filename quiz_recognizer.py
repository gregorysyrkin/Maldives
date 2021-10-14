import numpy
from matplotlib import pyplot, mlab
import scipy.io.wavfile
from collections import defaultdict

SAMPLE_RATE = 22050 # Hz
WINDOW_SIZE = 2048 # размер окна, в котором делается fft
WINDOW_STEP = 512 # шаг окна
WINDOW_OVERLAP = WINDOW_SIZE - WINDOW_STEP

def get_wave_data(wave_filename):
    sample_rate, wave_data = scipy.io.wavfile.read(wave_filename)
    assert sample_rate == SAMPLE_RATE, sample_rate
    if isinstance(wave_data[0], numpy.ndarray): # стерео
        wave_data = wave_data.mean(1)
    return wave_data

def show_specgram(wave_data):
    fig = pyplot.figure()
    ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
    ax.specgram(wave_data,
        NFFT=WINDOW_SIZE, noverlap=WINDOW_SIZE - WINDOW_STEP, Fs=SAMPLE_RATE)
    pyplot.show()

def get_fingerprint(wave_data):
    # pxx[freq_idx][t] - мощность сигнала
    pxx, _, _ = mlab.specgram(wave_data,
        NFFT=WINDOW_SIZE, noverlap=WINDOW_OVERLAP, Fs=SAMPLE_RATE)
    band = pxx[15:250]  # наиболее интересные частоты от 60 до 1000 Hz
    return numpy.argmax(band.transpose(), 1)  # max в каждый момент времени

wave_data = get_wave_data('CantinaBand60.wav')
wave_data2 = get_wave_data('BabyElephantWalk60.wav')
wave_data3 = get_wave_data('BabyElephantWalk60.wav')
#show_specgram(wave_data)

fingerprint = get_fingerprint(wave_data)
fingerprint2 = get_fingerprint(wave_data2)
fingerprint3 = get_fingerprint(wave_data3)

assert ((fingerprint2 == fingerprint3).all())

print("end")