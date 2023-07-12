# -*- coding: utf-8 -*-
"""
    Create a set of vector pointing to the surface of a unit sphere
    
"""
import math
import numpy as np
import plotly.graph_objects as go; import plotly.io as pio; pio.renderers.default = 'browser'
from   elemental_rotation_matrix   import elemental_rotation_matrix


def create_unit_sphere(nY=51, nZ=51, PLOT=True):  # local function for the 3D failure envelope    
    anglesY = np.linspace(start=0, stop=2*math.pi,num=nY+1)
    anglesY = anglesY[1::]
    nY= len(anglesY)
    
    anglesZ = np.linspace(start=0, stop=2*math.pi,num=nZ+1)
    anglesZ = anglesZ[1::]
    
    Ry = elemental_rotation_matrix(axis='y', theta=anglesY, Type='rad')
    Rz = elemental_rotation_matrix(axis='z', theta=anglesZ, Type='rad')
    UnitVector = np.array([1,0,0])
    V = np.zeros([3,nY,nZ])
    for i in range(nY):
        for j in range(nZ):
            V[:,i,j] = Ry[:,:,i] @ Rz[:,:,j] @ UnitVector
    
    if PLOT:
        fig = go.Figure()
        Px = V[0,:,:].flatten()
        Py = V[1,:,:].flatten()
        Pz = V[2,:,:].flatten()
        colors = list(Pz)
        fig.add_trace(go.Scatter3d(x=Px, y=Py, z=Pz,
                             mode='markers', 
                             marker=dict(
                                         size=5,
                                         color=colors,                      # Assign colors based on the list of values
                                         colorscale='Viridis',              # Choose a colorscale
                                         colorbar=dict(title='Values'),     # Add a colorbar
                                         ), showlegend=False))     
        
        fig.show()
        fig.update_layout(title='Unit Ball')
        
    return V

