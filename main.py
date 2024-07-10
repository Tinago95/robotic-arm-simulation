# Make sure to have the add-on "ZMQ remote API" running in
# CoppeliaSim. Do not launch simulation, but run this script
import forward_kinematics as fk
import InverseKinematics as ik
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

print('Program started')

maxForce = 100



 
# sim loop   
try:
    ik.sysCall_init()
    while True :
      ik.ik_sensing()
      ik.ik_actuate()
    
      
except KeyboardInterrupt:
    ik.stop_sim()






