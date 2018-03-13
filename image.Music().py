
# coding: utf-8

# In[1]:


# Import Commands
import wave
import numpy as np
#Library for Interaction of python with SonicPi
from psonic import *                     
from random import choice
#Library For importing image in python
from PIL import Image                    


# In[2]:


x = int(2)
time = 2

#Functions to define notes to be playes at different pixel intesity values
#Mapping for "Red" Base pixel intensities
def bas_zero(q):
    q.append("E" + str(x))
def bas_one(q):
    q.append("C" + str(x))
def bas_two(q):
    q.append("C" + str(x+1))
def bas_three(q):
    q.append("E" + str(x))
def bas_four(q):
    q.append("G" + str(x))
def bas_five(q):
    q.append("E" + str(x))
def bas_six(q):
    q.append("C" + str(x))
def bas_seven(q):
    q.append("C" + str(x+1))
def bas_eight(q):
    q.append("E" + str(x))
def bas_nine(q):
    q.append("G" + str(x))
#Mapping for "Red" Middle pixel intensities
def mid_zero(q):
    q.append("E" + str(x+1))
def mid_one(q):
    q.append("C" + str(x+1))
def mid_two(q):
    q.append("D" + str(x+1))
def mid_three(q):
    q.append("E" + str(x+1))
def mid_four(q):
    q.append("F" + str(x+1))
def mid_five(q):
    q.append("G" + str(x+1))
def mid_six(q):
    q.append("A" + str(x+1))
def mid_seven(q):
    q.append("B" + str(x+1))
def mid_eight(q):
    q.append("C" + str(x+1))
def mid_nine(q):
    q.append("B" + str(x))
#Mapping for "Red" Upper pixel intensities
def upp_zero(q):
    q.append("E" + str(x+2))    
def upp_one(q):
    q.append("C" + str(x+2))
def upp_two(q):
    q.append("D" + str(x+2))
def upp_three(q):
    q.append("E" + str(x+2))
def upp_four(q):
    q.append("F" + str(x+2))
def upp_five(q):
    q.append("G" + str(x+2))
def upp_six(q):
    q.append("A" + str(x+2))
def upp_seven(q):
    q.append("B" + str(x+2))
def upp_eight(q):
    q.append("C" + str(x+3))
def upp_nine(q):
    q.append("B" + str(x+2))


# In[3]:


# Hilbert Curve Coordinates Calculation
hilbert_map = {
    'a': {(0, 0): (0, 'd'), (0, 1): (1, 'a'), (1, 0): (3, 'b'), (1, 1): (2, 'a')},
    'b': {(0, 0): (2, 'b'), (0, 1): (1, 'b'), (1, 0): (3, 'a'), (1, 1): (0, 'c')},
    'c': {(0, 0): (2, 'c'), (0, 1): (3, 'd'), (1, 0): (1, 'c'), (1, 1): (0, 'b')},
    'd': {(0, 0): (0, 'a'), (0, 1): (3, 'c'), (1, 0): (1, 'd'), (1, 1): (2, 'd')},
}
def point_to_hilbert(x, y, order=16):
  current_square = 'a'
  position = 0
  for i in range(order - 1, -1, -1):
    position <<= 2
    quad_x = 1 if x & (1 << i) else 0
    quad_y = 1 if y & (1 << i) else 0
    quad_position, current_square = hilbert_map[current_square][(quad_x, quad_y)]
    position |= quad_position
  return position


# In[4]:


#Array for getting image mapping
img_map = np.random.randn(256*256,3)           
#Function to convert image to array using Hilbert Curve(A family of space filling curve)
def hilbertify(image):
   global img_map
   img = np.array(image)
   for x in range(256):
       for y in range(256):
           img_map[point_to_hilbert(x,y)] = img[x][y]
   img_map = img_map/255
image = Image.open('test.jpg')
hilbertify(image)


# In[5]:


#Pre-Processing for Sound Generation
img_map = img_map.T * 9
bas = img_map[0]
mid = img_map[1]
upp = img_map[2]
bas = [int(a) for a in bas]
mid = [int(a) for a in mid]
upp = [int(a) for a in upp]
mus_bas = []
mus_mid = []
mus_upp = []
#Setting notes for different pixel intensities
for i in bas:
    if i == 0:
        bas_zero(mus_bas)
    elif i==1:
        bas_one(mus_bas)
    elif i==2:
        bas_two(mus_bas)
    elif i==3:
        bas_three(mus_bas)
    elif i==4:
        bas_four(mus_bas)
    elif i==5:
        bas_five(mus_bas)
    elif i==6:
        bas_six(mus_bas)
    elif i==7:
        bas_seven(mus_bas)
    elif i==8:
        bas_eight(mus_bas)
    elif i==9:
        bas_nine(mus_bas)
        
for i in mid:
    if i == 0:
        mid_zero(mus_mid)
    elif i==1:
        mid_one(mus_mid)
    elif i==2:
        mid_two(mus_mid)
    elif i==3:
        mid_three(mus_mid)
    elif i==4:
        mid_four(mus_mid)
    elif i==5:
        mid_five(mus_mid)
    elif i==6:
        mid_six(mus_mid)
    elif i==7:
        mid_seven(mus_mid)
    elif i==8:
        mid_eight(mus_mid)
    elif i==9:
        mid_nine(mus_mid)
        
for i in upp:
    if i == 0:
        upp_zero(mus_upp)
    elif i==1:
        upp_one(mus_upp)
    elif i==2:
        upp_two(mus_upp)
    elif i==3:
        upp_three(mus_upp)
    elif i==4:
        upp_four(mus_upp)
    elif i==5:
        upp_five(mus_upp)
    elif i==6:
        upp_six(mus_upp)
    elif i==7:
        upp_seven(mus_upp)
    elif i==8:
        upp_eight(mus_upp)
    elif i==9:
        upp_nine(mus_upp)


# In[6]:


#time for "One Bar" of music
time = 4
#total length of music
time_music = 120
#size of input image
size = 256*256
#Variable to store final code to be run
play =""
# Code for individual color channels
sonic_bas = "in_thread do\nwith_fx :reverb do\nloop do\n"
sonic_mid = "in_thread do\nwith_fx :reverb do\nloop do\n"
sonic_upp = "with_fx :reverb do\nloop do\n"
#Time for each note on different color channel intensities
time_bas = str(time/4.0)
time_mid = str(time/8.0)
time_upp = str(time/16.0)
#Selecting some of the pixel values to make smooth music
jump_bas = (int(size/(time_music/float(time_bas)-3)))
jump_mid = (int(size/(time_music/float(time_mid)-3)))
jump_upp = (int(size/(time_music/float(time_upp)-3)))
mus_bas[0] = ":C3"
mus_mid[0] = ":E3"
mus_upp[0] = ":G3"
bas_run = ", :".join(mus_bas[::jump_bas])
mid_run = ", :".join(mus_mid[::jump_mid])
upp_run = ", :".join(mus_upp[::jump_upp])
sonic_bas = sonic_bas + "play_pattern_timed [ " + bas_run + "], "+time_bas+", amp: 3\nend\nend\nend"
sonic_mid = sonic_mid + "play_pattern_timed [ " + mid_run + "], "+time_mid+", amp: 3\nend\nend\nend"
sonic_upp = sonic_upp + "play_pattern_timed [ " + upp_run + "], "+time_upp+", amp: 3\nend\nend"
play = sonic_bas + "\n" + sonic_mid +"\n" + sonic_upp


# In[7]:


#for running the final code in Sonic Pi
run(play)


# In[8]:


#stop executing code on Sonic Pi
stop()

