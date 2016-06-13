# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:46:49 2016

@author: Ben
"""

from __future__ import print_function, division

import thinkdsp
import thinkplot

import matplotlib

import array
import copy
import math

import numpy as np
import random
import scipy
import scipy.stats
import scipy.fftpack
import struct
import subprocess
import thinkplot
import warnings

from fractions import gcd
from wave import open as open_wave

import matplotlib.pyplot as pyplot

#%precision 3
#%matplotlib inline

tri_signal = thinkdsp.TriangleSignal(freq=440)

tri_wave = signal.make_wave(0.01, framerate=10000)
tri_wave.plot()
thinkplot.show()

tri_spec = tri_wave.make_spectrum()
tri_spec.plot()
thinkplot.show()

print(tri_spec.hs[0])

tri_spec.hs[0] = 100

mod_wave = tri_spec.make_wave()

mod_wave.plot()
thinkplot.show()

#pyplot.ylim(0, 500)
#thinkplot.show()
#
#sq_sig = thinkdsp.SquareSignal(freq=1100)
#sq_wave = sq_sig.make_wave(1, framerate=96000)
#sq_seg = sq_wave.segment(0, sq_sig.period*4)
#sq_seg.plot()
#thinkplot.show()
#
#sq_spec = sq_wave.make_spectrum()
#sq_spec.plot()
#thinkplot.show()
#
#sq_wave.write(filename='sq_wave_1100hz.wav')
#thinkdsp.play_wave(filename='sq_wave_1100hz.wav', player='vlc')

#class SawtoothSignal(thinkdsp.Sinusoid):
#    
#    def evaluate(self, ts):
#        
#        
#        ts = np.asarray(ts)
#        cycles = self.freq * ts + self.offset / thinkdsp.PI2
#        frac, _ = np.modf(cycles)
#        ys = thinkdsp.normalize(thinkdsp.unbias(frac), self.amp)
#        return ys
#
#
#saw_sig = SawtoothSignal(freq=1)
#saw_sig.make_wave(duration=2)
#saw_sig.plot()

