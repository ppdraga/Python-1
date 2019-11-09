import matplotlib.pyplot as plot
import numpy


# y=x*2- cos(x)
def f1(t):
    return t*2 - numpy.cos(t)

# y=x^3- sqrt(x)
def f2(t):
    return t**3 - numpy.sqrt(t)


arr1 = numpy.arange(0, 15.0, 0.1)
arr2 = numpy.arange(0, 2.0, 0.1)

plot.figure(1)
plot.subplot(211)
plot.plot(arr1, f1(arr1), 'k')
plot.subplot(212)
plot.plot(arr2, f2(arr2), 'r')


plot.title('------')
plot.show()
