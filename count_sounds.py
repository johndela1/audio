#!/usr/bin/env python3

import struct
import sys
import time


FORMAT = '<i' # single 32 bit integer
SAMPLERATE = 48e3

count = 0
t1 = time.time()

def smooth(old, new, factor=.35):
    return (old*(1-factor)) + (new*factor)
with open("/dev/stdin", "rb", buffering=0) as f:
    decay = 0
    bpm = 60
    start_time = time.time()
    while(True):
        try:
            raw = f.read(struct.calcsize(FORMAT))
            v = struct.unpack(FORMAT, raw)[0]
        except struct.error:
            break
        if decay:
            decay -= 1
            continue
        if abs(v) > 92e6:
            t2 = time.time()
            bpm = smooth(bpm, 60/(t2-t1))
            t1 = t2
            count += 1
            print(count, bpm, count/((t2-start_time)/60))
            decay = SAMPLERATE * .1
