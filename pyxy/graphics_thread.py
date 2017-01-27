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

import threading as th
import time as tm

import OpenGL.GL as gl
import OpenGL.GLUT as gt

class GraphicsThread (th.Thread):
    def __init__ (self, *charts):
        th.Thread.__init__ (self)
        self.daemon = True
        self.charts = charts
        self.start ()
        
    def idle (self):
        for chart in self.charts:
            gt.glutSetWindow (chart.window)
            gt.glutPostRedisplay ()
        tm.sleep (0.05)
           
    def run (self):
        gt.glutInit ()
        gt.glutInitDisplayMode (gt.GLUT_DOUBLE | gt.GLUT_RGB | gt.GLUT_DEPTH | gt.GLUT_MULTISAMPLE)   
        
        for chart in self.charts:
            chart.createWindow ()
            
        gt.glutIdleFunc (self.idle)
        gt.glutMainLoop ()
        