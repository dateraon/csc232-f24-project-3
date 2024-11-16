import pybullet as p 
import time as t 
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand
import math
import constants as c 

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName  
        
    
    def Set_Value(self, desiredAngle, robotId):
        
     
        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition = desiredAngle,

        maxForce = c.MOTOR_MAX_FORCE_BACK_LEG)



# ----------------------------------------UNUSED METHODS---------------------------------------------------#
'''
 def Prepare_To_Act(self):
        self.motorValues = np.zeros(1000)  
        self.amplitude = c.AMPLITUDE 
        self.frequency = c.FREQUENCY  
        self.offset = c.PHASEOFFSET 
        
         # Conditional to vary frequency based on joint name
        if self.jointName == b"Torso_BackLeg":
            self.frequency = c.FREQUENCY * 3  
        else:
            self.frequency = c.FREQUENCY / 2 
           
        
        time_steps = np.arange(1000)
        self.motorValues = self.amplitude * np.sin(self.frequency * time_steps * (2 * np.pi / 1000) + self.offset)
        
def Save_Values(self):
        # Save motor values to a file
        file_name = f"data/{self.jointName}_MotorValues.npy"
        np.save(file_name, self.motorValues)
        print(f"Motor values for {self.jointName} saved to {file_name}")
        
'''