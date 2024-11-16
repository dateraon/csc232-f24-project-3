import pybullet as p 
import pybullet_data
import time as t 
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):
        p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")