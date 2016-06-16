# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:18:56 2016

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

#waves = thinkdsp.read_wave(filename='241824__haldigital97__waves-1.wav')
#waves_spec = waves.make_spectrum()
#waves_spec.high_pass(100, 0.01)
#waves_spec.plot_power()
#pyplot.xlim(xmin=500)
#pyplot.xscale('log')
#pyplot.yscale('log')
#pyplot.show()

#-----------------------------

class UncorrelatedPoissonNoise(thinkdsp._Noise):
    def evaluate(self, ts):
        ys = np.random.poisson(self.amp, len(ts))
        return ys
        
p_sig = UncorrelatedPoissonNoise(amp=1)
p_wave = p_sig.make_wave(duration=5, framerate=11025)
#p_wave.write(filename='p_wave.wav')
#thinkdsp.play_wave(filename='p_wave.wav', player='vlc')

p_spec = p_wave.make_spectrum()
p_spec.hs[0] = 1
p_spec.plot_power()
pyplot.show()


