import math
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient


client = RemoteAPIClient()
sim = client.require('sim')
sim.loadScene('/Users/lticharwa/Desktop/test-sim.ttt')
endEffector = sim.getObject('/EndEffector')
joint2 = sim.getObject('/Joint2')
joint1 = sim.getObject('/Joint1')

endEffectorTrace = sim.addDrawingObject(sim.drawing_linestrip, 5, 0, -1, 100000,[1,0,0])
def moveToAngle(jointAngle, targetAngle):
        sim.setJointTargetPosition(jointAngle, targetAngle)
        sim.step()
        time.sleep(0.01)  # Adding a small delay to let the simulation process
        
def actuate ():
    # enable the stepping mode on the client:
    sim.setStepping(True)
    # start simulation
    sim.startSimulation()
    theta1 = sim.getJointPosition(joint1)
    theta2 = sim.getJointPosition(joint2)
    print('theta1:', theta1, 'theta2:', theta2)
    t = sim.getSimulationTime() 
    theta1 = math.pi*t/6
    theta2 = math.pi*t/3
    moveToAngle(joint2,theta2)
    moveToAngle(joint1,theta1)
    
def sensing():    
    effectorPos = sim.getObjectPosition(endEffector, sim.handle_world)
    sim.addDrawingObjectItem(endEffectorTrace, effectorPos)
    time.sleep(0.01)  # Adding a small delay to let the simulation process
        
def stop_sim():
    sim.stopSimulation()
 






