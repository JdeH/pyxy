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


import time as tm
import collections as cl
import itertools as it
import copy as cp
import builtins as bi
import threading as th

import OpenGL.GL as gl
import OpenGL.GLUT as gt
import OpenGL.GLU as gu

import base as bs
import graphics_thread as gr

class Entry:
    def __init__ (self, chart, index, height):
        self.chart = chart
        self.index = index
        self.height = height
        self.top = self.chart.entries [-1] .bottom if self.chart.entries else 0
        self.bottom = self.top + self.height
        
    def display (self):
        pass
        
class Group (Entry):
    def __init__ (self, chart, index, text, height):
        Entry.__init__ (self, chart, index, height)
        self.text = text
       
class Channel (Entry):
    def __init__ (self, chart, index, name, color, min, max, height):
        super () .__init__ (chart, index, height)
    
        self.name = name
        self.colorRgb = bs.colorsRgb [color]
        self.min = min
        self.max = max
        self.height = height
        
        self.mean = (self.min + self.max) / 2
        
        self.ceiling = self.top + 2
        self.floor = self.bottom - 2
        self.middle = (self.floor + self.ceiling) / 2
        
        self.scale = (self.floor - self.ceiling) / (self.max - self.min)
        self.values = cl.deque ()
        
    def __call__ (self, value):
        self.chart.lock.acquire ()
        tm.sleep (0.05)
        self.chart.activeChannel = self
        if self.values:
            self.values.rotate (-1)
            self.values [-1] = value
            self.chart.pad ()
        self.chart.lock.release ()
            
    def pad (self):
        if self.chart.activeChannel != self:
            if self.values:
                self.values.rotate (-1)
                self.values [-1] = self.values [-2]
            
    def display (self):
        values = cp.copy (self.values)

        gl.glColor (*bs.backgroundFromRgb (self.colorRgb))
        gl.glBegin (gl.GL_QUADS)
        gl.glVertex (0, self.floor)
        gl.glVertex (self.chart.width, self.floor)
        gl.glVertex (self.chart.width, self.ceiling)
        gl.glVertex (0, self.ceiling)
        gl.glEnd ()
        
        gl.glColor (*self.colorRgb)
        gl.glBegin (gl.GL_LINE_STRIP)
        for iValue, value in enumerate (values):
            if value != None:
                value = max (min (value, self.max), self.min)
                gl.glVertex (1 * iValue, self.middle - self.scale * (value - self.mean))
        gl.glEnd ()
        
        gl.glRasterPos (2, self.middle + 5)
        gt.glutBitmapString (gt.GLUT_BITMAP_HELVETICA_12, self.name.encode ('ascii'))    

class TimingChart:
    def __init__ (self, name = None, width = 600, height = 400):
        self.name = name if name else self.__class__.__name__.lower ()
        self.width = width
        self.height = height
        self.entries = []
        self.lock = th.Lock ()
        self.activeChannel = None
        
    def createWindow (self):
        gt.glutInitWindowSize (self.width, self.height)
        self.window = gt.glutCreateWindow (bs.logName.encode ('ascii'))
        
        gl.glEnable (gl.GL_LINE_SMOOTH)
        gl.glEnable(gl.GL_BLEND);
        gl.glEnable (gl.GL_MULTISAMPLE)
        
        gl.glShadeModel (gl.GL_SMOOTH)
        gl.glHint (gl.GL_LINE_SMOOTH_HINT, gl.GL_DONT_CARE)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glLineWidth (1.5)
        
        gl.glDisable (gl.GL_LIGHTING)

        gt.glutDisplayFunc (self.displayCallback)
        gt.glutReshapeFunc (self.reshapeCallback)
        
    def pad (self):
        for self.entry in self.entries:
            self.entry.pad ()
      
    def display (self):
        gl.glColor (1, 1, 1)
            
        for entry in self.entries:
            entry.display ()
        
    def displayCallback (self):
        gl.glMatrixMode (gl.GL_MODELVIEW)
        gl.glLoadIdentity ()
        gl.glClearColor (0, 0, 0, 0)  
    
        gl.glClear (gl.GL_COLOR_BUFFER_BIT)   
        
        gl.glPushMatrix ()
        gl.glLineWidth (1)
        self.display ()
        gl.glPopMatrix ()
        
        gl.glFlush ()
        
        gt.glutSwapBuffers ()
        
    def reshapeCallback (self, width, height):
        self.width = width
        self.height = height
        
        gl.glViewport (0, 0, width, height)
        gl.glMatrixMode (gl.GL_PROJECTION);       
        gl.glLoadIdentity ()
        gl.glOrtho (0, self.width, self.height, 0, 0, 1)
        
        for entry in self.entries:
            if isinstance (entry, Channel):
                if self.width > len (entry.values):
                    entry.values =  cl.deque ([None for i in range (self.width - len (entry.values))] + list (entry.values))
                else:
                    start = len (entry.values) - self.width
                    stop = None
                    entry.values = cl.deque (it.islice (entry.values, start, stop))
        
    def addChannel (self, *args):
        channel = Channel (self, len (self.entries), *args)
        self.entries.append (channel)
        return channel
        