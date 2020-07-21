#!/usr/bin/env python3

import struct
import sys
import time


FORMAT = "<i"  # single 32 bit integer
SAMPLERATE = 48e3

count = 0
t1 = time.time()
decay = 0
bpm = 60
start_time = time.time()
decay_factor = 0.4


def smooth(old, new, factor):
    assert factor <= 1
    return (old * factor) + (new * (1 - factor))


with open("/dev/stdin", "rb", buffering=0) as f:
    while True:
        try:
            raw = f.read(struct.calcsize(FORMAT))
            amplitude = struct.unpack(FORMAT, raw)[0]
        except struct.error:
            break
        if decay:
            decay -= 1
            continue
        if abs(amplitude) > 52e6:
            t2 = time.time()
            bpm = smooth(bpm, 60 / (t2 - t1), factor=0.25)
            t1 = t2
            count += 1
            print(count, "{:.1f}".format(bpm))
            decay = SAMPLERATE * decay_factor
