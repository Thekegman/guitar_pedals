import sounddevice as sd
from numpy import array, sin,cos, pi, real, fft
from matplotlib.pyplot import plot,show
from scipy.io import wavfile
from scipy import signal


fs, data = wavfile.read(r'normal.wav')
b, a = signal.butter(20, 0.22, 'low', analog=False)

audio = data[:,0]
def gen_delay(freq, r, phase, fs):
    i = 0
    while True:
        yield int((r/2)*sin(freq*2*pi*i/fs+ phase)-r/2)
        i+=1

#sd.stop()
y = []
delay1 = gen_delay(5,80,0,fs)
for i,sample in enumerate(audio):
    d1 = next(delay1)
    # check not shifted out of bounds
    d1 = -i if d1+i < 0 else d1
        
    y.append(audio[i+d1])

print("playing")


#y = signal.lfilter(b, a, y)
y = array(y, dtype="int16")
wavfile.write(r'vibrato.wav', fs, y)

sd.play(array(y, dtype="int16"), fs)

input()
