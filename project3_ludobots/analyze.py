import numpy 
import matplotlib.pyplot as matplot

backLegSensorValues = numpy.load('data/BackLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/FrontLegSensorValues.npy')
backMotor = numpy.load('data/motorBack.npy')
frontMotor = numpy.load('data/motorFront.npy')


matplot.plot(backMotor, label = "Back Leg Sensor", linewidth = 5)
matplot.plot(frontMotor, label = "Front Leg Sensor", linewidth = 1)

matplot.legend()
matplot.savefig('plot.png')
