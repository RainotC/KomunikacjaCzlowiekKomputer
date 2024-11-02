#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
import math
from matplotlib import rc
import numpy as np

from matplotlib import colors

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True) 
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

def hsv2rgb(h, s, v):
    if s==0:
        return (v, v, v)
    else:
        hi = math.floor(h/60)
        f = h/60 - hi
        
        p = v *(1-s)
        
        q = v* (1 - s*f)
        
        t = v * (1 - s *(1 - f))
        if hi == 0:
            return v, t, p
        elif hi == 1:
            return q, v, p
        elif hi == 2:
            return p, v, t
        elif hi == 3:
            return p, q, v
        elif hi == 4:
            return t, p, v
        elif hi == 5:
            return v, p, q
        



def gradient_rgb_bw(v):

    return (v, v, v)


def gradient_rgb_gbr(v):
    if v<=0.5:
        z = 1 - v *2
        b = v * 2
        return (0, z, b)
    else:
        b = (1-v)*2
        r = 2* (v - 0.50)
        return (r,0, b)

def gradient_rgb_gbr_full(v):
    if v<=0.25:
        b = v*4
        return (0, 1, b)
    elif v<=0.5:
        g = 1 -  (v - 0.25) * 4
        return(0 , g, 1)
    elif v <=0.75:
        r = (v-0.5) * 4
        return (r, 0 , 1)
    else:
        b = 1 - (v - 0.75) *4
        return(1, 0, b)


def gradient_rgb_wb_custom(v):
    if v<= 0.1428:
        a = 1 - v * 7
        return (1, a, 1)
    elif v <= 0.2856:
        r = 1- (v-0.1428) *7
        return (r, 0, 1)
    elif v <= 0.4284:
        g = (v - 0.2856) * 7
        return (0, g, 1)
    elif v <= 0.5712:
        b = 1 - (v - 0.4284) *7
        return (0, 1, b)
    elif v < 0.714:
        r = (v- 0.5712) * 7
        return (r, 1, 0)
    elif v <= 0.8568:
        g = 1 - (v - 0.714) * 7
        return (1, g, 0)
    elif v <= 0.9996:
        z = 1 - (v - 0.8568) *7
        return (z, 0, 0)
    else:
        return (0,0,0)
def gradient_hsv_bw(v):
    return hsv2rgb(0, 0, v)


def gradient_hsv_gbr(v):
    s = 1
    v1 = 1
    h = 120+ v * (240)

    return hsv2rgb(h, s, v1)

def gradient_hsv_unknown(v):
    s = 0.5
    v1 = 1
    h = (360-(120+ v * (240)))/2
    return hsv2rgb(h, s, v1)


def gradient_hsv_custom(v):
    s = v
    v1 = (1 - v*0.3)
    h = (120+ v * (240))
    return hsv2rgb(h, s, v1)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
