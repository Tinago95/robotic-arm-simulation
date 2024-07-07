import math
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

maxForce = 100

client = RemoteAPIClient()
sim = client.require('sim')
sim.loadScene('/Users/lticharwa/Desktop/test-sim.ttt')

def moveToAngle(jointAngle, targetAngle):
        sim.setJointTargetPosition(jointAngle, targetAngle)
        for _ in range(100):  # Adjust the range as needed
            sim.step()
            time.sleep(0.01)  # Adding a small delay to let the simulation process
        
def actuate ():
    # enable the stepping mode on the client:
    sim.setStepping(True)
    # start simulation
    sim.startSimulation()
    
    joint2 = sim.getObject('/Joint2')
    joint1 = sim.getObject('/Joint1')
    moveToAngle(joint2,math.pi/2)
    theta1 = sim.getJointPosition(joint1)
    theta2 = sim.getJointPosition(joint2)
    print('theta1:', theta1, 'theta2:', theta2)
    
def stop_sim():
    sim.stopSimulation()
 






