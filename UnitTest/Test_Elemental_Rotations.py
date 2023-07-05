import os
from math import cos,sin,pi

test_wd = os.getcwd()   # test working directory
os.chdir("..")          # only needed in the 1st test to get to the source dir
main_wd = os.getcwd()   # main working directory

import unittest
import numpy as np

from Elemental_RotationMatrix import Elemental_RotationMatrix # Elemental_RotationMatrix(axis, theta, Type):

# import plotly.graph_objects as go
# import plotly.io as pio
# pio.renderers.default = 'browser'

os.chdir(test_wd)


class Test1_ElementalRotations(unittest.TestCase):
    

    def test_Identity(self): 
        I = np.eye(3)
        Rx = Elemental_RotationMatrix(axis='x', theta=np.array([0]), Type='rad')
        Ry = Elemental_RotationMatrix(axis='y', theta=np.array([0]), Type='rad')
        Rz = Elemental_RotationMatrix(axis='z', theta=np.array([0]), Type='rad')     
        assert max(abs(Rx.flatten()-I.flatten()))<1e-12, 'Rx is not identity if theta = 0'
        assert max(abs(Ry.flatten()-I.flatten()))<1e-12, 'Ry is not identity if theta = 0'
        assert max(abs(Rz.flatten()-I.flatten()))<1e-12, 'Rz is not identity if theta = 0'
        
        Rx = Elemental_RotationMatrix(axis='x', theta=np.array([0,0]), Type='rad')
        Ry = Elemental_RotationMatrix(axis='y', theta=np.array([0,0]), Type='rad')
        Rz = Elemental_RotationMatrix(axis='z', theta=np.array([0,0]), Type='rad')      
        assert max(abs(Rx[:,:,0].flatten()-I.flatten()))<1e-12, 'Rx is not identity if theta = 0'
        assert max(abs(Ry[:,:,0].flatten()-I.flatten()))<1e-12, 'Ry is not identity if theta = 0'
        assert max(abs(Rz[:,:,0].flatten()-I.flatten()))<1e-12, 'Rz is not identity if theta = 0'       
        assert max(abs(Rx[:,:,1].flatten()-I.flatten()))<1e-12, 'Rx is not identity if theta = 0'
        assert max(abs(Ry[:,:,1].flatten()-I.flatten()))<1e-12, 'Ry is not identity if theta = 0'
        assert max(abs(Rz[:,:,1].flatten()-I.flatten()))<1e-12, 'Rz is not identity if theta = 0'

        
    def test_90(self):   
        Rx = Elemental_RotationMatrix(axis='x', theta=np.array([90]), Type='deg')
        V  = Rx @ np.array([0,1,0])
        assert max(abs(V-np.array([0,0,1])))<1e-12, 'Rx 90 is incorrect'   
        
        Rx = Elemental_RotationMatrix(axis='x', theta=np.array([-90]), Type='deg')
        V  = Rx @ np.array([0,1,0])
        assert max(abs(V-np.array([0,0,-1])))<1e-12, 'Rx -90 is incorrect'          

        Rx = Elemental_RotationMatrix(axis='x', theta=np.array([90]), Type='deg')
        V  = Rx @ np.array([0,0,1])
        assert max(abs(V-np.array([0,-1,0])))<1e-12, 'Rx 90 is incorrect'   
 
        Ry = Elemental_RotationMatrix(axis='y', theta=np.array([90]), Type='deg')
        V  = Ry @ np.array([1,0,0])
        assert max(abs(V-np.array([0,0,-1])))<1e-12, 'Ry 90 is incorrect'   

        Ry = Elemental_RotationMatrix(axis='y', theta=np.array([-90]), Type='deg')
        V  = Ry @ np.array([1,0,0])
        assert max(abs(V-np.array([0,0,1])))<1e-12, 'Ry -90 is incorrect'       
             
        Rz = Elemental_RotationMatrix(axis='z', theta=np.array([90]), Type='deg')
        V  = Rz @ np.array([1,0,0])
        assert max(abs(V-np.array([0,1,0])))<1e-12, 'Rz 90 is incorrect'      
        
        Rz = Elemental_RotationMatrix(axis='z', theta=np.array([-90]), Type='deg')
        V  = Rz @ np.array([1,0,0])
        assert max(abs(V-np.array([0,-1,0])))<1e-12, 'Rz -90 is incorrect'    
        
        Rz = Elemental_RotationMatrix(axis='z', theta=np.array([90]), Type='deg')
        V  = Rz @ np.array([0,1,0])
        assert max(abs(V-np.array([-1,0,0])))<1e-12, 'Rz 90 is incorrect'    
      
        
    def test_TaitBryan(self):
        for i in range(10):
            x_deg = np.random.rand(1)*180-90
            y_deg = np.random.rand(1)*180-90
            z_deg = np.random.rand(1)*180-90
             
            Rx = Elemental_RotationMatrix(axis='x', theta=x_deg, Type='deg')
            Ry = Elemental_RotationMatrix(axis='y', theta=y_deg, Type='deg')
            Rz = Elemental_RotationMatrix(axis='z', theta=z_deg, Type='deg')            
            R  = Rz @ Ry @ Rx
            
            
            # https://en.wikipedia.org/wiki/Rotation_matrix
            # More formally, it is an intrinsic rotation whose Tait–Bryan angles are α, β, γ, about axes z, y, x, respectively. Similarly, the product
            gamma = x_deg*pi/180
            beta = y_deg*pi/180
            alpha = z_deg*pi/180 # alpha
            
            R_ana = np.array([[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma)-sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*sin(gamma)],
                              [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma)+cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma)],
                              [-sin(beta),           cos(beta)*sin(gamma),                                   cos(beta)*cos(gamma)]])
            
            assert max(abs(R.flatten()-R_ana.flatten()))<1e-12, 'R is not matching analytical epxression'
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    