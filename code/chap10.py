# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:47:21 2016

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

response = thinkdsp.read_wave('180960__kleeb__gunshot.wav')
response = response.segment(start=0.26, duration=5.0)
response.normalize()
transfer = response.make_spectrum()
transfer.plot()

violin = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
violin.truncate(len(response))
violin.normalize()
v_spec = violin.make_spectrum()

output = (v_spec * transfer).make_wave()
output.normalize()

output.write('violin_room.wav')


