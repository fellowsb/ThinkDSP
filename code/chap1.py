# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 04:49:08 2016

@author: ben
"""
from __future__ import print_function, division

import thinkdsp
import thinkplot
import datetime
import numpy as np

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

from matplotlib import pyplot

def stretch(wave, stretch_factor):
    return thinkdsp.Wave(wave.ys, 
                         wave.ts / stretch_factor, 
                         framerate=wave.framerate * stretch_factor
                         )

start_time = datetime.datetime.now()

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.CosSignal(freq=1000, amp=0.5, offset=0)

mix = sin_sig + cos_sig

wave = mix.make_wave(duration=0.5, start=0, framerate=10000)

period = mix.period
segment = wave.segment(start=0, duration=period*3)

segment.plot()
thinkplot.show()

mix_spectrum = wave.make_spectrum()

mix_spectrum.plot()
thinkplot.show()

stretched_seg = stretch(segment, 0.5)
stretched_seg.plot()
thinkplot.show()

#violin_wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
#thinkdsp.play_wave(filename='92002__jcveliz__violin-origional.wav', player='vlc')

#spectrum = violin_wave.make_spectrum()

#spectrum.plot()
#thinkplot.show()

#print(spectrum.framerate, "samples/sec")

#spectrum.high_pass(cutoff=1000, factor=0.05)
#filtered_violin = spectrum.make_wave()
#filtered_violin.write(filename="filtered_violin.wav")
#
#thinkdsp.play_wave(filename='filtered_violin.wav', player='vlc')


end_time = datetime.datetime.now()



#spectrum.plot()
#thinkplot.show()



#cos_sig.plot()
#thinkplot.config(xlabel='Time (s)')
#
#sin_sig.plot()
#thinkplot.config(xlabel='Time (s)')


delta = end_time - start_time
print(round(delta.microseconds/1000), "ms computation time\n")

