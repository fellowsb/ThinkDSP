# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:09:15 2016

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

wave = thinkdsp.read_wave(filename='28042__bcjordan__voicedownbew.wav')
spec_g = wave.make_spectrogram(1024)
spec_g.plot()
pyplot.ylim(ymax=4000)
pyplot.show()

seg_1 = wave.segment(start=0.2, duration=.002)

corrs_1 = np.correlate(seg_1.ys, seg_1.ys, "same")
length = len(seg_1.ts)
pyplot.plot(range(-length//2, length//2, 1), corrs_1)
pyplot.show()