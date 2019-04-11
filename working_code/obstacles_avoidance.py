#!/usr/bin/python3
import motor as m
import ultra as u
import turn as t

# Initialization
m.setup()
dist = 0.5

# Loop
try:
    m.motorStart(1, m.Dir_forward, 100)
    while 1:
        if u.checkdist() < dist:
            t.left()
            while u.checkdist() < dist:
                pass
            t.middle()
except KeyboardInterrupt:
	m.destroy()
