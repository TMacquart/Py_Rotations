'''
    Evaluate Elemental_RotationMatrix (Rx, Ry, Rz)

     Rx = [1         0               0
           0   cos(theta)  -sin(theta)
           0   sin(theta)   cos(theta)]

    Ry = [cos(theta),     0     sin(theta)
              0           1         0
         -sin(theta),     0     cos(theta)]
        
    Rz = [ cos(theta)  -sin(theta)    0
           sin(theta)   cos(theta)    0 
               0           0          1]


'''

from math import pi
import numpy as np

def Elemental_RotationMatrix(axis, theta, Type):
    # axis is a string, either 'x', 'y', or 'z'
    # theta is a scalar or 1D-array of angles either an rad or deg.
    # Type = 'degree' or 'radians' 
    
    if Type == 'degree':
        # the angle is input in deg and converted into rad
        theta = theta*pi/180;
    
    n = len(theta)
    
    if axis == 'x':
        Rx = np.zeros(3,3,n)
        Rx[0,0,:] = np.ones(n) 
        Rx[1,1,:] = np.cos(theta)
        Rx[1,2,:] = -np.sin(theta)
        Rx[2,1,:] = np.sin(theta)
        Rx[2,2,:] = np.cos(theta)
        return Rx  
    
    if axis == 'y':
        Ry = np.zeros(3,3,n)
        Ry[0,0,:] = np.cos(theta)
        Ry[0,2,:] = np.sin(theta)
        Ry[1,1,:] = np.ones(n)
        Ry[2,0,:] = -np.sin(theta)
        Ry[2,2,:] = np.cos(theta)
        return Ry
    
    if axis == 'z':
        Rz = np.zeros(3,3,n)
        Rz[0,0,:] = np.cos(theta)
        Rz[1,1,:] = -np.sin(theta)
        Rz[1,2,:] = np.cos(theta)
        Rz[2,1,:] = np.sin(theta)
        Rz[2,2,:] = np.ones(n) 
        return Rz  
        