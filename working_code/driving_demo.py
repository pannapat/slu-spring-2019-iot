#!/usr/bin/python3
import motor as m
import ultra as u
import turn as t

# Initialization
m.setup()
t.middle()
dist = 0.4

def stopWhenObstacle():
    m.motorStart(1, m.Dir_forward, 80)
    while 1:
        if u.checkdist() < dist:
            m.motorStop()
            break

def turnLeftWhenObstacle():
    m.motorStart(1, m.Dir_forward, 80)
    while 1:
        if u.checkdist() < dist:
            t.left()
            while u.checkdist() < dist:
                pass
            t.middle()
            while 1:
                if u.checkdist() < dist:
                    m.motorStop()
                    break
            break
    
try:
    stopWhenObstacle()
except KeyboardInterrupt:
	m.destroy()


