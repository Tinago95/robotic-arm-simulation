# Make sure to have the add-on "ZMQ remote API" running in
# CoppeliaSim. Do not launch simulation, but run this script
from forward_kinematics import actuate,stop_sim,sensing
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

print('Program started')

maxForce = 100



 
# sim loop   
try:
    while True :
      sensing()
      actuate()
    
      
except KeyboardInterrupt:
    stop_sim()






