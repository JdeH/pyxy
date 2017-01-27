# ====== Legal notices
#
# Copyright (C) 2017 GEATEC engineering
#
# This program is free software.
# You can use, redistribute and/or modify it, but only under the terms stated in the licence.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# No need to use _ prefix, since

import sys as ss
import types as tp

import base as bs
import graphics_thread as gp
import timing_chart as tc

class CallableModule (tp.ModuleType):
    def __init__ (self):
        super () .__init__ (__name__)
        self._timingChart = tc.TimingChart ()
        self._graphicsThread = gp.GraphicsThread (self._timingChart)

    def __call__(self, *channelParamTuple):
        setattr (self, channelParamTuple [0], self._timingChart.addChannel (*channelParamTuple))
     
ss.modules [__name__] = CallableModule ()
