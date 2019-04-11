#!/usr/bin/python3
import motor as m
import ultra as u
import turn as t

# Initialization
m.setup()
dist = 0.5

# Loop
m.motorStart(1, m.Dir_forward, 100)
while 1:
    if u.checkdist() < dist:
        t.left()
        t.middle()
