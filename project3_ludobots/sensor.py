import numpy as np 
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)
    
    def Get_Value(self, time_step):
        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    
    
    def Save_Values(self):     
        file_name = f"data/{self.linkName}_SensorValues.npy"
        np.save(file_name, self.values)
        print(f"Sensor values for {self.linkName} saved to {file_name}")

    