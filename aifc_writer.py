import aifc
import random
import struct

sample_rate = 44100.0 # hertz

obj = aifc.open('sound.aiff','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sample_rate)

for i in range(99999):
    value = random.randint(-32767, 32767)
    data = struct.pack('<h', value)
    obj.writeframesraw( data )

obj.close()