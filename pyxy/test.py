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

import sys as ss
import os
import threading as th
import time as tm

ss.path.append (os.path.abspath ('..'))

import pyxy as px

class TestThreadA (th.Thread):
    def __init__ (self):
        super () .__init__ ()
        self.a0 = 0
        px ('a0', 'red', 0, 100, 100)
        self.spike = 0
        px ('spike', 'white', 0, 1, 100)
        self.a1 = 0
        px ('a1', 'maroon', 0, 100, 100)
        self.start ()
        
    def run (self):
        while True:
            self.a0 = (self.a0 + 1) % 100
            px.a0 (self.a0)
            
            self.spike = self.a0 == 0
            px.spike (self.spike)
            
            self.a1 = (self.a1 + 2) % 100
            px.a1 (self.a1)
          
            tm.sleep (0.01)
    
testThreadA = TestThreadA ()

class TestThreadB (th.Thread):
    def __init__ (self):
        super () .__init__ ()
        self.b0 = 0
        px ('b0', 'lime', 0, 100, 100)
        self.b1 = 0
        px ('b1', 'green', 0, 100, 100)
        self.start ()
        
    def run (self):
        while True:
            self.b0 = (self.b0 + 1) % 100
            px.b0 (self.b0)
            
            self.b1 = (self.b1 + 2) % 100
            px.b1 (self.b1)
          
            tm.sleep (0.03)

testThreadB = TestThreadB ()
            
c0 = 0
px ('c0', 'blue', 0, 100, 100)
c1 = 0
px ('c1', 'navy', 0, 100, 100)
        
while True:
    c0 = (c0 + 1) % 100
    px.c0 (c0)
        
    c1 = (c1 + 2) % 100
    px.c1 (c1)
      
    tm.sleep (0.07)
    