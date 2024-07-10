import math
import time
from numpy import cos, sin, array, linalg
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient


client = RemoteAPIClient()
sim = client.require('sim')
sim.loadScene('/Users/lticharwa/Desktop/test-sim.ttt')
t_end = 10 
r = 0.5 

def sysCall_init():
    global joint1
    global joint2
    global endEffector
    global endEffectorTrace
    global x_center
    global y_center
    sim.startSimulation()
    endEffector = sim.getObject('/EndEffector')
    endEffectorTrace = sim.addDrawingObject(sim.drawing_linestrip, 5, 0, -1, 100000,[1,0,0])
    joint2 = sim.getObject('/Joint2')
    joint1 = sim.getObject('/Joint1')
    moveToAngle(joint1, 45/180*math.pi)
    moveToAngle(joint2, -95/180*math.pi)
    
    endEffectorPosition = sim.getObjectPosition(endEffector, sim.handle_world)
    x = endEffectorPosition[0]
    y = endEffectorPosition[1]
    x_center = x - r
    y_center = y
    
def moveToAngle(jointAngle, targetAngle):
        sim.setJointTargetPosition(jointAngle, targetAngle)
        sim.step()
        time.sleep(0.01)  # Adding a small delay to let the simulation process

def ik_actuate ():
    sim.setStepping(True)    
    theta1 = sim.getJointPosition(joint1) 
    theta2 = sim.getJointPosition(joint2)
    print('theta1:', theta1, 'theta2:', theta2)
    l = 1
    J = np.array([[l*(np.cos(theta1) + np.cos(theta1 + theta2)), l*np.cos(theta1 + theta2)], \
                  [l*(np.sin(theta1) + np.sin(theta1 + theta2)), l*np.sin(theta1 + theta2)]])
    if(linalg.det(J) == 0):
        sim.stopSimulation()
        print('Jacobian:', J)
        print('Jacobian is singular, This occures when you attempt to invert a matrix with no inverse matrix i.e det(J) = 0, simulation ended')
        raise (ValueError('Jacobian is singular, This occures when you attempt to invert a matrix with no inverse matrix i.e det(J) = 0, simulation ended'))

    Jinv = linalg.inv(J)
    t = sim.getSimulationTime() 
    x_ref,y_ref = curve(t)
    effectorPos = sim.getObjectPosition(endEffector, sim.handle_world)
    x = effectorPos[0]
    y = effectorPos[1]
    dr = [x_ref - x,y_ref-y]
    dq = Jinv.dot(dr)
    
    theta1 += dq[0]
    theta2 += dq[1]
    
    moveToAngle(joint1,theta1)
    moveToAngle(joint2,theta2)
    if (t>=t_end):
        sim.stopSimulation()
        print('Simulation ended')
        exit()
    
def ik_sensing():
    effectorPos = sim.getObjectPosition(endEffector, sim.handle_world)
    sim.addDrawingObjectItem(endEffectorTrace, effectorPos)
    
def curve(t):
    f = 2*math.pi/t_end
  
    x_ref = x_center + r*math.cos(f*t)
    y_ref = y_center + r*math.sin(f*t)
    
    # y_ref = y_center --> y_center = y
    # x_ref = x_center + r --> x_center = x - r
    
    return x_ref, y_ref
          
def stop_sim():
    sim.stopSimulation()
 

    



