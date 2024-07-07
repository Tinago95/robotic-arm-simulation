# Make sure to have the add-on "ZMQ remote API" running in
# CoppeliaSim. Do not launch simulation, but run this script

import math

from coppeliasim_zmqremoteapi_client import RemoteAPIClient

print('Program started')

maxForce = 100

client = RemoteAPIClient()
sim = client.require('sim')

sim.loadScene('/Users/lticharwa/Desktop/test-sim.ttt')

def moveToAngle(jointAngle, targetAngle):
        sim.setJointTargetPosition(joint2, targetAngle)
        sim.setJointMaxForce(joint2, maxForce)
        sim.step()
     
joint2 = sim.getObject('/Joint2')
joint1 = sim.getObject('/Joint2')

jointAngle = sim.getJointPosition(joint2)
sim.setJointTargetVelocity(joint2, 360 * math.pi / 180)

# enable the stepping mode on the client:
sim.setStepping(True)

sim.startSimulation()

moveToAngle(joint2,45 * math.pi / 180)
moveToAngle(joint1,90 * math.pi / 180)
moveToAngle(joint2,-99 * math.pi / 180)  # no -90, to avoid passing below
moveToAngle(joint1,0 * math.pi / 180)

sim.stopSimulation()

print('Program ended')
