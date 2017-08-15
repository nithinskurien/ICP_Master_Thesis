#!/usr/bin/env python

from math import *
from Queue import Queue
import os

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y


class errorCalc:
    def __init__(self, newPath=None):
        if newPath is None:
            self.path = '/path.txt'
        else:
            #mainly used for testing with a testMap
            self.path = '/'+newPath

        self.queue = self.createQueuePath()
        p1= self.queue.get()
        p2= self.queue.get()
        self.queue.put(p1)
        self.queue.put(p2)
        self.line = (p1,p2)

    def calculateError(self, (backp0x, backp0y), (frontp0x, frontp0y), la):
        print "points: ",backp0x, backp0y , frontp0x, frontp0y

        lookahead = 350 +la

        #if backp0x -frontp0x ==0:
        #    #avoid division by 0
        #    if backp0x > frontp0x:
        #        #driving left
        #        theta = pi
        #    else:
        #        #driving right
        #        theta = 0
        #else:
        #    theta = atan((frontp0y - backp0y)/(frontp0x - backp0x))

        #distance = sqrt((frontp0y - backp0y)**2 + (frontp0x - backp0x)**2 )
        #x = (distance + lookahead) * cos(theta) + backp0x
        #y = (distance + lookahead) * sin(theta) + backp0y

        prevV =(frontp0x - backp0x , frontp0y - backp0y)
        mag = sqrt((frontp0x - backp0x)**2 + (frontp0y - backp0y)**2)
        nPrevV = tuple( comp/mag for comp in prevV )
        (x,y) = tuple(comp*lookahead for comp in nPrevV) #the vector from prevToPoint to newPoint
        x= x+frontp0x
        y= y+frontp0y
        print "forward x and y: ", x,y

        p0 = Point(x,y)
        (p1,p2) = self.line
        while self.isAboveEnd(p1,p2,p0):
            self.queue.put(p1)
            tempP1=p2
            tempP2=self.queue.get()
            self.line= (tempP1,tempP2)
            (p1,p2) = self.line

        isLeft = ((p2.x - p1.x)*(p0.y - p1.y) - (p2.y - p1.y)*(p0.x - p1.x)) >0 #decides if the error is to the left of centerline or not
        value = abs((p2.x - p1.x)*(p1.y-p0.y) - (p1.x-p0.x)*(p2.y-p1.y)) / (sqrt((p2.x-p1.x)*(p2.x-p1.x) + (p2.y-p1.y)*(p2.y-p1.y)))
        if (value > 1000):
            #reset queue, mainly for debugging
            self.queue = self.createQueuePath()
            p1= self.queue.get()
            p2= self.queue.get()
            self.queue.put(p1)
            self.queue.put(p2)
            self.line = (p1,p2)
        if(isLeft):
            return value
        else:
            return -value

    def isAboveEnd (self,begin, end, p0):
        #checks if a point is passed the end point of a line.
        if begin.x - end.x !=0 and begin.y - end.y !=0:
            slope = float(begin.y - end.y) / float(begin.x - end.x)
            prependularSlope = (-1)/slope
            prependularM = end.y - end.x*prependularSlope
            if begin.y < end.y:
                #going up
                return (p0.x*prependularSlope + prependularM - p0.y) < 0
            else:
                #going down
                return (p0.x*prependularSlope + prependularM - p0.y) > 0
        elif begin.x - end.x:
            #going straight in x direction
            if begin.x < end.x:
                #going right
                return p0.x > end.x
            else:
                #going left
                return p0.x < end.x
        else:
            #going straight in y direction
            if begin.y < end.y:
                #going up
                return p0.y > end.y
            else:
                #going down
                return p0.y < end.y

    def createQueuePath(self):
        #change path to path/to/gulliviewServer/src/path.txt
        dirpath = os.path.dirname(os.path.abspath(__file__))
        f = open(dirpath+self.path, 'r')
        lines = [line.rstrip('\n') for line in f.readlines()]
        posL = [s.split(' ', 1 ) for s in lines]
        queue = Queue()
        for l in posL:
            queue.put(Point(float(l[0]),float(l[1])))
        return queue
