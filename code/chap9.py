# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:15:51 2016

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

import pandas as pd

#names = ['date', 'open', 'high', 'low', 'close', 'volume']
#df = pd.read_csv('fb.csv', header=0, names=names)
#ys = df.close.values
#close = thinkdsp.Wave(ys, framerate=1)
#spectrum = close.make_spectrum()
#int_spec = spectrum.copy()
##integration
#int_spec.hs = int_spec.hs / (PI2 * 1j * int_spec.fs)
#int_spec.hs[0] = 0
#
##cumulative sum
#cumsum_wav = close.cumsum()
#cumsum_spec = cumsum_wav.make_spectrum()
#
#close.plot()
#pyplot.show()
#
#cumsum_wav.plot()
#pyplot.show()
#
#cumsum_spec.plot()
#pyplot.show()

#these operations only work on periodic waves...
#inv_close = int_spec.make_wave()
#inv_close.plot()
#pyplot.show()

sq_sig = thinkdsp.SawtoothSignal()
sq_wav = sq_sig.make_wave()

sq_wav.plot()
pyplot.xlim(0,.01)
#pyplot.show()

cs_wav = sq_wav.cumsum()
cs_wav.normalize()
cs_wav.unbias()
cs_wav.plot()
pyplot.xlim(0,.01)
#pyplot.show()

sq_spec = sq_wav.make_spectrum()
int_spec = sq_spec.integrate()
int_wav = int_spec.make_wave()
int_wav.plot()
pyplot.xlim(0,.01)
pyplot.show()