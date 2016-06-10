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

import scipy.signal as ss
import scipy.stats as stats

wave = thinkdsp.read_wave(filename='28042__bcjordan__voicedownbew.wav')
spec_g = wave.make_spectrogram(1024)
spec_g.plot()
pyplot.ylim(ymin=250, ymax=550)
pyplot.show()
#seg_1 = wave.segment(start=0.2, duration=.002)
#
#corrs_1 = np.correlate(seg_1.ys, seg_1.ys, "full")[len(seg_1.ys):]
#length = len(corrs_1)
#offset = range(-length//2, length//2, 1)
#peaks = ss.find_peaks_cwt(corrs_1, np.arange(3,5))
#pyplot.plot(offset, corrs_1)
#pyplot.vlines(offset[peaks[-1]], 0, 6)
#pyplot.show()
#
#
#
#
#print(peaks)
#print(wave.framerate)

def serial_corr(wave, lag=1):
    n = len(wave)
    y1 = wave.ys[lag:]
    y2 = wave.ys[:n-lag]
    corr = np.corrcoef(y1, y2, ddof=0)[0, 1]
    return corr
    
def autocorr(wave):
    lags = range(len(wave.ys)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

def estimate_fundamental(wave, tracking_resolution=0.01):
    current_time = 0
    index = 0
    freq = []

    while (current_time + tracking_resolution < wave.duration):
        seg = wave.segment(start = current_time, duration = tracking_resolution)
#        auto_corr = np.correlate(seg.ys, seg.ys, "full")[len(seg.ys):]
        lags, corrs = autocorr(seg)
        stats.threshold(corrs, threshmin=0.999, newval=0)
     
#        peak_index = ss.find_peaks_cwt(auto_corr, np.arange(3,5))[-1]
        peak_index = ss.find_peaks_cwt(corrs, np.arange(20, 21))[1]        
        
        if index == 0: print(peak_index)
        
        freq.append(wave.framerate / peak_index)
        
        current_time += tracking_resolution
        index += 1
    return freq
    
def estimate_fundamental_faster(wave, tracking_resolution=0.01):
    current_time = 0
    freq = []

    while (current_time + tracking_resolution < wave.duration):
        seg = wave.segment(start = current_time, duration = tracking_resolution)
        N = len(seg)
        auto_corr = np.correlate(seg.ys, seg.ys, "same")
        
        lags = np.arange(-N//2, N//2)
        
        P = len(auto_corr)
        lengths = range(P, P//2, -1)
        
        half = auto_corr[P//2:].copy()
        half /= lengths
        half /= half[0]
                
#        lags, corrs = autocorr(seg)
        stats.threshold(half, threshmin=0.999, newval=0)
     
#        peak_index = ss.find_peaks_cwt(auto_corr, np.arange(3,5))[-1]
        peak_index = ss.find_peaks_cwt(half, np.arange(20, 21))[1]        
                      
        freq.append(wave.framerate / peak_index)
        
        current_time += tracking_resolution
        
    return freq
    
#frequencies = estimate_fundamental(wave)
#pyplot.plot(range(len(frequencies)), frequencies)
#pyplot.show()

frequencies = estimate_fundamental_faster(wave)
pyplot.plot(range(len(frequencies)), frequencies)
pyplot.show()
