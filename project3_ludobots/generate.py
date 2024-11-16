import pyrosim.pyrosim as pyrosim
import random 

#Position Variables

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5



initial_size = [length, width, height]
initial_pos = [x,y,z]

def _create_tower(tower_height, position=[0,0,0.5], initial_block_size=[1,1,1]):
    
    initial_sizes = initial_block_size

    for count in range(10):
        sim_size = [dim * (0.9 ** count) for dim in initial_sizes]
        #Update z-coord
        position[2] += 1
        pyrosim.Send_Cube(name=f"box{count}", pos=position, size=sim_size)
    
def create_25_towers(height):           
    pyrosim.Start_SDF("boxes.sdf")
    for x in range(5):
        for y in range(5):
            pos = [x, y, 0.5]
            _create_tower(height, pos, initial_size)
    pyrosim.End()


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube("Box1", [-4,4,1],[2,2,2])
    pyrosim.End()


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube("Torso", [0,0,1.5],[1,1,1])
    
    pyrosim.Send_Cube("BackLeg", [-0.5, 0, -0.5],[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1.0])
    

    pyrosim.Send_Cube("FrontLeg", [0.5,0,-0.5],[1,1,1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1.0])
    
    pyrosim.End()
    

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    for source_neuron in range(0,3):
        for target_neuron in range(3,5):
            pyrosim.Send_Synapse( sourceNeuronName = source_neuron , targetNeuronName = target_neuron , weight = random.random() )
    
    
    
    pyrosim.End()


#create_25_towers(10)
Create_World()
Generate_Body()
Generate_Brain()
