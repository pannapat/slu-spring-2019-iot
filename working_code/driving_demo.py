#!/usr/bin/python3
import motor as m
import ultra as u
import turn as t

# Initialization
m.setup()
t.middle()
dist = 0.5

def stopWhenObstacle():
    m.motorStart(1, m.Dir_forward, 80)
    while 1:
        if u.checkdist() < dist:
            m.motorStop()
            break

def turnLeftWhenObstacle():
    m.motorStart(1, m.Dir_forward, 90)
    while 1:
        if u.checkdist() < dist:
            #m.motorStop()
            t.left()
            #m.motorStart(1, m.Dir_forward, 100)
            while u.checkdist() < dist:
                pass
            t.middle()
            while 1:
                if u.checkdist() < dist:
                    m.motorStop()
                    break
            
    
try:
    turnLeftWhenObstacle()
except KeyboardInterrupt:
	m.destroy()


