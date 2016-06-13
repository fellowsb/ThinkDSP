# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:37:11 2016

@author: Ben
"""

from __future__ import print_function, division

import thinkdsp
import thinkplot
import numpy as np

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

from matplotlib import pyplot

#chirp_sig = thinkdsp.ExpoChirp(start=220, end=10000)
#chirp_wav = chirp_sig.make_wave(duration=1, framerate=96000)

##chirp_wav.write(filename='chirp.wav')
##thinkdsp.play_wave(filename='chirp.wav', player='vlc')
#
#spectrogram = chirp_wav.make_spectrogram(seg_length=1024)
#spectrogram.plot(high=15000)

#sig = thinkdsp.SinSignal(freq=440)
#duration = sig.period*1000.25
#wave = sig.make_wave(duration, framerate=96000)
#spec = wave.make_spectrum()
#
#spec.plot()
#pyplot.xlim(400,500)
#thinkplot.show()
#
#hamming_wav = wave
#hamming_wav.hamming()
#hamming_spec = hamming_wav.make_spectrum()
#
#hamming_spec.plot()
#pyplot.xlim(400,500)
#thinkplot.show()
#
#kaiser_window = np.kaiser(len(wave.ys), 5)
#kaiser_wav = wave
#kaiser_wav.window(kaiser_window)
#kaiser_spec = kaiser_wav.make_spectrum()
#
#kaiser_spec.plot()
#pyplot.xlim(400,500)
#thinkplot.show()

class SawtoothChirp(thinkdsp.Chirp):
    def __init__(self, fundamental=1, offset=0, start=440, end=880, amp=1.0):
        self.freq = fundamental
        self.offset = offset
        self.start = start
        self.end = end
        self.amp = amp
        
    def evaluate(self, ts):
        ts = np.asarray(ts)
        cycles = self.freq * ts + self.offset / thinkdsp.PI2
#        frac, _ = np.modf(cycles)
#        ys = normalize(frac, self.amp)
        
        num_cycles = int(round(cycles[len(cycles)-1]))
        print(num_cycles, "num_cycles")
        cycle_ts = ts[:round((len(ts)-1)/num_cycles)]
        
        freqs = np.linspace(self.start, self.end, len(cycle_ts)-1)
        dts = np.diff(cycle_ts)
        dps = thinkdsp.PI2 * freqs * dts
        phases = np.cumsum(dps)
        phases = np.insert(phases, 0, 0)

        ys = np.zeros((num_cycles*len(cycle_ts)+1))
        
        for i in range(num_cycles):
            n = i*len(cycle_ts)+1
            print("n=", n)
            ys[n:n+len(cycle_ts)] = self.amp * np.cos(phases)
        
        ys = np.asarray(ys)
        ys = ys[:(len(ys)-1)]
#        ys = thinkdsp.normalize(ys, self.amp)        
        
        return ys
        
sig = SawtoothChirp()
wav = sig.make_wave(duration=3, framerate=11025)
#wav.normalize()
print(len(wav.ys), "ys", len(wav.ts), "ts")
wav.plot()
thinkplot.show()

wav.write(filename="chirp.wav")
thinkdsp.play_wave(filename="chirp.wav", player='vlc')