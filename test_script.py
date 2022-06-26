import numpy as np
import pyaudio
import json
import ctypes
from ctypes import *

lib = ctypes.cdll.LoadLibrary(".\\SimpleLipSync.dll")
lib.voice2bs.restype = c_voidp

FORMAT = pyaudio.paInt16
CHUNK = 640
CHANNELS = 1
RATE = 16000


attr_names = ["jawOpen", "mouthFunnel",
              "mouthPucker", "mouthRollUpper", "mouthRollLower"]


def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(input_device_index=0,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    last_output = 0
    init_flag = True
    while 1:
        """
        read pcm data from your device
        change the input_device_index to your microphone index
        """
        data = stream.read(CHUNK, exception_on_overflow=True)
        data = np.frombuffer(data, np.int16)
        data = data/(1 << 15)
        data = data.tolist()
        indata = (c_float*CHUNK)()
        for ix in range(len(data)):
            indata[ix] = data[ix]
        outdata = (c_float*52)()
        for ix in range(52):
            outdata[ix] = 0
        len_p = c_int(CHUNK)
        mp = ctypes.c_char_p(".\\".encode())
        lib.init_model(mp)
        lib.voice2bs(ctypes.pointer(indata), len_p, ctypes.pointer(outdata))
        out = []
        for x in outdata:
            out.append(x)
        out = np.array(out)[[17, 19, 20, 32, 31]]
        if init_flag:
            last_output_t = out
            out = (out+last_output)/2
            last_output = last_output_t
        else:
            last_output = out
            init_flag = False
        out = out.tolist()
        ret = json.dumps([out, attr_names])
        print(ret)

    stream.stop_stream()
    stream.close()
    p.terminate()


record_audio()
