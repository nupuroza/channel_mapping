#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


# read data frame
df = pd.read_excel('channel_mapping.xlsx')


# In[ ]:


# function to find the start and end coordinates on an APA of a wire given the wire no. & which plane it belongs

def find_coords(plane, wire_no):
    
    if plane=='Y':
        
        h = 3991           # height of each APA

        dx = 3             # distance (mm) b/w wires on Y plane
        x = wire_no*3-dx/2

        return [(x,h),(x,0)]
    
    elif plane=='U':
    
        h = 3991        # height of each APA
        w = 2496*2      # width of each APA

        dx = 3/np.cos(np.pi/3)  # distance in x b/w wires on U/V plane
        dy = 3/np.sin(np.pi/3)  # distance in y b/w wires on U/V plane

        minx = dx/2-(w-dx*832)/2    # distance of first wire from sides of APA
        miny = dy/2-(h-dy*1152)/2   # distance of first wire from bottom/top of APA
        
        # find start coordinates
        if wire_no < 1153:     # side wires
            x0 = 0
            y0 = wire_no*dy - miny
        else:                  # top wires
            x0 = (wire_no-1152)*dx - minx
            y0 = h

        # find end coordinates
        if wire_no < 833:     # wires that end on bottom
            xf = wire_no*dx - minx
            yf = 0
        else:                 # wires that end on the side
            xf = w
            yf = (wire_no-832)*dy - miny  

        return [(x0,y0),(xf,yf)]
    
    elif plane=='V':
    
        h = 3991        # height of each APA
        w = 2496*2      # width of each APA

        dx = 3/np.cos(np.pi/3)  # distance in x b/w wires on U/V plane
        dy = 3/np.sin(np.pi/3)  # distance of first wire from bottom/top of APA

        minx = dx/2-(w-dx*832)/2    # distance of first wire from sides of APA
        miny = dy/2-(h-dy*1152)/2   # distance of first wire from bottom/top of APA

        if wire_no < 833:   # top wires
            x0 = wire_no*dx - minx
            y0 = h
        else:               # side wires
            x0 = w
            y0 = (1985-wire_no)*dy - miny

        if wire_no < 1153:      # wires that end on the side
            xf = 0
            yf = (1153-wire_no)*dy - miny
        else:                  # wires that end on bottom
            xf = (wire_no-1152)*dx - minx
            yf = 0  

        return [(x0,y0),(xf,yf)]


# In[4]:


# function that returns a tuple with ranges of wires in a list of all wires

def find_ranges(array):
    n = len(array)
    sarray = np.sort(array)   # ensure that wires are in order
 
    length = 1
    list = []
     
    for i in range (1, n + 1):
     
        if (i == n or sarray[i] -
            sarray[i - 1] != 1):
        
            if (length == 1):
                list.append(str(sarray[i - length]))
            else:
                temp = (sarray[i - length], sarray[i - 1])
                list.append(temp)
                
            length = 1
        
        else:
            length += 1
    return list


# In[ ]:


# function that plots the projection of wires given a specific WIB

def plotWIBprojection(WIB_crate, WIB_no):
    
    # select portion of data frame that corresponds to WIB
    df2 = df.loc[(df['WIB Crate #']==WIB_crate) & (df['WIB # (1-6)']==WIB_no)]
    
    # format figure
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_ylim(0, 3991+1)
    ax.set_xlim(0, 2496*2+1)
    ax.set_yticks([])
    ax.set_xticks([]) 
    
    # loop over planes
    for i, plane, color, nwires in [(0,'U','b', 1984), (1,'V', 'g', 1984), (2, 'Y', 'r', 1664)]:
        
        df2_plane = df2.loc[(df2['Wire plane']==plane)] 
        wires = np.array(df2_plane['Wire number'])
        
        # make backgrounds grid
        gridwires = np.arange(0, nwires, 64)
        for k in range(len(gridwires)):
            gridpoints = find_coords(plane, gridwires[k])
            ax.plot(*zip(*gridpoints), alpha=0.1, linestyle = '-', color='grey')
        
        # loop over wires in WIB
        for j in range(len(wires)):   
            plane_coords = find_coords(plane, wires[j])    # find coords
            ax.plot(*zip(*plane_coords), alpha=0.2, color=color)  # plot lines with specified coords
            
        # add a legend with # of wires on each plane and ranges
        if len(wires) > 0:
            wire_ranges = find_ranges(wires)
            no_wires = str(len(wires))
        else:
            wire_ranges = []
            no_wires = '0'
        
        x = 2496*2+100
        y = 3991 - 100 - 1500*i
        ax.text(x,y, no_wires+' '+plane+' wires', color = color)
        
        for l in range(len(wire_ranges)):
            wire_range = 'ch '+str(wire_ranges[l][0])+'-'+str(wire_ranges[l][1])
            y2 = y-(l+1)*200
            ax.text(x,y2, wire_range)
    
    # add a title
    if WIB_crate == 1 or WIB_crate == 3:
        apa = 'west'
    else:
        apa = 'east'
        
    if WIB_crate == 1 or WIB_crate == 2:
        half = 'South'
    else:
        half = 'North'
    
    ax.set_title('APA '+half+apa+' - WIB #'+str(WIB_no), weight='bold') 
    
    # more formatting
    ax.spines['bottom'].set_color('0.5')
    ax.spines['top'].set_color('0.5')
    ax.spines['right'].set_color('0.5')
    ax.spines['left'].set_color('0.5')
    fig.tight_layout()


# In[ ]:


# function that plots the projection of wires given a specific WIB fiber

def plotfiberprojection(WIB_crate, WIB_no, WIB_QFSP, WIB_fiber):
    
    # select portion of data frame that corresponds to WIB fiber
    df2 = df.loc[(df['WIB Crate #']==WIB_crate) & (df['WIB # (1-6)']==WIB_no) & (df['WIB QFSP']==WIB_QFSP) & (df['QFSP Fiber #']==WIB_fiber)]
    
    # format figure
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_ylim(0, 3991+1)
    ax.set_xlim(0, 2496*2+1)
    ax.set_yticks([])
    ax.set_xticks([]) 
    
    # loop over planes
    for i, plane, color, nwires in [(0,'U','b', 1984), (1,'V', 'g', 1984), (2, 'Y', 'r', 1664)]:
        
        df2_plane = df2.loc[(df2['Wire plane']==plane)] 
        wires = np.array(df2_plane['Wire number'])
        
        # make backgrounds grid
        gridwires = np.arange(0, nwires, 64)
        for k in range(len(gridwires)):
            gridpoints = find_coords(plane, gridwires[k])
            ax.plot(*zip(*gridpoints), alpha=0.1, linestyle = '-', color='grey')
        
        # loop over wires in WIB fiber
        for j in range(len(wires)):   
            plane_coords = find_coords(plane, wires[j])    # find coords
            ax.plot(*zip(*plane_coords), alpha=0.2, color=color)  # plot lines with specified coords
            
        # add a legend with # of wires on each plane and ranges
        if len(wires) > 0:
            wire_ranges = find_ranges(wires)
            no_wires = str(len(wires))
        else:
            wire_ranges = []
            no_wires = '0'
        
        x = 2496*2+100
        y = 3991 - 100 - 1500*i
        ax.text(x,y, no_wires+' '+plane+' wires', color = color)
        
        for l in range(len(wire_ranges)):
            wire_range = 'ch '+str(wire_ranges[l][0])+'-'+str(wire_ranges[l][1])
            y2 = y-(l+1)*200
            ax.text(x,y2, wire_range)
    
    # add a title
    if WIB_crate == 1 or WIB_crate == 3:
        apa = 'west'
    else:
        apa = 'east'
        
    if WIB_crate == 1 or WIB_crate == 2:
        half = 'South'
    else:
        half = 'North'
    
    ax.set_title('APA '+half+apa+' (WIB #'+str(WIB_no)+ '-' +WIB_QFSP+'-Fiber '+str(WIB_fiber)+')', weight='bold')
    
    # more formatting
    ax.spines['bottom'].set_color('0.5')
    ax.spines['top'].set_color('0.5')
    ax.spines['right'].set_color('0.5')
    ax.spines['left'].set_color('0.5')
    fig.tight_layout()

