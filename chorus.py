import sounddevice as sd
from numpy import array, sin,cos, pi, real, fft
from matplotlib.pyplot import plot,show
from scipy.io import wavfile
from scipy import signal


fs, data = wavfile.read(r'normal.wav')
audio = data[:,0]

def gen_delay(freq, r, phase, fs):
    i = 0
    while True:
        yield int((r/2)*sin(freq*2*pi*i/fs+ phase)-r/2)
        i+=1

#sd.stop()
y = []
delay1 = gen_delay(5,50,0,fs)
delay2 = gen_delay(2,200,pi/2,fs)
for i,sample in enumerate(audio):
    d1 = next(delay1)
    d2 = next(delay2)
    
    # check not shifted out of bounds
    d1 = -i if d1+i < 0 else d1
    d2 = -i if d2+i < 0 else d2


        
    y.append(0.50*sample+0.25*audio[i+d1]+0.25*audio[i+d2])

print("playing")
y = array(y, dtype="int16")
wavfile.write(r'chorus.wav', fs, y)

sd.play(array(y, dtype="int16"), fs)

input()