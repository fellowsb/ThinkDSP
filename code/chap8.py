# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:55:02 2016

@author: ben
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

import scipy.signal as ss
import scipy.stats as stats

sample_rate = 96000
points = 2048
x = np.arange(-points//2, points//2,1)
signal = ss.gaussian(M=points, std=60.0)

spec = np.fft.fft(signal, norm="ortho")
spec = np.fft.fftshift(np.abs(spec))
freqs = np.fft.fftfreq(points, d=1./sample_rate)
pyplot.plot(x, signal)


pyplot.plot(x, spec)
pyplot.show()