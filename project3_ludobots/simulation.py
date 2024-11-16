from world import WORLD
from robot import ROBOT 
import pybullet as p 
import pybullet_data
import time as t 
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c 

class SIMULATION: 
      
    def __init__(self): 
        self.physics_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,-9.8)
    
    def Run(self):
        for time_step in range(c.NUM_ITERATIONS):
            print(time_step)
            
            p.stepSimulation()
            self.robot.Sense(time_step)  
            self.robot.Think(time_step)
            self.robot.Act(time_step)   
            t.sleep(0.5 / 60.0) 
          
        
    def Save_Values(self):
        for sensor in self.robot.sensors.values():
            sensor.Save_Values()

    def __del__(self):
        self.Save_Values()  
        p.disconnect()