# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 04:49:08 2016

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
from IPython.display import display

#%matplotlib inline

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

cos_sig.plot()
thinkplot.config(xlabel='Time (s)')

sin_sig.plot()
thinkplot.config(xlabel='Time (s)')
