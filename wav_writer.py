import random
import struct
import wave


sample_rate = 44100.0  # hertz
duration = 1.0  # seconds
frequency = 440.0  # hertz

wav = wave.open("sample.wav", "w")
wav.setnchannels(1) # mono
wav.setsampwidth(2)
wav.setframerate(sample_rate)

# Create a wav file _ hissy noise
for i in range(2000):
    value = random.randint(-32767, 32767)
    data = struct.pack('<h', value)
    wav.writeframesraw(data)

wav.close()