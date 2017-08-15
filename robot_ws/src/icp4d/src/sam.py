import Vehicle
import numpy as np
import Measurement as me
import Pdfproduct as pdf
import Pdf
import math

a = np.matrix('0;0')
b = np.matrix('0 0;0 0')

#veh1 = Vehicle.Vehicle()
#[a, b] = veh1.predict(np.matrix('1; 1'), np.matrix('1 0; 0 1'), 1)
meas = me.Measurement()
meas.vehicle(1, 2)
meas.feature(2, 50)

m1 = np.matrix('1;1')
m2 = np.matrix('1.2;1.2')
m3 = np.matrix('1.2;1.2')
v1 = np.matrix('100 0;0 100')
v2 = np.matrix('100 0;0 100')
v3 = np.matrix('0.001 .000;.000 0.001')


X,Y,p = 2,2,.2
a, b = pdf.product(m1, m2, v1, v2)
print "Mean is :"
print a
print "Variance is :"
print b

Pdf.pdf(m3, v3)

